# Founder Skills

A simple skills library for **solo founders** — building, growing, SEO, and customers. Fewer, sharper skills that I actually use in my own projects, added to as I go.

**Install:** [INSTALLATION.md](./INSTALLATION.md) — claude.ai via ZIP upload, Claude Code / Cursor via `git clone`.
Repo: [founder-skills](https://github.com/shreyvijayvargiya/founder-skills)

## How it works

One entry skill, [`SKILL.md`](./SKILL.md) (**Founder OS**), reads your request, picks the minimum skills needed, runs them, and returns one clear answer. Each skill is a single markdown file: `capabilities/<category>/<skill>/AGENT.md`.

```
capabilities/
├── build/       validate · scope · position · price
├── grow/        launch · directories · outreach · weekly report
├── seo/         audits · content · links · AI-search visibility
└── customers/   leads · voice · interviews · feedback · onboarding · churn
```

Ask in plain language: *"Should I build this?"*, *"Audit my SEO"*, *"Why are people cancelling?"*

## Skills

Rendered from each skill's frontmatter by `python3 scripts/sync-registry.py` — do not edit by hand.

<!-- skills:start -->
### Build (7)

Validate the idea, scope the MVP, position and price it.

| Skill | What it does |
|-------|--------------|
| [`ai-agent-opportunity`](capabilities/build/ai-agent-opportunity/AGENT.md) | Find AI agent and automation opportunities from workflows, bottlenecks, and pain points. Use when exploring agent products. |
| [`competitor-intelligence`](capabilities/build/competitor-intelligence/AGENT.md) | Research competitors: positioning, sentiment, strengths, weaknesses, and strategic moves. Use for competitive strategy. |
| [`market-intelligence`](capabilities/build/market-intelligence/AGENT.md) | Analyze a market or category: competitors, demand, trends, risks, and opportunities. Use for market entry or positioning decisions. |
| [`micro-saas-builder`](capabilities/build/micro-saas-builder/AGENT.md) | Scope a micro-SaaS MVP: ICP, features, pricing, distribution, and launch plan. Use when validating a small product idea. |
| [`positioning-and-landing-copy`](capabilities/build/positioning-and-landing-copy/AGENT.md) | Turn discovery and voice-mining output into value prop, hero, sections, and CTA for a landing page. Use when the plan needs an actual page founders can ship. |
| [`pricing-intelligence`](capabilities/build/pricing-intelligence/AGENT.md) | Research SaaS pricing, packaging, plans, and competitor pricing. Use to find pricing and packaging opportunities. |
| [`saas-discovery`](capabilities/build/saas-discovery/AGENT.md) | Research a SaaS URL: product, ICP, competitors, and positioning. Use before SEO, content, competitor, or growth research. |

### Grow (5)

Launch and market: channels, directories, outreach, weekly growth.

| Skill | What it does |
|-------|--------------|
| [`cold-outreach-writer`](capabilities/grow/cold-outreach-writer/AGENT.md) | Turn lead-research-intelligence output into a short cold email or DM sequence for the ICP. Use when you know where leads are but need messages to send. |
| [`directory-launch`](capabilities/grow/directory-launch/AGENT.md) | Find quality SaaS directories and create a submission strategy with reusable listing copy. Use for directory launch. |
| [`launch-post-writer`](capabilities/grow/launch-post-writer/AGENT.md) | Write platform-specific launch drafts for Show HN, Product Hunt, r/SaaS, r/microsaas, X, and LinkedIn. Use after saas-launch when founders need actual posts. |
| [`saas-launch`](capabilities/grow/saas-launch/AGENT.md) | Build a SaaS launch plan: Product Hunt, channels, assets, and timeline. Use when planning a product launch. |
| [`weekly-growth-report`](capabilities/grow/weekly-growth-report/AGENT.md) | Summarize weekly traffic signals, top pages, new content gaps, and one recommended next action. Use as a recurring founder OS check-in on a live SaaS site. |

### SEO (14)

Audit and grow search + AI-search visibility.

| Skill | What it does |
|-------|--------------|
| [`competitor-seo-page`](capabilities/seo/competitor-seo-page/AGENT.md) | Plan SEO pages around a competitor: alternatives, comparisons, switching, and migration. Use when targeting a rival in search. |
| [`content-decay-recovery`](capabilities/seo/content-decay-recovery/AGENT.md) | Identify declining content, diagnose ranking and traffic decay, and create recovery plans through updates, consolidation, and optimization. |
| [`content-gap`](capabilities/seo/content-gap/AGENT.md) | Find content topics and formats competitors cover that your site is missing. Use after discovery or with a URL and competitor list. |
| [`content-refresh-and-repurpose`](capabilities/seo/content-refresh-and-repurpose/AGENT.md) | Identify decaying posts to update and repurpose each blog into an X thread, LinkedIn post, and newsletter blurb. Use for refresh plus distribution from existing content. |
| [`geo-aeo-audit`](capabilities/seo/geo-aeo-audit/AGENT.md) | Audit AI search visibility for a SaaS in ChatGPT, Claude, Gemini, and Perplexity. Use for GEO/AEO and answer-engine readiness. |
| [`internal-link-optimizer`](capabilities/seo/internal-link-optimizer/AGENT.md) | Improve SaaS internal linking, fix orphan pages, and connect SEO pages. Use for site structure and link optimization. |
| [`launch-foundation-audit`](capabilities/seo/launch-foundation-audit/AGENT.md) | Audit post-launch website readiness — Search Console, indexing, sitemap, analytics, Google Business Profile, technical SEO, and business listings. Use when a site is live and needs foundational setup. |
| [`query-fan-out-optimizer`](capabilities/seo/query-fan-out-optimizer/AGENT.md) | Expand a target topic into related queries, search intents, follow-up questions, entities, and answer opportunities for SEO, GEO, and AEO. |
| [`saas-seo-discovery`](capabilities/seo/saas-seo-discovery/AGENT.md) | Baseline SEO audit before launch — site inventory, quick wins, and page gaps from your product URL. Use pre-launch or early site. |
| [`seo-authority-architect`](capabilities/seo/seo-authority-architect/AGENT.md) | Design SEO site architecture, authority flow, internal linking, reverse silos, and entity relationships. Use to strengthen topical authority and important pages. |
| [`seo-content-planner`](capabilities/seo/seo-content-planner/AGENT.md) | Turn SEO research into clusters, briefs, internal links, and a publishing roadmap. Use after SEO opportunity research. |
| [`seo-opportunity`](capabilities/seo/seo-opportunity/AGENT.md) | Find and prioritize SaaS SEO pages, keywords, gaps, and commercial opportunities. Use for SEO strategy and page planning. |
| [`seo-page-generator`](capabilities/seo/seo-page-generator/AGENT.md) | Write a high-quality SaaS SEO page from a brief or topic. Use when ready to create title, meta, article, FAQ, and CTA. |
| [`technical-seo-audit`](capabilities/seo/technical-seo-audit/AGENT.md) | Audit technical SEO issues — 404s, redirects, error pages, sitemap, canonicals, and broken URLs. Use for recurring site health checks on live SaaS sites. |

### Customers (6)

Find them, listen to them, onboard them, keep them.

| Skill | What it does |
|-------|--------------|
| [`churn-recovery`](capabilities/customers/churn-recovery/AGENT.md) | Diagnose why customers cancel or go inactive, and create win-back, save-offer, and prevention plays. Use when churn or cancellations are hurting MRR. |
| [`customer-interview-guide`](capabilities/customers/customer-interview-guide/AGENT.md) | Build a short customer interview script and recruiting message, then synthesize notes into insights. Use before building, repositioning, or when you need real customer conversations. |
| [`customer-voice-mining`](capabilities/customers/customer-voice-mining/AGENT.md) | Mine real pain points and exact customer wording from Reddit, HN, G2, and X reviews, then cluster themes. Use to validate demand and feed copy skills. |
| [`feedback-triage`](capabilities/customers/feedback-triage/AGENT.md) | Turn raw customer feedback (emails, support chats, reviews, DMs) into ranked themes, bug vs feature requests, and a small what-to-build-next list. Use when feedback is piling up. |
| [`lead-research-intelligence`](capabilities/customers/lead-research-intelligence/AGENT.md) | Find lead sources, communities, and outreach angles for your ICP. Use to build a customer acquisition pipeline. |
| [`onboarding-activation-audit`](capabilities/customers/onboarding-activation-audit/AGENT.md) | Audit signup-to-first-value flow, define the activation moment, and propose onboarding fixes and welcome emails. Use when signups don't turn into active users. |
<!-- skills:end -->

## Roadmap

Rolling out four categories first, then expanding.

| Status | Category | Focus |
|--------|----------|-------|
| Live | Build · Grow · SEO · Customers | Above |
| Next | **Investors** | Fundraising narrative, investor list + outreach, update emails, data room |
| Next | **Scale** | Hiring, ops and systems, metrics, pricing evolution |

## Add a skill

Short version — full guide in [CONTRIBUTING.md](./CONTRIBUTING.md):

1. Copy [`templates/AGENT.template.md`](./templates/AGENT.template.md) to `capabilities/<category>/<name>/AGENT.md`
2. Fill in the frontmatter and workflow
3. Run `python3 scripts/sync-registry.py`
4. Commit

## Docs

- [docs.md](./docs.md) — architecture and file map
- [framework/](./framework) — planner, router, evaluator, synthesizer
- [LICENSE](./LICENSE) — MIT
