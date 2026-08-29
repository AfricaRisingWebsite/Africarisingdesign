# Africa Rising Investments website prototype

A lightweight, responsive one-page prototype built with semantic HTML, modern CSS and minimal JavaScript. It is ready for static hosting and contains no database, framework, API keys or form-processing dependency.

## Preview

Open `index.html` directly for a quick preview, or serve the folder through any simple local web server. Serving the folder is recommended because it matches production hosting more closely.

## Included

- Original SVG brand mark and wordmark
- Optimised WebP hero artwork
- Responsive desktop, tablet and mobile layouts
- Keyboard-accessible mobile navigation
- Reduced-motion support and visible focus states
- Six primary service cards
- Robert Bwire leadership section with an honest portrait placeholder
- Selected-experience timeline with client-verification flags
- Sector perspective and proposed editorial topics
- Downloadable historical investment library containing the three supplied PDFs
- Professional advertising section
- Contact and social links with unverified details withheld
- Content verification checklist

## Publication status

This is a review prototype, not an approved public website. `robots` is set to `noindex, nofollow`. Remove that restriction only after content approval, the final domain is known and the canonical/metadata values have been updated.

## GitHub Pages preview

This package is prepared for the public repository:

`https://github.com/AfricaRisingWebsite/Africarisingdesign`

Upload the **contents of this folder** to the root of the repository so that `index.html` is visible on the repository's first screen. Do not upload the parent `africa-rising-prototype` folder as a single nested folder.

After the files are committed:

1. Open the repository's **Settings** tab.
2. Select **Pages** under **Code and automation**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Select branch **main**, folder **/(root)**, then choose **Save**.
5. Wait for GitHub to report that the site is live.

The shareable review address will be:

`https://africarisingwebsite.github.io/Africarisingdesign/`

The preview remains marked `noindex, nofollow`, and `robots.txt` blocks crawling. This keeps it suitable for client review without inviting search-engine indexing. Remove both safeguards only after final approval.

## Cloudflare Pages (future option)

For a future Git-connected Cloudflare deployment:

- Production branch: `main`
- Build command: none
- Output directory: repository root (if this folder becomes the repository root)

Do not connect `africa.or.ke`, alter nameservers or modify existing DNS until the current website and all DNS/email records have been backed up, the client has approved this prototype, and a rollback plan exists.

## GitHub packaging

Before pushing, confirm that only public website assets are present. Do not include credentials, private correspondence, the browser installer from the parent folder, temporary render files or unapproved source material beyond the intended downloadable publications.

## Finalisation

Complete every item in `CONTENT-VERIFICATION.md`, replace the portrait placeholder, confirm the two uncertain publication dates, add the approved privacy policy, change robots indexing and generate `robots.txt` and `sitemap.xml` once the production domain is final.
