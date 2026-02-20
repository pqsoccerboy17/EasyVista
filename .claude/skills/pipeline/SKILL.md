---
name: pipeline
description: "Deal health, forecasting, stage review, negotiation strategy, win/loss patterns. Trigger with 'pipeline review', 'deal health', 'forecast', 'how are my deals', 'negotiation strategy for [deal]', 'why did we win/lose [deal]', or 'coach me'."
---

# /pipeline — Unified Pipeline & Deal Intelligence

## Objective
Single command for everything pipeline-related — health check, forecasting, deal strategy, negotiation prep, and performance coaching. Consolidates: pipeline-review, forecast, deal-room, negotiation-playbook, roi-calculator, win-loss-analysis, sales-coach.

## Step 1: Determine What's Needed
Parse Mike's request to determine which mode(s) to run:
- **"pipeline review"** / **"how are my deals"** → Pipeline Health (Step 2)
- **"forecast"** → Weighted Forecast (Step 3)
- **"deal room for [company]"** / **"everything on [deal]"** → Deal Deep-Dive (Step 4)
- **"negotiation"** / **"pricing objection"** → Negotiation Playbook (Step 5)
- **"ROI"** / **"business case"** → ROI Model (Step 6)
- **"win loss"** / **"post-mortem"** → Win/Loss Analysis (Step 7)
- **"coach me"** / **"how am I doing"** → Performance Coaching (Step 8)

If unclear, default to Pipeline Health (Step 2) — it's the most generally useful.

## Step 2: Pipeline Health
Data sources (parallel):
- Notion pipeline/deal data
- Recent email activity for each deal
- Granola notes for meeting context
- Calendar for upcoming meetings

Produce:
- **Active deals** ranked by priority (revenue × probability × urgency)
- **Movement this week** — which deals advanced, stalled, or regressed
- **At-risk deals** — no activity >5 days, missing next steps, approaching deadline
- **Top 3 actions** — specific things Mike should do this week

## Step 3: Weighted Forecast
Build three scenarios:
- **Best case** — every active deal closes on time
- **Likely case** — weighted by stage probability
- **Worst case** — only committed deals
Include: commit vs. upside breakdown, gap to target (if target known), expected close dates

## Step 4: Deal Deep-Dive
For a specific deal, assemble everything:
- **Deal snapshot** — Stage, value, close date, key stakeholders
- **Activity timeline** — All emails, meetings, notes in chronological order
- **Stakeholder map** — Decision makers, champions, blockers, and their current positions
- **Risk factors** — Stalled conversations, missing stakeholders, competitive threats
- **Recommended next steps** — Specific actions with draft messages if applicable

## Step 5: Negotiation Playbook
For a specific deal entering negotiation:
- **BATNA analysis** — Mike's best alternative + estimated client BATNA
- **Objection handling** — Top 3 likely objections with responses
- **Pricing defense** — Value justification, comparable benchmarks
- **Walk-away criteria** — Clear red lines
- **Concession strategy** — What to give vs. what to protect

## Step 6: ROI Model
For a specific deal, build a value case:
- **Current state costs** — Time, headcount, opportunity cost of status quo
- **Proposed improvement** — Specific metrics the engagement would improve
- **ROI calculation** — Payback period, first-year return, 3-year NPV
- **EBITDA impact** — For PE-backed companies, translate to EBITDA bridge
- Format as clean, shareable output (can pipe to `/docx` or `/pptx`)

## Step 7: Win/Loss Analysis
For closed deals (won or lost):
- **What happened** — Timeline of key events
- **Process assessment** — Did we follow best practices? Where did we deviate?
- **Stakeholder analysis** — Who championed us? Who blocked? Who was missing?
- **Competitive factors** — Were competitors involved? How did we differentiate?
- **Pricing analysis** — Did pricing align with value delivered?
- **Lessons** — 3 specific takeaways for future deals

## Step 8: Performance Coaching
Holistic assessment across 5 dimensions:
1. **Pipeline health** — Coverage ratio, stage distribution, velocity
2. **Activity consistency** — Outreach volume, follow-up discipline, meeting cadence
3. **Outreach quality** — Response rates, personalization, channel mix
4. **Deal strategy** — Multi-threading, stakeholder coverage, competitive positioning
5. **Win/loss patterns** — What's working, what's not

Deliver as: strengths (keep doing), improvements (start doing), and one specific action for this week.

## Output Format
- Always lead with a 2-3 sentence executive summary
- Use scannable sections with clear headers
- End with specific recommended actions
- Offer to generate artifacts: "Want me to create a deck/report/tracker from this?"

## Constraints
- Pull from Notion first, then email/calendar for supplementary context
- Don't fabricate pipeline data — if Notion doesn't have deal info, ask Mike
- For forecasting, be honest about confidence levels — don't give false precision
- Client-specific context lives in `memory/clients/` — check the relevant file
