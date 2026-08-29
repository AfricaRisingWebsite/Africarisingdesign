---
name: publish-africa-rising-article
description: Create, edit, or prepare an Africa Rising Investments insight article for publication while preserving the site's editorial voice, evidence rules, metadata, accessibility, and static-site structure. Use when asked to draft or publish an insight, market note, policy analysis, or article for this website.
---

# Publish an Africa Rising Investments article

Use this workflow for every new article or substantial article revision.

## Read first

Before editing, read these project files in full:

- `PUBLISHING-GUIDE.md`
- `insights/eac-guidebooks-what-still-holds/index.html`
- `insights/index.html`
- `sitemap.xml`

Treat the seed article as the markup template, not as a source of facts for a new topic.

## Editorial standard

Write for a decision-maker considering an African market, policy, institution, or investment. Lead with the decision or tension, then supply the evidence needed to act.

- Prefer specific, restrained claims over promotional language.
- Do not use superlatives such as “leading,” “best,” “unmatched,” or “guaranteed.”
- Never present a historical figure as current. State the source and publication year in the same paragraph.
- Never publish a quantitative claim without a dated, traceable source.
- Distinguish confirmed facts, interpretation, and uncertainty.
- Say what the evidence cannot establish.
- Do not imply Africa Rising Investments or Robert Bwire authored, commissioned, or contributed to a source unless that involvement is verified.
- End every article with a Sources section containing direct links to the primary or official sources used.

## Build the article

1. Create a durable lowercase, hyphenated slug. Do not include a date unless it is essential to the subject.
2. Copy the seed article folder to `insights/<slug>/`.
3. Update the title, description, canonical URL, Open Graph URL, Article JSON-LD, dates, hero, breadcrumb, and article body.
4. Keep one `h1`. Use sequential `h2` and `h3` headings without skipping levels.
5. Use a lede that identifies the decision and why it matters. Keep paragraphs focused and avoid generic scene-setting.
6. Calculate reading time as word count divided by 200, rounded to the nearest whole minute with a minimum of one minute.
7. Add the article card to `insights/index.html`, newest first, and remove any matching proposed-topic card.
8. Add the canonical article URL and modification date to `sitemap.xml`.

## Verify before completion

- Read the finished copy aloud in your head and remove robotic transitions, repeated conclusions, empty abstractions, and unnecessary headings.
- Confirm every named institution, date, figure, quotation, and legal or policy statement against a primary source.
- Confirm the canonical URL uses `https://africarisingwebsite.github.io/Africarisingdesign/`.
- Open the article locally and test every link.
- Check desktop and phone layouts for horizontal overflow.
- Confirm the article card, breadcrumb, metadata, structured data, and sitemap entry agree on the title, URL, and date.
- Run the project's audience-facing writing lint when available, then judge each finding in context rather than applying mechanical substitutions.

Do not publish or push unless the user explicitly asks for deployment.
