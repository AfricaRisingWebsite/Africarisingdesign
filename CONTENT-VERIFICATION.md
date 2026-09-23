# Content verification checklist

Every item below is either unconfirmed, incomplete, or deliberately withheld from the
site. Nothing on this list was invented or guessed. Work through it with Robert before
the site is published.

Priority order reflects impact on credibility, not effort.

---

## Priority 1 — blocks launch

| # | Item | Current state on the site | What is needed |
|---|---|---|---|
| 1 | ~~**Professional email address**~~ CHANGED 23 Sep 2026 | `africarisinginvestments@gmail.com` published throughout | Client instruction (23 Sep 2026): use the Gmail address. All 59 instances of `africa@africa.or.ke` replaced across 12 pages and the capability-statement generator. The `africa@africa.or.ke` mailbox still exists at WebHost Kenya but is no longer published. |
| 2 | ~~**Telephone number**~~ RESOLVED 20 Sep 2026 | `+254 788 695 599` on `/contact/`, in every footer, and in the Organization JSON-LD | Client supplied `+254788695599` in feedback round 1. Still to confirm: that the line is answered during business hours. |
| 3 | ~~**Robert Bwire’s photograph**~~ RESOLVED | Supplied portrait published on the home page and About page | Client supplied the image. |
| 4 | **Robert Bwire's approved biography** | A short profile written from the confirmed facts only | The biography Robert wants published, in his own words. |
| 5 | **Qualifications and memberships** | Not shown | Degrees, professional certifications and memberships, with awarding bodies. |
| 6 | **EAC / AfDB engagement** | One cautious sentence, prominently flagged, with no dates or scope | The project title, the contracting party, the dates and a one-paragraph scope. This is potentially the strongest of the three engagements and is currently the vaguest. |
| 7 | **Privacy notice** | Published against the site&rsquo;s current behaviour and the Kenya Data Protection Act, 2019 | A qualified legal review remains recommended. Add the registered entity name, registration number, registered address and named data-protection contact when available. |

## Priority 2 — needed for a complete site

| # | Item | Current state | What is needed |
|---|---|---|---|
| 8 | **COMESA engagement wording** | Published as supplied, flagged for approval | Confirmation that the description is accurate and may be published. |
| 9 | **DFID BERF engagement wording** | Published as supplied, flagged for approval | Confirmation of wording and of the 2018 date. |
| 10 | **LinkedIn URL** | Omitted | The correct company or personal profile URL. The address supplied pointed to a generic LinkedIn feed. |
| 11 | **TikTok handle spelling** | `@africarisinginvesstments` used exactly as supplied | Confirm the double "s" is correct and not a typo. |
| 12 | **Authorship of the three publications** | Explicitly disclaimed everywhere they appear | If Robert contributed to any of them — particularly the 2013 EAC/AfDB guidebook — that is a significant credibility asset currently going unused. If so, supply the exact nature of the contribution and it can be stated accurately. |
| 13 | **Company registration** | Not shown | Registered name, registration number and jurisdiction, and whether they should appear in the footer. |
| 14 | **Physical / registered address** | "Nairobi, Kenya" only | Whether a fuller address should be published. |
| 15 | **Advertising criteria and rates** | `/partner/` describes formats and standards. No rates invented. | Rate card, specifications, lead times and approval process. |
| 16 | **Form handler** | The enquiry form is visibly disabled with an explanation. It does not silently fail. | Choose and configure a handler (Formspree, Cloudflare Workers, Netlify Forms) and enable the form. |

## Round 2 feedback — actioned 20 Sep 2026

| Item | What was asked | What was done |
|---|---|---|
| Contact address | Everything to go to `africarisinginvestments@gmail.com` | 23 Sep 2026: client reversed the 20 Sep decision; all 59 `africa@africa.or.ke` references replaced with the Gmail address. |
| "LEAD CONSULTANT" on the home page | Not in the main page; place it under Robert Bwire at the bottom | The leadership block moved from mid-page (section 5 of 9) to the foot of the home page, after the FAQ and before the closing CTA. The "Lead Consultant" line in the portrait caption was removed, so it now appears exactly once, directly under his name. It remains in the photo `alt` text, which is not visible and is correct for screen readers. Section backgrounds rebalanced so the alternation still reads. |
| "About Robert Bwire" | Rename to "OUR TEAM" | Footer link renamed on all 12 pages. Section eyebrow on the home page is now "Our team"; the About page breadcrumb reads "Our Team". The header nav item is still "About" — a generic label pointing at the same page. Change it if the client prefers. |
| Weekly publishing | A place to post weekly updates | New `/updates/` page ("Weekly Brief"). One file, one paste per week, with the template and instructions inline. Linked from the header nav, footer, home page and `/insights/`. Procedure in `WEEKLY-UPDATES.md`. |

### Process note

The local working copy used for this round was 16 commits behind `origin/main`.
The portrait, the sector photographs, the removal of all downloadable PDFs and a
full pass of copy polish existed only on the remote. The work was redone on top of
`origin/main` rather than merged. **Pull before editing.**


## Priority 3 — strengthens the site

| # | Item | Current state | What is needed |
|---|---|---|---|
| 17 | **Case studies** | None | Two or three engagements described at outcome level, with client permission. |
| 18 | **Testimonials** | None | Attributed quotes with permission to publish. |
| 19 | **Capability statement PDF** | A two-page production edition is linked from the homepage and contact page | Update it whenever public contact details or the selected-experience record changes. |
| 20 | **Additional articles** | One seed article published; six proposed topics clearly labelled as unwritten | The editorial engine only earns its keep once there are four or five pieces. See `PUBLISHING-GUIDE.md`. |
| 21 | **Speaking history** | Not shown | Past conferences, panels and moderation, for `/expertise/rapporteur/`. |
| 22 | **Sector depth** | Six sectors described generically | If the firm has genuine depth in two or three, say which and give each a dedicated page. |

---

## What was deliberately NOT done

Recorded so the client can see where the line was drawn:

- No degrees, awards, employers, dates, client results, revenue figures or headcounts were invented.
- No claim of authorship or contribution to any of the three EAC publications.
- No AI-generated or stock portrait was used to represent Robert Bwire.
- The incomplete telephone number was not published, guessed or "corrected".
- The LinkedIn link was omitted rather than pointed at a generic feed.
- No statistic from the historical publications is presented as current; the only figures
  quoted anywhere on the site are in the seed article and are explicitly attributed to the
  2013 guidebook and dated.
- No advertising rates were invented.
- Six proposed article topics are listed as proposed, visually distinct from published work.
