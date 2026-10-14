---
name: technical-seo-audit
description: Audit technical SEO issues — 404s, redirects, error pages, sitemap, canonicals, and broken URLs. Use for recurring site health checks on live SaaS sites.
---

# Technical SEO Audit

## Mission

Find **crawl and index problems** that block or waste organic traffic — a repeatable health check for live SaaS sites.

Use when the user asks:

- Technical SEO audit
- Fix 404s and redirects
- Sitemap or canonical issues
- Broken links on my marketing site
- Monthly SEO health check

This is not content strategy or keyword research — pair with **seo-opportunity** or **content-gap** for growth ideas.

---

# Input

## Required

- Website URL (marketing site root)

## Optional

- Sitemap URL
- Search Console export or screenshots (user-provided only)
- Staging vs production note
- CMS (Webflow, WordPress, Next.js, etc.)
- Recent migration or redesign date
- Priority sections (blog, docs, pricing)

If URL is missing, ask once.

---

# Workflow

## 1. Crawl Surface Discovery

Research and inspect when available:

- robots.txt
- XML sitemap(s)
- homepage and main nav paths
- common templates (blog, docs, landing pages)
- status of key URLs (home, pricing, signup, top blog posts if known)

Use public signals and fetches — do not invent crawl data.

If live crawl tools are unavailable, use spot checks and clearly label limits.

---

## 2. Issue Categories

### HTTP and errors

- 404 Not Found (broken internal links, old campaigns)
- 5xx server errors
- Soft 404s (thin/error pages returning 200)

### Redirects

- Redirect chains (A → B → C)
- Redirect loops
- HTTP → HTTPS
- www vs non-www consistency
- Trailing slash inconsistencies

### Indexation signals

- robots.txt blocks on important paths
- noindex on money pages by mistake
- missing or duplicate sitemap entries

### Canonicals

- Missing canonical tags
- Conflicting canonicals
- Parameterized URLs without clear canonical

### Internal links

- Broken internal links (sample high-traffic paths)
- Orphan important pages (if inferable from sitemap/nav)

### Core templates

- Title/meta missing on key templates (brief note — full on-page is optional)

---

## 3. Prioritize Fixes

Score each issue:

- Severity (critical / high / medium / low)
- Scope (one URL vs site-wide)
- Effort (dev hours rough bucket: S / M / L)
- SEO impact (indexation, link equity, crawl waste)

Quick wins first: broken redirects on top pages, sitemap 404s, canonical mistakes on blog.

---

## 4. Recurring Schedule

Recommend a simple cadence:

- Weekly: monitor 404 spikes (if GSC available)
- Monthly: full sitemap + redirect spot check
- After deploy: smoke test top 20 URLs

Frame as **schedulable** — same audit shape each run for diff-over-time.

---

# Output

## Audit Summary

- Site:
- Audit date:
- Data limits (what you could not verify):

## Findings

| Issue | URL or pattern | Severity | Evidence | Recommended fix | Effort |
|-------|----------------|----------|----------|-----------------|--------|

## Redirect Map Notes

(Chains to flatten, if found)

## Sitemap Notes

(Missing, stale, or invalid entries)

## Canonical Notes

## Quick Wins (this week)

## Dev Handoff

(Bullet list a developer can ticket — no code unless user asked)

## Recommended Next Step

(Re-run after fixes; or internal-link-optimizer / launch-foundation-audit if indexation blocked)

---

# Quality Rules

- Do not invent Search Console metrics or crawl counts.
- Separate confirmed issues from hypotheses.
- Do not claim full site crawl if only partial checks were done.
- SaaS marketing sites only — not app authentication flows behind login unless user specifies public docs.
- No backlinks, PR, or programmatic SEO in this skill.
