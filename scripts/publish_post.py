#!/usr/bin/env python3
"""Publish one blog post to the Blazonshots static site.

Usage:
    python3 scripts/publish_post.py content/drafts/<slug>.html [--date YYYY-MM-DD] [--check-only]

A draft is an HTML fragment (the article body only: lead paragraph, h2/h3
sections, lists, tables) that starts with a metadata comment:

    <!--meta
    {
      "slug": "how-to-calculate-cgpa-nigerian-universities",
      "title": "How to Calculate Your CGPA in Nigerian Universities",
      "description": "120-160 character meta description.",
      "category": "Student Life",
      "card_summary": "One or two sentences shown on the blog index card.",
      "related": ["existing-slug-1", "existing-slug-2"]
    }
    -->

The script validates the draft, renders site/blog/<slug>.html from
templates/post.html, adds the card to the top of site/blog.html, adds the
URL to site/sitemap.xml, rebuilds the blog list in site/llms.txt, and moves
the draft to content/published/. It exits non-zero on any validation error
without touching the site.
"""
import argparse
import datetime as dt
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
BLOG = SITE / "blog"
TEMPLATE = ROOT / "templates" / "post.html"
PUBLISHED = ROOT / "content" / "published"
BASE = "https://blazonshots.com"

MIN_WORDS = 1200
CATEGORIES = {
    "Student Life", "Study Skills", "Student Money", "Careers & Skills",
    "Student Tech", "App Development", "Growth", "Digital Trust & Safety",
    "Payroll & HR", "Rosta Guides",
}


def fail(errors):
    for e in errors:
        print("ERROR:", e)
    sys.exit(1)


def parse_draft(path):
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"\s*<!--meta\s*(\{.*?\})\s*-->\s*(.*)\Z", raw, re.S)
    if not m:
        fail([f"{path}: missing <!--meta {{...}} --> header"])
    try:
        meta = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        fail([f"{path}: metadata is not valid JSON: {e}"])
    return meta, m.group(2).strip()


def existing_slugs():
    return {p.stem for p in BLOG.glob("*.html")}


def validate(meta, body, date):
    errors, warnings = [], []
    for key in ("slug", "title", "description", "category", "card_summary", "related"):
        if not meta.get(key):
            errors.append(f"metadata field '{key}' is missing or empty")
    if errors:
        return errors, warnings
    slug = meta["slug"]
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
        errors.append("slug must be lowercase words joined by hyphens")
    if len(slug) > 75:
        warnings.append("slug is long; keep it under ~75 characters")
    if slug in existing_slugs():
        errors.append(f"a post with slug '{slug}' already exists")
    if len(meta["title"]) > 70:
        warnings.append(f"title is {len(meta['title'])} chars; Google truncates past ~60-65")
    dlen = len(meta["description"])
    if not 110 <= dlen <= 165:
        errors.append(f"description is {dlen} chars; keep it between 110 and 165")
    if meta["category"] not in CATEGORIES:
        errors.append(f"category must be one of: {', '.join(sorted(CATEGORIES))}")
    rel = meta["related"]
    if not isinstance(rel, list) or not 2 <= len(rel) <= 4:
        errors.append("related must list 2-4 existing post slugs")
    else:
        for r in rel:
            if r not in existing_slugs():
                errors.append(f"related slug '{r}' does not exist in site/blog/")

    text = re.sub(r"<[^>]+>", " ", body)
    words = len(re.findall(r"\b[\w'’-]+\b", text))
    if words < MIN_WORDS:
        errors.append(f"body has {words} words; minimum is {MIN_WORDS}")
    if re.search(r"<h1\b", body, re.I):
        errors.append("body must not contain <h1> (the template supplies it)")
    if len(re.findall(r"<h2\b", body, re.I)) < 4:
        errors.append("body needs at least 4 <h2> sections")
    if not re.match(r'<p class="lead">', body):
        errors.append('body must start with <p class="lead">')
    if re.search(r"adsbygoogle|<ins\b|<script\b|<iframe\b|<style\b", body, re.I):
        errors.append("body must not contain ad units, scripts, iframes or style blocks")
    if re.search(r"lorem ipsum|\[insert|TODO|TBD|as an ai\b", body, re.I):
        errors.append("body contains placeholder or AI-boilerplate text")
    if re.search(r"<img\b", body, re.I):
        errors.append("body must not contain images (no image pipeline yet)")
    # Internal links must resolve.
    for href in re.findall(r'href="([^"]+)"', body):
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = (BLOG / href.split("#")[0]).resolve()
        if not target.exists():
            errors.append(f"internal link '{href}' does not resolve")
    internal = [h for h in re.findall(r'href="([^"]+)"', body) if not h.startswith(("http", "mailto:", "#"))]
    if len(internal) < 2:
        errors.append("body needs at least 2 contextual internal links to other posts or pages")
    if date > dt.date.today() + dt.timedelta(days=1):
        errors.append("publish date is in the future")
    return errors, warnings


def esc(s):
    return html.escape(s, quote=True)


def card_title(slug):
    page = (BLOG / f"{slug}.html").read_text(encoding="utf-8")
    m = re.search(r"<h1>(.*?)</h1>", page, re.S)
    return m.group(1).strip() if m else slug


def render(meta, body, date):
    slug = meta["slug"]
    jsonld = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": meta["title"],
        "description": meta["description"],
        "image": f"{BASE}/assets/img/og-default.png",
        "author": {"@type": "Organization", "name": "Blazonshots Editorial Team", "url": f"{BASE}/team.html"},
        "publisher": {"@type": "Organization", "name": "Blazonshots LTD", "url": f"{BASE}/",
                      "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/img/icon-512.png"}},
        "datePublished": date.isoformat(),
        "dateModified": date.isoformat(),
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{BASE}/blog/{slug}.html"},
        "url": f"{BASE}/blog/{slug}.html",
        "articleSection": meta["category"],
        "inLanguage": "en",
    }
    related = "\n".join(
        f'  <li><a href="{r}.html">{card_title(r)}</a></li>' for r in meta["related"]
    )
    out = TEMPLATE.read_text(encoding="utf-8")
    repl = {
        "{{TITLE}}": esc(meta["title"]),
        "{{DESCRIPTION}}": esc(meta["description"]),
        "{{SLUG}}": slug,
        "{{CATEGORY}}": esc(meta["category"]),
        "{{MONTH_YEAR}}": date.strftime("%B %Y"),
        "{{YEAR}}": str(date.year),
        "{{JSONLD}}": json.dumps(jsonld, indent=2, ensure_ascii=False),
        "{{RELATED}}": related,
        "{{BODY}}": body,
    }
    for k, v in repl.items():
        out = out.replace(k, v)
    return out


def update_blog_index(meta):
    path = SITE / "blog.html"
    s = path.read_text(encoding="utf-8")
    marker = '<section><div class="container grid blog-grid">'
    if marker not in s:
        fail(["could not find the blog grid in site/blog.html"])
    card = (
        "\n\n<article class=\"card blog-card\">\n"
        f"  <p class=\"tag\">{esc(meta['category'])}</p>\n"
        f"  <h3><a href=\"blog/{meta['slug']}.html\">{esc(meta['title'])}</a></h3>\n"
        f"  <p>{esc(meta['card_summary'])}</p>\n"
        f"  <a class=\"read-more\" href=\"blog/{meta['slug']}.html\">Read article</a>\n"
        "</article>"
    )
    s = s.replace(marker, marker + card, 1)
    path.write_text(s, encoding="utf-8")


def update_sitemap(slug, date):
    path = SITE / "sitemap.xml"
    s = path.read_text(encoding="utf-8")
    d = date.isoformat()
    entry = f"  <url><loc>{BASE}/blog/{slug}.html</loc><lastmod>{d}</lastmod><changefreq>monthly</changefreq></url>\n"
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    for page in ("", "blog.html"):
        s = re.sub(
            rf"(<loc>{re.escape(BASE)}/{re.escape(page)}</loc><lastmod>)[0-9-]+(</lastmod>)",
            rf"\g<1>{d}\g<2>", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    path.write_text(s, encoding="utf-8")


def update_home(limit=6):
    """Refresh the 'Latest articles' cards on the homepage from blog.html."""
    path = SITE / "index.html"
    s = path.read_text(encoding="utf-8")
    if "<!--LATEST:START-->" not in s:
        return
    blog = (SITE / "blog.html").read_text(encoding="utf-8")
    cards = re.findall(r'<article class="card blog-card">.*?</article>', blog, re.S)[:limit]
    cards = [c.replace("\n", "\n      ") for c in cards]
    block = "<!--LATEST:START-->\n      " + "\n\n      ".join(cards) + "\n<!--LATEST:END-->"
    s = re.sub(r"<!--LATEST:START-->.*?<!--LATEST:END-->", lambda m: block, s, flags=re.S)
    path.write_text(s, encoding="utf-8")


def rebuild_llms():
    path = SITE / "llms.txt"
    s = path.read_text(encoding="utf-8")
    blog = (SITE / "blog.html").read_text(encoding="utf-8")
    items = re.findall(r'<h3><a href="blog/([^"]+)\.html">(.*?)</a></h3>', blog)
    lines = "\n".join(f"- [{html.unescape(t)}]({BASE}/blog/{slug}.html)" for slug, t in items)
    s = re.sub(r"(## Blog\n\n.*?\n\n)(?:- \[.*?\n)+", lambda m: m.group(1) + lines + "\n", s, flags=re.S)
    path.write_text(s, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--date", help="YYYY-MM-DD (default: today, Africa/Lagos)")
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()

    draft = Path(a.draft)
    if not draft.is_absolute():
        draft = (Path.cwd() / draft).resolve()
    meta, body = parse_draft(draft)
    lagos_today = dt.datetime.now(dt.timezone(dt.timedelta(hours=1))).date()
    date = dt.date.fromisoformat(a.date) if a.date else lagos_today

    errors, warnings = validate(meta, body, date)
    for w in warnings:
        print("WARNING:", w)
    if errors:
        fail(errors)
    if a.check_only:
        print("OK: draft passes all checks")
        return

    (BLOG / f"{meta['slug']}.html").write_text(render(meta, body, date), encoding="utf-8")
    update_blog_index(meta)
    update_sitemap(meta["slug"], date)
    rebuild_llms()
    update_home()
    PUBLISHED.mkdir(parents=True, exist_ok=True)
    shutil.move(str(draft), PUBLISHED / draft.name)
    print(f"PUBLISHED: {BASE}/blog/{meta['slug']}.html")


if __name__ == "__main__":
    main()
