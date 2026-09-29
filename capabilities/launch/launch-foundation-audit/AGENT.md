---
name: launch-foundation-audit
description: Audit post-launch website readiness — Search Console, indexing, sitemap, analytics, Google Business Profile, technical SEO, and business listings. Use when a site is live and needs foundational setup.
---

# Launch Foundation Audit

## Mission

Audit the foundational setup required after launching a website.

Most founders publish a website but never properly configure indexing, analytics, Search Console, business listings, or technical SEO foundations.

The goal is to identify missing setup, explain why it matters, and provide a prioritized action plan.

---

# Use When

The user asks:

* Is my website launch ready?
* What should I do after launching?
* Why isn't Google indexing my pages?
* What SEO setup am I missing?
* How do I configure Search Console?
* What launch checklist should I follow?

---

# Input

## Required

* Website URL

## Optional

* Business type
* Country
* Local business address
* Existing Google accounts/tools

---

# Workflow

## 1. Website Discovery

Review:

* Website structure
* Important pages
* Blog/docs/resources
* Navigation
* Crawlability

Identify missing launch pages.

---

## 2. Search Console

Check and explain:

* Property setup
* Verification
* Sitemap submission
* URL inspection
* Coverage issues
* Performance reporting

Determine:

* What is configured
* What is missing
* What should be monitored

---

## 3. Sitemap & Indexing

Review:

* Sitemap.xml
* Robots.txt
* Indexed pages
* Missing pages
* Crawl blockers

Identify indexing risks and priority pages.

---

## 4. Technical SEO Foundations

Review:

* Titles
* Meta descriptions
* Canonicals
* Structured data
* Open Graph
* Mobile readiness
* HTTPS
* Core Web Vitals
* Internal linking

Highlight critical launch issues.

### Reference — Technical SEO Checklist

Use when auditing. Separate verified findings from assumptions.

| Task | How to check | Fix |
|------|--------------|-----|
| HTTPS | URL bar, redirect from HTTP | Install SSL certificate |
| Mobile-friendly | Google Mobile-Friendly Test | Responsive design |
| Site speed | PageSpeed Insights, GTmetrix | Compress images, caching, CDN |
| Indexability | Search Console > Pages / Coverage | Fix robots.txt, remove accidental noindex |
| XML sitemap | `[site]/sitemap.xml` | Generate, submit in GSC |
| Robots.txt | `[site]/robots.txt` | Allow crawling of important pages |
| Canonical tags | Page source | Add canonicals to prevent duplicates |
| Structured data | Rich Results Test / Schema validator | Add relevant schema markup |

### Core Web Vitals

| Metric | Measures | Target |
|--------|----------|--------|
| LCP (Largest Contentful Paint) | Loading | Under 2.5 seconds |
| INP (Interaction to Next Paint) | Interactivity | Under 200 ms |
| CLS (Cumulative Layout Shift) | Visual stability | Under 0.1 |

Quick wins: compress images and lazy-load for LCP; minimize/defer JS for INP; set image dimensions and avoid layout shifts above the fold for CLS.

### Essential Verification Tools

| Tool | Purpose | Cost |
|------|---------|------|
| Google Search Console | Index status, rankings, clicks | Free |
| Google Analytics 4 | Traffic, behavior, conversions | Free |
| PageSpeed Insights | Performance, Core Web Vitals | Free |
| Screaming Frog | Technical crawl (500 URLs free) | Free tier |

Do not invent metrics from these tools if access is unavailable.

---

## 5. Analytics & Tracking

Review:

### Google Analytics

* Installation
* Events
* Conversions

### Google Tag Manager

* Setup
* Tracking readiness

Recommend key events and goals.

---

## 6. Google Business Profile

When relevant:

Review:

* Eligibility
* Categories
* Website linkage
* Contact details
* Services
* Reviews
* Images

Recommend improvements and local SEO actions.

---

## 7. Business Listings & Citations

Identify relevant:

* Directories
* Business listings
* Local citations
* Industry listings

Prioritize high-value submissions.

---

## 8. Learning Resources

Provide:

* Official Google documentation
* Relevant setup guides
* Beginner-friendly YouTube tutorials
* Useful SEO references

Include direct links whenever possible.

---

# Output

## Executive Summary

## Launch Readiness Score

Score: X/100

---

## Search Console Status

## Sitemap & Indexing Status

## Technical SEO Status

## Analytics Status

## SEO Metrics Baseline

When GSC/GA4 are accessible or the founder supplies data:

| Metric | Current (if known) | Target / monitor |
|--------|-------------------|------------------|
| Indexed pages | | All important pages indexed |
| Organic clicks (28d) | | Establish baseline, grow MoM |
| Average position (target keywords) | | Improve over 90 days |
| Core Web Vitals | | LCP, INP, CLS in "good" range |

If no data yet, list what to track once setup is complete.

## Business Profile Status

## Business Listing Opportunities

---

## Critical Actions

Highest-priority items that should be completed immediately.

---

## 7-Day Action Plan

Actions to complete during the first week.

---

## 30-Day Action Plan

Actions to complete during the first month.

---

## Resources

### Official Documentation

### Tutorials

### YouTube Videos

### Recommended Reading

---

## Final Checklist

A complete launch checklist with completed, missing, and recommended actions.

---

# Quality Rules

* Do not assume access to Search Console, Analytics, or Business Profile.
* Do not invent indexing, traffic, or performance data.
* Clearly separate verified findings from assumptions.
* Prioritize actions by impact.
* Prefer official Google resources whenever possible.
* Keep recommendations practical and beginner-friendly.
* Focus on execution, not SEO theory.

### Technical Mistakes to Flag

When found, call these out explicitly:

1. Blocking important pages in robots.txt or noindex
2. Missing or broken sitemap not submitted to GSC
3. HTTP without HTTPS redirect
4. Slow mobile experience or failing Core Web Vitals
5. Duplicate URLs without canonicals
6. Analytics or GSC not installed — cannot measure improvement
7. Targeting launch without indexation checks on key pages
