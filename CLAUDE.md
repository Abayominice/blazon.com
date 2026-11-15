# blazonshots.com — repo guide and blog publishing procedure

This repo is the live static site for https://blazonshots.com (Blazonshots LTD,
Lagos). Netlify deploys the `site/` folder from the `master` branch
(`netlify.toml`). Every push to `master` goes live within a minute or two, so
never push anything broken.

```
site/                 the public website (only this folder is deployed)
  blog/               one HTML file per article
  blog.html           blog index (newest card first)
  sitemap.xml, llms.txt, robots.txt, ads.txt
templates/post.html   article page template
scripts/publish_post.py   validates a draft and publishes it into site/
content/topic-backlog.md  two queues: S (students) and R (payroll, HR and Rosta)
content/rosta-reference.md  the only source of truth for Rosta features and prices
content/drafts/       drafts waiting to publish (normally empty)
content/published/    source drafts of published posts (record only)
```

## AdSense rules (do not change without the owner asking)

- The AdSense loader script (client `ca-pub-4696041272755947`) is in `<head>`
  of content pages only: home, about, services, apps (Products), rosta, team,
  blog index and every article. The template already includes it.
- It is deliberately NOT on contact, privacy, terms, cookie-policy,
  editorial-policy or the Google verification file. Do not add it there.
- No manual `<ins class="adsbygoogle">` ad units anywhere until the owner says
  the site is approved. After approval, Auto ads are switched on in the
  AdSense dashboard, not in code.
- Never touch `ads.txt`, `google450b24c64d1de8f5.html`, the privacy policy's
  AdSense section, or the cookie policy.

## Each publishing run (the scheduled task runs exactly this)

Every run publishes **two articles** and refreshes **one older article**:

- **Article A:** the first `- [ ]` topic in Queue S (students) of
  `content/topic-backlog.md`.
- **Article B:** the first `- [ ]` topic in Queue R (payroll, HR and Rosta).
- **Refresh:** one older post (see "Refreshing an older article" below).

Write, validate and publish Article A completely (steps 1–6), then Article B,
then the refresh, then commit and push once (step 7). If one article is
blocked, still publish the other.

## Publishing one article

1. **Pick the topic.** Take the first `- [ ]` line in the right queue. If a
   queue is empty, add 10 new topics to it that follow the backlog's "Rules
   for topic choice", then take the first. Check `site/blog/` so you never
   duplicate or near-duplicate an existing post.

2. **Research before writing.** Run several web searches for the target
   keyword. Look at what currently ranks and note what those pages miss.
   Verify every fact that could be wrong or out of date (grading scales,
   official rules, prices, deadlines, programme names) against an official or
   primary source such as NUC, JAMB, NYSC, ITF, a university's own site, or
   the product's own site. If a fact can't be verified, leave it out or state
   it as general guidance ("check your faculty handbook") — never guess.

3. **Write the draft** to `content/drafts/<slug>.html` in this format:

   ```html
   <!--meta
   {
     "slug": "lowercase-hyphenated-keyword-slug",
     "title": "Title Under 65 Characters, Keyword Near the Start",
     "description": "110-165 character meta description that promises a specific answer.",
     "category": "one of the allowed categories below",
     "card_summary": "One or two sentences for the blog index card.",
     "related": ["existing-slug", "existing-slug"]
   }
   -->
   <p class="lead">Opening paragraph that answers the searcher's question directly.</p>
   <h2>...</h2>
   <p>...</p>
   ```

   Allowed categories: Student Life, Study Skills, Student Money,
   Careers & Skills, Student Tech, App Development, Growth,
   Digital Trust & Safety, Payroll & HR, Rosta Guides.
   Use "Rosta Guides" for how-to-do-X-in-Rosta articles and "Payroll & HR"
   for general employer education.

   **Extra rules for Queue R (payroll, HR and Rosta):**
   - Everything said about Rosta must come from `content/rosta-reference.md`.
     Use the screen and section names exactly as written there. If a step is
     not described there, explain it in general terms or leave it out. Never
     invent features, screens, integrations, prices, customers, testimonials
     or results. Rosta mobile apps are not in app stores yet.
   - Quote prices only with "at the time of writing" and a link to
     https://blazonshotsltd.com/pricing.
   - Verify every tax band, rate, relief, contribution percentage, deadline
     and agency name against official sources (Nigeria Revenue Service, the
     relevant State Internal Revenue Service, PenCom, NSITF, ITF, FMBN, and
     the Nigeria Tax Act / Nigeria Tax Administration Act texts or their
     official summaries). The federal tax authority is the Nigeria Revenue
     Service (formerly FIRS) since 1 January 2026. For other countries use
     that country's official revenue authority and social security bodies
     (e.g. GRA and SSNIT in Ghana, KRA, NSSF and SHA in Kenya, SARS in South
     Africa, URA in Uganda, RRA and RSSB in Rwanda). If sources disagree or a
     figure cannot be confirmed, say so and tell readers to confirm with an
     accountant or the agency — never guess.
   - Rosta serves businesses across Africa (48 countries), not only Nigeria.
     Describe non-Nigerian rule support exactly as `content/rosta-reference.md`
     does: researched starting rules each company can adjust, not reviewed by
     a local accountant. Only Nigeria's PAYE is accountant signed off.
   - End every payroll or tax article with this sentence in its own
     paragraph: `<p><em>This article explains how the rules generally work
     and is not tax, legal or financial advice. Confirm your situation with a
     qualified accountant or the relevant agency.</em></p>`
   - General "Payroll & HR" articles must be useful to an employer who never
     uses Rosta. Mention Rosta at most twice, in a short section near the
     end, linking `../rosta.html`.
   - "Rosta Guides" articles are step-by-step and honest about plan limits
     (say which plan includes the module). Link `../rosta.html` and
     `https://blazonshotsltd.com/signup` once each.
   - Link Queue R articles to each other and, where it fits, to student
     articles (for example a payslip or SIWES article), and vice versa.

   **Editorial standard — this is what gets the site approved and ranked:**
   - 1,500–2,500 words of real substance. The script rejects under 1,200.
   - Answer the searcher's question in the first 2–3 sentences, then go deeper.
   - At least 5 `<h2>` sections with descriptive, question-style or
     keyword-bearing headings; use `<h3>`, `<ul>/<ol>` and `<table>` where they
     genuinely help (worked examples, comparisons, step lists).
   - Concrete and specific: worked examples with real numbers, step-by-step
     instructions, checklists, Nigerian/African context (naira, NEPA/power cuts,
     data costs, hostel life, SIWES, NYSC) where it is relevant.
   - Include a short "Frequently asked questions" `<h2>` near the end with 3–5
     `<h3>` questions people really search, each answered in 2–4 sentences.
   - At least 2 contextual internal links in the body to existing posts
     (`<a href="other-slug.html">`) or site pages (`<a href="../apps.html">`).
     Link to official sources externally with
     `<a href="https://..." rel="noopener" target="_blank">`.
   - British English spelling (realise, organisation), matching existing posts.
   - Honest, plain, helpful tone. No hype, no clickbait, no filler intros
     ("In today's fast-paced world..."), no "In conclusion" padding.
   - NEVER invent statistics, studies, quotes, testimonials, named students,
     or personal anecdotes presented as real. Hypothetical examples must read
     as hypothetical ("Say a student has...").
   - No medical, legal or investment advice; no gambling, crypto-trading
     tips, exam leaks, "guaranteed admission" or anything AdSense prohibits.
   - No images, scripts, iframes, inline styles or ad units in the body.
   - Mention Blazonshots products only where genuinely useful (for example,
     BlazonCalc on a CGPA post links to `../apps.html`), at most once.

4. **Validate, then publish:**
   ```
   python3 scripts/publish_post.py content/drafts/<slug>.html --check-only
   python3 scripts/publish_post.py content/drafts/<slug>.html
   ```
   Fix every ERROR and re-run. Treat WARNINGs seriously (shorten the title).
   The script renders the page, adds the card to the top of `site/blog.html`,
   refreshes the homepage's latest articles, adds the sitemap entry,
   refreshes `site/llms.txt` and moves the draft to `content/published/`.

5. **Proofread the rendered page** `site/blog/<slug>.html` once: headings make
   sense in order, links work, no leftover markup, facts match your sources.

6. **Tick the topic** in `content/topic-backlog.md`:
   `- [x] Title — kw: ... — published YYYY-MM-DD`.

7. **Commit and push to master** (once, after both articles and the refresh):
   ```
   git add -A
   git commit -m "Publish: <title A> + <title B>; refresh <slug>"
   git push origin master
   ```
   If the push is rejected, `git pull --rebase origin master` and push again.
   Never force-push.

## Refreshing an older article

Pick the published post in `site/blog/` with the fewest body words (text
between `<p class="lead">` and `<h2>Related articles</h2>`) that is under
1,400 words and was not refreshed in the last 30 days (check its
`dateModified`). Make it genuinely better, not just longer:
- Add 2–3 new `<h2>` sections with concrete, Nigeria-relevant detail and a
  "Frequently asked questions" section (3–4 `<h3>` questions) before
  `<h2>Related articles</h2>`, if it has none.
- Turn any "our piece on ..." mention into a real link to that post.
- Fix anything outdated. Keep the existing slug, title and structure.
- Set `"dateModified"` in its JSON-LD and its `<lastmod>` in
  `site/sitemap.xml` to today.
The same editorial rules apply. Do not touch posts already over 1,400 words.

## When something blocks you

Never more than two new articles per run. If anything blocks you (research shows the topic is
unsafe or unanswerable, the script keeps failing, push fails), skip the topic
with a note in the backlog (`- [~] ... — skipped: reason`), and do not push a
half-finished post.
