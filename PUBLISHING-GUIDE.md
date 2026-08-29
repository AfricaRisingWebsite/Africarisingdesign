# How to publish a new article

No build tools, no CMS, no developer. Copy one file, change six things, add one card.
About fifteen minutes.

---

## Step 1 — copy the template

```bash
cp -r insights/eac-guidebooks-what-still-holds insights/your-new-article-slug
```

Slug rules: lowercase, hyphens, no dates, no stop-words you don't need. The slug becomes
the URL and cannot be changed later without breaking links, so choose it deliberately.

## Step 2 — open the new `index.html` and change six things

1. **`<title>`** — the article headline, then ` | Africa Rising Investments`. Under ~60 characters before the pipe if you can.
2. **`<meta name="description">`** — one sentence, 140–160 characters, describing what the reader gets.
3. **`<link rel="canonical">` and `og:url`** — change the slug to match the folder name.
4. **The JSON-LD `Article` block** — update `headline`, `description`, `datePublished`, `dateModified` and `mainEntityOfPage`.
5. **The page hero** — the eyebrow (category), the `<h1>`, the published date and the reading time.
6. **The breadcrumb** — the last item's label.

## Step 3 — write the body

Replace everything inside `<div class="prose"> … </div>`.

The only tags you need:

```html
<p class="lede">The opening paragraph. One sentence of setup, one of stake.</p>
<p>Ordinary paragraph.</p>
<h2>Section heading</h2>
<h3>Sub-heading, only if the section really needs one</h3>
<ul><li>Bullet</li></ul>
<ol><li>Numbered point</li></ol>
<p><strong>Bold lead-in.</strong> Body text follows.</p>
<blockquote class="pullquote">A sentence worth isolating.</blockquote>
<hr class="rule">
<a href="../../library/">Internal link</a>
```

Keep heading order sequential: `h1` then `h2` then `h3`. Never skip a level — it breaks
screen-reader navigation and the accessibility audit.

Always end with a **Sources** section. It is the firm's main credibility signal.

## Step 4 — add the card to the index

Open `insights/index.html` and paste this into the "Published" grid, newest first:

```html
<article class="post reveal">
  <p class="post__kicker">Category</p>
  <h3><a href="your-new-article-slug/">The headline</a></h3>
  <p>One or two sentences on what the reader gets.</p>
  <p class="post__meta">1 January 2027 &middot; 7 minute read</p>
</article>
```

If the article was a proposed topic, delete its `post--proposed` card from the
"Proposed topics" grid at the same time.

## Step 5 — add it to the sitemap

In `sitemap.xml`, copy an existing `<url>` block and update `<loc>` and `<lastmod>`.

## Step 6 — check before you push

- [ ] Open the page locally (`python3 -m http.server 8080`) and read it end to end.
- [ ] Click every link in the article.
- [ ] Resize the browser to phone width — nothing should scroll sideways.
- [ ] Confirm the card on `/insights/` links to the right place.
- [ ] Check the reading time is honest: roughly word count ÷ 200, rounded.

---

## House rules for the writing

These are what keep the site credible. They matter more than the mechanics above.

1. **Never publish a figure without a dated source.** If you cannot attribute it, cut it.
2. **Never quote a statistic from the historical publications as if it were current.**
   Attribute and date it, as the seed article does.
3. **No superlatives.** No "leading", "best", "unmatched", "guaranteed". Every claim on
   this site has to be defensible on its face.
4. **Write for one reader with one decision.** General commentary is what everyone else
   publishes; specificity is the product.
5. **Analysis, not promotion.** An article that only argues you should hire the firm is
   worth less than one that teaches something and lets the reader draw the conclusion.
6. **Say what you don't know.** Naming the limits of an analysis raises trust; pretending
   there are none lowers it.
