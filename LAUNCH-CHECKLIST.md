# Launch checklist

Mechanical switches to flip when the client approves publication. Work top to bottom.

## 1. Remove the prototype signals

- [ ] Delete the `<aside class="review-bar">…</aside>` line from all 11 HTML files.
- [ ] Delete the line `<meta name="robots" content="noindex, nofollow">` from all 11 HTML files.
- [ ] Replace `robots.txt` with the launch version already written inside it as comments.
- [ ] Delete or resolve every `class="flag"` block. Each one names an unverified fact —
      resolve the fact first (see `CONTENT-VERIFICATION.md`), then remove the flag.
- [ ] Change the footer line "Prototype for client review — not for public distribution."

Quick sweep to find what is left:

```bash
grep -rn "review-bar\|noindex\|class=\"flag\"\|VERIFY BEFORE LAUNCH" --include="*.html" .
```

## 2. Confirm the production domain

- [x] Canonical, Open Graph, JSON-LD and sitemap URLs are set to the GitHub Pages preview:

```bash
https://africarisingwebsite.github.io/Africarisingdesign/
```

If a custom production domain is connected later, replace this base URL everywhere.

- [ ] Update `lastmod` dates in `sitemap.xml`.

## 3. Contact details

- [ ] Replace the Gmail address with the domain address in all files.
- [ ] In `contact/index.html`, uncomment the `tel:` block and insert the confirmed number.
      Remove the accompanying flag and the "Not published pending verification" line.
- [ ] Add the LinkedIn link to the footer, the contact page and the `sameAs` array in the
      Organization JSON-LD.

## 4. Content

- [ ] Insert the approved portrait: replace the `.portrait` block in `index.html` and
      `about/index.html` with `<img src="…" alt="Robert Bwire" width="…" height="…">`.
- [ ] Insert the approved biography and qualifications in `about/index.html`.
- [ ] Complete the EAC/AfDB engagement entry in `about/index.html`.
- [ ] Add registered entity details to the footer and `privacy/index.html`.
- [ ] Publish at least two more articles before launch if possible — one article makes an
      insights section look abandoned.

## 5. Form

- [ ] Configure a form handler.
- [ ] Set the `action` and `method` on the form in `contact/index.html`, remove `disabled`
      from every field and from the submit button, remove `aria-disabled`, remove the
      `onsubmit="return false"`, and delete the explanatory flag.
- [ ] Add a success page or inline success state, and test an actual submission end to end.
- [ ] Confirm the privacy notice still describes what the form does.

## 6. Final verification

- [ ] Run a link check across the live site.
- [ ] Run Lighthouse on the live URL. Targets: Performance ≥ 95, Accessibility 100,
      Best Practices 100, SEO 100.
- [ ] Confirm the three PDFs download over HTTPS.
- [ ] Test the Open Graph card in a real share (LinkedIn Post Inspector, Facebook Debugger).
- [ ] Submit `sitemap.xml` in Google Search Console.
- [ ] Check the site on a real phone on a mobile network, not only in a simulator.
