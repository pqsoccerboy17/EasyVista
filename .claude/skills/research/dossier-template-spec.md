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
├── 🎧 Audio Briefing: [direct audio_url link]
├── 📊 Infographic: [direct infographic_url link]
├── 📓 Full Notebook: [notebook URL]
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
- `--teal: #4dc0c7` (Default brand accent — section title underlines, info boxes, LinkedIn links, avatars, entry point badges)
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
- `--success-bg: rgba(34, 197, 94, 0.1)` (positive badge background)
- `--warning-bg: rgba(245, 158, 11, 0.1)` (caution badge background)
- `--info-bg: rgba(59, 130, 246, 0.1)` (unknown badge background)

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

### KPI Cards (4-column grid, DisplayCards-inspired glassmorphism)
- **Container:** `transform: skewY(-2deg)` (subtle professional skew)
- **Cards:** `backdrop-filter: blur(12px)`, `rgba(255,255,255,0.7)` background, `rgba(255,255,255,0.4)` border
- **Top edge sheen:** `linear-gradient(90deg, var(--teal), var(--accent))` 3px line, `opacity: 0` → `1` on hover
- **Values:** `filter: saturate(0.7)` at rest, full color on hover; Amber 600 default, Warning for moderate ICP scores
- **Animation:** `@keyframes kpiSlideIn` with staggered delay via `--card-index` custom property (100ms per card)
- **Hover:** `translateY(-8px)` lift with `cubic-bezier(0.16, 1, 0.3, 1)` 700ms transition
- **Counter-skew:** All child elements get `transform: skewY(2deg)` to keep text level
- **ICP card:** Add `.kpi-icp` class; use `var(--warning)` for moderate (3/5), `var(--success)` for strong (4+/5)
- Value: large text (2em), font-weight 700
- Label: small text (0.9em), Stone 500, uppercase, letter-spacing 0.5px
- Border-radius: 12px
- On mobile (< 768px): 2x2 grid, remove skew (`transform: none`), disable animation

### Person Cards (Key People tab)
- **Avatar:** 48px circular, Teal (#4dc0c7) background, white initials text, font-weight 700
- **Header layout:** Flex row — avatar + info block (name, title)
- **Name:** `.person-name` — Stone 900, font-weight 700, 1.1rem
- **Title:** `.person-title` — Amber 600, font-weight 600, 0.95rem
- **Detail lines:** `.person-detail` — Stone 600, 0.85rem (tenure, location)
- **LinkedIn link:** `.person-linkedin` — Teal color, font-weight 600, underline on hover
- **Talking points:** Below a `border-top: 1px solid Stone 200` separator, Stone 600 text, 0.85rem, line-height 1.6
- Card: white bg, Stone 200 border, shadow-sm, 8px radius
- Grid: `repeat(auto-fill, minmax(300px, 1fr))` — responsive columns, 1 on mobile

### News Items (Recent News tab)
- **Card background:** `var(--teal-soft)` (rgba(77,192,199,0.12))
- **Left border:** 4px solid `var(--teal)`
- **Title:** Stone 900, font-weight 700, font-size 1.1rem
- **Meta (date + source):** Stone 500, font-size 0.85em
- **Link:** Teal color, font-weight 500, underline on hover
- **"Why it matters":** Stone 600, font-size 0.9em, italic
- Items ordered newest first
- Margin-bottom 12px between items, 8px border-radius

### Qualification Tab Components

**Score Hero Card:**
- `linear-gradient(135deg, color1, var(--teal))` background, white text
- Color1 varies by score: `var(--warning)` for moderate (2-3/5), `var(--success)` for strong (4-5/5), `var(--danger)` for weak (1/5)
- Score number: 3rem, font-weight 700, centered
- Label: 1.2rem, font-weight 600

**ICP Scorecard (progress bars):**
- Container: Stone 50 bg, 24px padding, 8px radius
- Each criterion: label (flex space-between with score) + 8px progress bar
- Progress bar: Stone 200 track, Amber 600 fill, `width = score/5 * 100%`
- Criteria should reflect the specific ICP dimensions evaluated

**Signal Badges:**
- Three sections: Positive Signals, Caution Signals, Unknown Gaps
- Each badge: `.badge` with icon circle + title + description text
- Layout: single-column grid (better readability with descriptions)
  - `.badge-positive`: `var(--success-bg)` background, success left border, white checkmark icon on success bg
  - `.badge-caution`: `var(--warning-bg)` background, warning left border, white warning icon on warning bg
  - `.badge-unknown`: `var(--info-bg)` background, info left border, white "?" icon on info bg
- Icon circles: 32px, rounded, solid semantic color bg, white text
- Title: Stone 900, font-weight 700
- Description: Stone 600, 0.95rem

### Approach Section

**Entry Points:**
- `.entry-point` cards: Stone 50 bg, 4px Teal left border, 8px radius
- Teal numbered badge circles: 28px, white text on Teal bg, inline-flex centered
- Flex layout: badge + content block (h4 title + p description)

**Opening Hooks:**
- `.hook-card` cards: Amber 50 bg, 1px Amber 600 border, 8px radius — visually distinct from entry points
- Amber numbered badge circles: 28px, white text on Amber 600 bg
- Flex layout: badge + content block (h4 title + p quote text)

**Discovery Questions:**
- `.discovery-questions` container: Stone 50 bg, 24px padding, 8px radius
- `.discovery-list` items with CSS `::before` "Q" badges: 24px Teal-soft circles, Teal "Q" text
- Left padding 36px to accommodate badge
- Stone 600 text for question content

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
8. **Print-friendly** — hide tab bar on print, show all sections sequentially, disable transforms/glassmorphism/animations (`backdrop-filter: none`, `transform: none`, `animation: none`, `filter: none`)
9. **Accessible** — proper heading hierarchy, alt text for any images, `focus-visible` states on tab buttons, LinkedIn links, footer links, and news links (2px solid Amber 600 outline, 2px offset)
10. **Section headings** — All `.section h2` headings use `border-bottom: 3px solid var(--teal)` (teal accent, not border color)
11. **Footer links** — Use `var(--teal)` color (not info blue)

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
