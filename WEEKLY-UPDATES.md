# How to publish a weekly update

Everything happens in one file: `updates/index.html`, the Weekly Brief page.
No new folders, no sitemap edit, no build step. About three minutes.

---

## In the GitHub web editor

1. Repository → **updates** folder → **index.html**.
2. Click the **pencil icon** (top right of the file).
3. Find the comment block that begins `HOW TO ADD THIS WEEK'S UPDATE`.
   Directly below it is a line reading `<!-- PASTE HERE -->`.
4. Paste the entry below on the blank line under `<!-- PASTE HERE -->`.
5. **Commit changes** → short message (`Weekly brief – 20 September`) → **Commit changes**.

Live in one to two minutes. Check the **Actions** tab for the green tick, then
hard-refresh the page (Shift + refresh).

## The entry

```html
<article class="brief__entry reveal">
  <p class="brief__date">20 September 2026<span class="brief__tag">Policy</span></p>
  <h3>Headline for this update</h3>
  <p>What happened, stated plainly, with the source named.</p>
  <p>Why it matters for someone weighing an investment decision.</p>
</article>
```

A copy of this block already sits inside the instruction comment in the file,
so it can be copied from there rather than from this document.

| Change | To | Leave alone |
|---|---|---|
| `20 September 2026` | The date of the update | `<p class="brief__date">` |
| `Policy` | One word — Policy, Trade, Energy, Infrastructure, Regional | `<span class="brief__tag">` |
| `Headline for this update` | The headline, one line | `<h3>` `</h3>` |
| The two `<p>` lines | What happened, then why it matters | `<p>` `</p>` |

Newest entry always goes directly under `<!-- PASTE HERE -->`, above last week's.
Older entries stay put; nothing needs deleting.

**After the first real entry**, delete the grey placeholder — the block running
from `<div class="brief__empty">` to its matching `</div>`.

## Optional: drop a category tag

The tag chip is optional. Remove `<span class="brief__tag">Policy</span>` and the
date stands alone.

---

## House rules

Same rules as `PUBLISHING-GUIDE.md`, because a weekly note carries the firm's name
exactly as an article does.

1. **Never publish a figure without a dated source.** If you cannot attribute it, cut it.
2. **Never quote a statistic from the historical publications as if it were current.**
3. **No superlatives.** No "leading", "best", "unmatched", "guaranteed".
4. **Two paragraphs is usually enough.** Longer treatments belong under `/insights/`.
5. **Say what you don't know.** Naming the limits of a reading raises trust.

## When it stops being a weekly note

If a piece needs sections, a table or sources, it is an article, not a brief.
Follow `PUBLISHING-GUIDE.md` instead and link to it from a short brief entry.

---

## Undoing a mistake

Nothing is lost. Repository → **Commits** → click the bad commit → **…** menu →
**Revert**. A new commit restores the previous state and the site rebuilds.

If a page looks broken, revert first and investigate afterwards.
