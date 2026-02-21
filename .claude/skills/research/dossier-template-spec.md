# Account Dossier — HTML Template Specification

> Design brief for `/frontend-design`. This file constrains structure, brand, and components.
> The `/frontend-design` skill handles visual execution within these constraints.

## Purpose

Self-contained, branded HTML dossier for account research output. One file per company, saved to `/Users/mdmac/Projects/Mycel/memory/companies/`. Opens in any browser with zero dependencies.

## Tab Structure (6 tabs, same every time)

1. **Overview** — Company snapshot: what they do, products/services, target customers, competitive landscape, recent acquisitions
2. **Recent News** — Timestamped news items with "Why it matters" sales context for each item
3. **Key People** — Leadership cards with photo placeholder/initials, title, tenure, LinkedIn URL, talking points
4. **Hiring Signals** — Open roles by department, growth rate indicators, tech stack signals from job postings
5. **Qualification** — Positive signals, caution signals, unknown gaps, with evidence for each. ICP scorecard (1-5 scale)
6. **Approach** — Recommended entry points, opening hooks tied to research findings, discovery questions

## Page Layout

```
HEADER
├── Company name (h1) + subtitle (what they do, 1 line)
├── Metadata row: Industry | Employee Count | HQ Location | Founded Year
├── Left accent bar: 4px solid Amber 600 (#d97706)
└── PE ownership badge (if applicable): "[PE Firm] portfolio company"

KPI ROW (4-column CSS grid)
├── Revenue estimate
├── Employee count
├── Funding / stage
└── ICP Score (1-5, color-coded)

TAB BAR
├── 6 tabs, horizontal
├── Active tab: Amber 600 text + 2px bottom underline + rgba(217,119,6,0.1) background tint
└── Inactive tabs: Stone 600 text, hover → Stone 900

CONTENT AREA
├── Swappable tab panels (only active panel visible)
└── Each panel follows component specs below

FOOTER
├── NotebookLM notebook link (if available)
├── "Powered by Mycel.io" branding
├── Generation date
└── Sources used count
```

## Mycel Light Theme Tokens

Source of truth: `/Users/mdmac/Projects/Mycel/clients/easyvista/portal/css/design-system.css`

These tokens MUST be used exactly as specified. This is a branded template, not a creative freestyle.

### Backgrounds
- `--bg: #fafaf9` (Stone 50 — warm off-white, NOT pure white)
- `--card: #ffffff` (Pure white for cards)
- `--bg-secondary: #f5f5f4` (Stone 100 — muted areas)

### Text
- `--text-primary: #1c1917` (Stone 900)
- `--text-secondary: #57534e` (Stone 600)
- `--text-muted: #78716c` (Stone 500)

### Accents
- `--accent: #d97706` (Amber 600 — primary accent, CTAs, active tab, KPI numbers)
- `--accent-hover: #b45309` (Amber 700)
- `--accent-light: #fffbeb` (Amber 50 — subtle highlight backgrounds)
- `--teal: #4dc0c7` (EasyVista brand pop — section title bars, info boxes, LinkedIn links, timeline dots)
- `--teal-soft: rgba(77, 192, 199, 0.12)` (Teal background tint)

### Borders & Effects
- `--border: #e7e5e4` (Stone 200)
- `--border-strong: #d6d3d1` (Stone 300)
- `--shadow-sm: 0 1px 2px rgba(28,25,23,0.05)`
- `--shadow-md: 0 4px 12px rgba(28,25,23,0.08)`
- `--radius: 8px` (cards)
- `--radius-lg: 12px` (large containers)

### Semantic Colors
- `--success: #22c55e` (positive signals, "Strong Fit")
- `--warning: #f59e0b` (caution signals, "Moderate Fit")
- `--danger: #ef4444` (negative signals, "Weak Fit")
- `--info: #3b82f6` (neutral info items)

### Typography
- Font: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif` (system font stack — brand constraint, overrides frontend-design's font preferences)
- Body: 16px / 1.5 line-height
- Headings: 600-700 weight, Stone 900

## Component Specifications

### Header
- Company name as h1, Stone 900, font-weight 700
- Subtitle: 1-line description, Stone 600
- Metadata row: pills/chips with Industry, Size, HQ, Founded — Stone 100 bg, Stone 600 text, Stone 200 border
- Left accent bar: 4px solid Amber 600, runs full height of header card
- If PE-owned: small badge below metadata — "Portfolio of [PE Firm]" in Amber 50 bg, Amber 700 text

### KPI Cards (4-column grid)
- White background, Stone 200 border, shadow-sm
- Value: large text (1.875rem / 30px), font-weight 700, Amber 600 color
- Label: small text (0.875rem / 14px), Stone 600
- Border-radius: 8px
- On mobile (< 768px): 2x2 grid

### Person Cards (Key People tab)
- Circular avatar placeholder: 48px, Amber 50 background, Amber 600 text (initials, font-weight 600)
- Name: Stone 900, font-weight 600
- Title + tenure: Stone 600
- LinkedIn link: Teal color (#4dc0c7), underline on hover
- Talking points: bulleted list below, Stone 500 text, font-size 14px
- Card: white bg, Stone 200 border, shadow-sm, 8px radius
- Grid: 2 columns on desktop, 1 on mobile

### News Timeline (Recent News tab)
- Left border: 2px solid Stone 300
- Timeline dots: 12px circles, Teal fill (#4dc0c7)
- Each item: headline (Stone 900, font-weight 600), date + source (Stone 500, font-size 14px), source as link in Teal
- "Why it matters" callout: Teal-soft background (rgba(77,192,199,0.12)), left border 3px solid Teal, padding 12px, Stone 700 text
- Items ordered newest first

### Signal Items (Qualification tab)
- Three sections: Positive Signals, Caution Signals, Unknown Gaps
- Each signal: badge + evidence text
  - Positive: Green 500 bg (10% opacity), Green 500 text badge
  - Caution: Amber 500 bg (10% opacity), Amber 500 text badge
  - Unknown: Blue 500 bg (10% opacity), Blue 500 text badge
- Evidence: Stone 600 text, indented below badge
- ICP Scorecard: table with criteria rows, teal progress bar fills (width = score/5 * 100%), overall score in large Amber 600 text

### Approach Section
- Entry points: numbered list with Teal left accent bar per item
- Opening hooks: card-style items with Amber 50 background, italic quote text
- Discovery questions: simple numbered list, Stone 700 text

### Tab Switching
- Vanilla JS `showTab(tabId)` function
- Active tab: Amber 600 text, 2px bottom border Amber 600, `rgba(217,119,6,0.1)` background
- Tab bar: Stone 200 bottom border, tabs as inline-block with padding
- Content panels: display:none by default, display:block when active
- First tab (Overview) active by default on load

## Constraints for `/frontend-design`

1. **Self-contained single HTML file** — ALL CSS and JS inline, no external dependencies, no CDN links, no Google Fonts
2. **Must follow Mycel tokens exactly** — this is a branded template, not a creative freestyle
3. **Responsive**: mobile breakpoint at 768px (tabs stack vertically, grids collapse to single column)
4. **File naming**: `[CompanyName]-account-dossier-[YYYY-MM-DD].html` (spaces replaced with hyphens, lowercase)
5. **Save to**: `/Users/mdmac/Projects/Mycel/memory/companies/`
6. **Data injection**: The `/research` skill will provide a structured data object. The template should use placeholder markers like `{{company.name}}` in the spec, but the actual HTML will be generated with real data interpolated
7. **No dark mode** — light theme only for dossiers
8. **Print-friendly** — hide tab bar on print, show all sections sequentially
9. **Accessible** — proper heading hierarchy, alt text for any images, focus-visible states

## Data Model Reference

The `/research` skill assembles this data structure before passing to `/frontend-design`:

```yaml
account:
  name: "Company Name"
  website: "https://..."
  industry: "B2B SaaS"
  founded: "2015"
  headquarters: "Austin, TX"
  employee_count: "500-1000"
  revenue_estimate: "$50M-$100M"
  funding_stage: "Series C"
  funding_total: "$120M"
  pe_ownership:
    firm: "Vista Equity Partners"
    fund: "Fund VII"
    investment_date: "2022-03"
    hold_period_stage: "Growth"
  quick_take: "2-3 sentence executive summary"

  overview:
    what_they_do: "..."
    products_services: ["Product A", "Product B"]
    target_customers: "Mid-market B2B companies"
    competitive_landscape: "Competes with X, Y, Z"
    acquisitions: ["Acquired CompanyA in 2023"]

  news:
    - headline: "Company Raises $50M Series C"
      date: "2024-01-15"
      source: "TechCrunch"
      source_url: "https://..."
      why_it_matters: "Signals investment in go-to-market expansion"

  people:
    - name: "Jane Smith"
      title: "CRO"
      linkedin_url: "https://linkedin.com/in/..."
      tenure: "2 years"
      background: "Former VP Sales at Competitor"
      talking_points: ["Shared connection via...", "Posted about AI in sales"]
      email: "jane@company.com"

  hiring:
    total_open_roles: 45
    departments:
      Sales: 12
      Engineering: 18
      Marketing: 8
      CS: 7
    growth_indicators: ["Sales team doubled in 6 months"]
    tech_stack_from_jobs: ["Salesforce", "Snowflake", "dbt"]

  qualification:
    positive_signals:
      - signal: "PE-backed with growth mandate"
        evidence: "Vista acquired in 2022, typical 3-5 year hold"
      - signal: "Active GTM hiring"
        evidence: "12 open sales roles, new CRO hired 6 months ago"
    caution_signals:
      - signal: "Recent layoffs in engineering"
        evidence: "LinkedIn data shows 15% reduction in Q3"
    unknown_gaps:
      - signal: "Current AI/automation maturity unknown"
        evidence: "No public statements on AI strategy"
    icp_score: 4
    icp_criteria:
      pe_backed: { score: 5, note: "Vista Equity" }
      revenue_range: { score: 4, note: "Est. $50-100M" }
      gtm_transformation: { score: 4, note: "New CRO, sales expansion" }
      decision_maker_access: { score: 3, note: "No direct connection yet" }
    recommended_action: "Strong fit — prioritize outreach to CRO"

  approach:
    entry_points:
      - "CRO Jane Smith — new in role, likely evaluating tools"
      - "VP Marketing — hiring for demand gen, may need enablement"
    opening_hooks:
      - "Vista portfolio companies typically centralize GTM ops within 18 months of acquisition"
      - "Their Salesforce + Snowflake stack suggests data-driven but may lack AI layer"
    discovery_questions:
      - "How are you measuring sales productivity post-acquisition?"
      - "What's your timeline for the GTM transformation?"
      - "How are reps using AI today vs. where you want to be?"

  metadata:
    generated_date: "2024-02-20"
    sources_used: ["Brave Search", "Clay", "NotebookLM", "Company Website"]
    notebooklm_notebook_url: "https://notebooklm.google.com/notebook/..."
```

Missing data should display as "Not found" with muted styling — the structure is always consistent regardless of data completeness.
