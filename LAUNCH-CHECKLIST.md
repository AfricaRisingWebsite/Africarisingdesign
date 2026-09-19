# Production checklist

The website is live at <https://africarisingwebsite.github.io/Africarisingdesign/>.
The public pages have no prototype banner, use launch-ready footers, allow search-engine
indexing, and publish the production sitemap.

## Completed

- [x] Removed public client-review and prototype labels.
- [x] Removed `noindex` from every public page; the custom 404 correctly remains `noindex, follow`.
- [x] Set `robots.txt` to allow crawling and publish the sitemap location.
- [x] Set canonical, Open Graph and structured-data URLs to the live GitHub Pages domain.
- [x] Replaced the disabled contact form with working, pre-addressed email routes.
- [x] Removed unverified telephone and LinkedIn placeholders from public pages.
- [x] Removed all downloadable PDFs and download buttons at the owner's request.
- [x] Checked headings, local links, assets, duplicate IDs and deployment URLs across all pages.
- [x] Tested desktop, phone and landscape layouts without horizontal overflow.

## Optional enhancements

- [ ] Move from Gmail to a domain email address and update every `mailto:` link and JSON-LD entry.
- [ ] Add a confirmed international telephone number if telephone contact is required.
- [ ] Add the approved company or Robert Bwire LinkedIn profile.
- [ ] Add an approved professional portrait and any qualifications intended for publication.
- [ ] Connect a custom domain if the firm wants a shorter public address.
- [ ] Configure Google Search Console and submit `sitemap.xml`.
- [ ] Test the Open Graph card through LinkedIn Post Inspector and Facebook Sharing Debugger.
- [ ] Add more published insight articles through `.codex/skills/publish-africa-rising-article/`.

## Before each release

1. Run `python tools/test-static-site.py`.
2. Open the changed pages at desktop and phone widths.
3. Test every changed email and external link.
4. Confirm `git diff --check` and review the complete staged file list.
5. After pushing, verify the live URLs and the custom 404 page.
