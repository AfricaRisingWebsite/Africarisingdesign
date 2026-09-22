from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import json
import sys


ROOT = Path(__file__).resolve().parents[1]
PAGES_PREFIX = "/"


class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.headings = []
        self.refs = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if "id" in data:
            self.ids.append(data["id"])
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings.append(int(tag[1]))
        if tag == "img" and "alt" not in data:
            self.errors.append("img missing alt")
        if tag in {"a", "link"} and "href" in data:
            self.refs.append((tag, data["href"]))
        if tag in {"script", "img", "source"} and "src" in data:
            self.refs.append((tag, data["src"]))
        if tag == "a" and data.get("target") == "_blank" and "noopener" not in data.get("rel", ""):
            self.errors.append(f"target=_blank missing noopener: {data.get('href', '')}")


def page_url(path):
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def local_target(current_url, ref):
    if not ref or ref.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    parts = urlsplit(ref)
    if parts.scheme or parts.netloc:
        return None
    path = unquote(urljoin(current_url, parts.path))
    if path.startswith(PAGES_PREFIX):
        path = "/" + path[len(PAGES_PREFIX) :]
    rel = path.lstrip("/")
    target = ROOT / rel
    if not rel or path.endswith("/"):
        target = target / "index.html"
    return target


def main():
    failures = []
    pages = sorted(ROOT.rglob("*.html"))
    for page in pages:
        parser = AuditParser()
        parser.feed(page.read_text(encoding="utf-8"))
        rel = page.relative_to(ROOT).as_posix()
        failures.extend(f"{rel}: {err}" for err in parser.errors)
        if len([h for h in parser.headings if h == 1]) != 1:
            failures.append(f"{rel}: expected exactly one h1")
        for previous, current in zip(parser.headings, parser.headings[1:]):
            if current > previous + 1:
                failures.append(f"{rel}: heading level jumps h{previous} to h{current}")
        duplicate_ids = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
        if duplicate_ids:
            failures.append(f"{rel}: duplicate ids {duplicate_ids}")
        current_url = page_url(page)
        for tag, ref in parser.refs:
            target = local_target(current_url, ref)
            if target is not None and not target.exists():
                failures.append(f"{rel}: broken {tag} reference {ref} -> {target.relative_to(ROOT)}")

    manifest = json.loads((ROOT / "site.webmanifest").read_text(encoding="utf-8"))
    for icon in manifest.get("icons", []):
        target = local_target("/", icon.get("src", ""))
        if target is not None and not target.exists():
            failures.append(f"site.webmanifest: missing icon {icon.get('src')}")

    for path in ROOT.rglob("*.pdf"):
        failures.append(f"Downloadable PDF remains: {path.relative_to(ROOT)}")
    for page in pages:
        import re
        if re.search(r"(?i)\.pdf|\bdownload\s*(?:=|>)", page.read_text()):
            failures.append(f"Download reference remains: {page.relative_to(ROOT)}")

    placeholder = "africa-rising-investments.pages.dev"
    for path in list(ROOT.rglob("*.html")) + list(ROOT.rglob("*.xml")):
        if placeholder in path.read_text(encoding="utf-8"):
            failures.append(f"{path.relative_to(ROOT)}: placeholder domain remains")

    print(f"Audited {len(pages)} HTML pages.")
    if failures:
        print("\n".join(f"FAIL: {item}" for item in failures))
        return 1
    print("PASS: headings, IDs, images, local links, manifest assets, and deployment URLs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
