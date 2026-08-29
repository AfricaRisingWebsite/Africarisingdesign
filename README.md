# Africa Rising Investments — website prototype (v2)

A static, multi-page website for Africa Rising Investments. No framework, no build step,
no database, no API keys. Every file in this folder is deployable as-is.

**Status: prototype for client review. Not for public release.** See
`CONTENT-VERIFICATION.md` for the list of facts still awaiting confirmation and
`LAUNCH-CHECKLIST.md` for the switches to flip before going live.

---

## Preview it locally

The site uses directory-style URLs (`/expertise/`), so it needs a local web server —
opening `index.html` straight from the file system will break the internal links.

```bash
cd africa-rising-investments
python3 -m http.server 8080
# then open http://localhost:8080
```

Any static server works (`npx serve`, `php -S localhost:8080`, VS Code Live Server).

---

## What is here

```
africa-rising-investments/
├── index.html                     Home
├── expertise/index.html           All eight services, grouped by the four lenses
├── expertise/rapporteur/          Rapporteur & conference services
├── about/index.html               Robert Bwire, method, selected experience
├── insights/index.html            Article index + proposed editorial topics
├── insights/eac-guidebooks-what-still-holds/   Seed article
├── library/index.html             Annotated investment library + EAC reference
├── partner/index.html             Sponsorship & institutional notices
├── contact/index.html             Routed enquiries + disabled form preview
├── privacy/index.html             Draft privacy notice (Kenya DPA 2019 aware)
├── 404.html                       Not-found page (uses root-absolute paths)
├── robots.txt                     Currently blocks all indexing — see launch checklist
├── sitemap.xml                    Placeholder domain — update before launch
├── site.webmanifest
├── .nojekyll                      Stops GitHub Pages running Jekyll
├── .gitignore
└── assets/
    ├── css/styles.css             Design system (tokens, components, motion)
    ├── css/fonts.css              Self-hosted @font-face declarations
    ├── js/site.js                 ~100 lines, progressive enhancement only
    ├── fonts/                     Manrope + DM Sans woff2 (SIL OFL)
    ├── logo/                      SVG logo family
    ├── img/                       OG share image + app icons
    └── publications/              The three EAC PDFs
```

## Design system at a glance

| Token | Value | Use |
|---|---|---|
| `--forest` | `#123C32` | Primary brand green, buttons, dark bands |
| `--forest-deep` | `#082820` | Hero, footer, deepest ground |
| `--ivory` / `--ivory-warm` | `#F4F1E8` / `#FAF8F2` | Section grounds |
| `--gold` | `#C4A35A` | Accent only. **Never body text on light** (2.1:1) |
| `--gold-ink` | `#7F6326` | The gold-toned text colour that passes AA (5.0:1 on ivory) |
| `--charcoal` | `#16211D` | Body text (14.7:1 on ivory) |
| `--slate` | `#4E5C56` | Secondary text (6.2:1 on ivory) |
| `--sage` | `#B7C9C1` | Secondary text on dark (7.1:1 on forest) |

Type: Manrope (headings) / DM Sans (body), self-hosted, with full system fallback stacks.
Fluid `clamp()` scale, 68ch measure, 17px minimum body size.

**Gold rule:** gold is used for rules, indices, focus rings, small marks and headline
emphasis on dark grounds only. It never carries body copy on a light background.

## Verified quality gates

Run against Chromium at 1440×900, 1280×720, 1024×768, 768×1024, 390×844 and 375×667
(66 page/viewport combinations):

- Zero horizontal overflow
- Zero console errors, zero failed requests, zero broken internal links (33 targets)
- Zero axe-core violations (WCAG 2.0/2.1/2.2 A + AA + best practice) across all 11 pages
- Exactly one `<h1>` per page, no heading-level skips
- Every tab stop has a visible focus ring
- Full content and working navigation with JavaScript disabled
- `prefers-reduced-motion` honoured — no element is hidden behind an animation
- Homepage transfer ≈ 152 KB including self-hosted fonts

## Technical notes

- **No third-party requests.** Fonts are self-hosted, there is no analytics, no cookies,
  no tracking and nothing stored in the browser. This matters for government and DFI
  visitors on restricted networks, and it is what makes the privacy notice truthful.
- **JavaScript is optional.** `site.js` adds the scrolled header state, the mobile menu,
  section reveals and the footer year. Without it a `<noscript>` block turns the mobile
  nav into a plain list and all content renders immediately.
- **The 404 page uses root-absolute paths** because it can be served from any URL depth.
  Every other page uses relative paths, so the site also works from a subdirectory.
- **The review banner** is the gold strip at the top of every page. It lives in
  `lib`-generated markup as an `<aside class="review-bar">` inside `<header>`; delete
  that one line per page at launch.

## Licences

Manrope and DM Sans are used under the SIL Open Font License; licence texts are in
`assets/fonts/`. The three PDFs in `assets/publications/` are publications of the East
African Community and the African Development Bank and are included as reference material.
Africa Rising Investments is not their author and claims no contribution to them.

## A note on the PDF sizes

The three publications are shipped unaltered — they are third-party official documents and
re-compressing them would change what the client is redistributing. Two are large (9.3 MB
and 7.4 MB), so the file size is printed next to every download button and announced to
screen readers. If bandwidth becomes a concern, the honest options are to host them
externally or to link to the publishers' own copies rather than to silently degrade them.
