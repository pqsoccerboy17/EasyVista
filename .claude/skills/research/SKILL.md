---
name: research
description: "Deep dive on a company or person — multi-source research with NotebookLM deep analysis, branded HTML dossier output, competitive intel, ICP fit. Trigger with 'research [company]', 'look up [person]', 'intel on [prospect]', 'who is [name]', 'competitive analysis', or 'ICP fit check'."
---

# /research — Unified Account & Contact Research

## Objective
Provide deep, actionable intelligence on a company or person. For company research, runs an 8-phase pipeline that produces a branded HTML dossier with persistent NotebookLM notebook. For person research, produces a structured contact brief.

## Step 1: Determine Research Target
- If a **company** is mentioned → run company research (Phases 1-8 below)
- If a **person** is mentioned → run person research (Steps 5-6 below)
- If **competitive** keywords are used → run competitive analysis (Step 7)
- If **ICP** or **qualification** keywords → run ICP fit check (Step 8)

---

## Company Research Pipeline (8 Phases)

### Phase 1: Initialize (~30s)
1. Parse target company name and/or URL from user input
2. Check **Notion CRM** for existing records:
   - Search Stakeholders DB (`1447853a-4ae0-4cc2-b560-0879e5f97374`) for contacts at this company
   - Search Granola Notes for any meeting notes mentioning the company
3. Check **MS365 Outlook** for prior correspondence:
   - `outlook_email_search` for emails from @company domain (Inbox)
   - `outlook_email_search` for emails to @company domain (Sent Items)
4. Check `memory/companies/` for any existing research on this company
5. Summarize what we already know before starting external research

### Phase 2: Multi-Source Research (parallel, 2-3 min)
Run ALL simultaneously — do not wait for one to finish before starting another:

- **Brave Search** (5-6 queries):
  - "[Company] overview founding leadership"
  - "[Company] recent news funding 2024 2025"
  - "[Company] products services customers"
  - "[Company] competitors market position"
  - "[Company] careers jobs open positions"
  - "[Company] private equity acquisition investor" (if PE signals found)

- **Clay enrichment** (`find-and-enrich-company`):
  - Headcount, tech stack, funding rounds, competitors, revenue estimate

- **Clay contacts** (`find-and-enrich-contacts-at-company`):
  - Key leadership: CEO, CRO, CTO, VP Sales, VP Marketing
  - Include LinkedIn URLs, emails, titles

- **Fetch/Firecrawl** (website scraping):
  - Company about page
  - Press/news page
  - Careers page (for hiring signals + tech stack)

### Phase 3: NotebookLM Setup (parallel with Phase 2, ~1 min)
1. `notebook_create` — name: "[Company Name] - Account Research"
2. `notebook_add_url` — add up to 5 URLs in parallel (skip silently if any fail with 404/blocked):
   - Company homepage (e.g., `https://www.easyvista.com`)
   - Company press/news page (guess standard pattern: `/press-releases`, `/newsroom`, `/news`)
   - Top 2-3 specific news article URLs from Phase 2 web search results
3. `notebook_add_text` — add as text sources:
   - Clay enrichment data (company + contacts combined into one text block) — **required minimum**
   - Notion CRM summary (if existing records found in Phase 1)
   - Outlook email summary (if prior correspondence found in Phase 1)

> **Graceful failure:** If `notebook_add_url` fails for a URL, skip it silently and continue. Minimum 1 text source (Clay data) is required before proceeding to deep research. If NotebookLM tools are entirely unavailable: skip Phases 3-5.5, proceed to Phase 6 with web + Clay data only. Note in metadata that NotebookLM was unavailable.

### Phase 4: NotebookLM Deep Research (always runs, 3-5 min)
1. `research_start` (mode: "deep") with a GTM-focused research query:
   > "Analyze [Company Name]'s competitive position, strategic direction, recent developments, leadership changes, funding history, and go-to-market strategy. What signals suggest they are investing in sales and marketing transformation? What technology decisions have they made recently?"
2. Capture the `task_id` from the response
3. **Polling with timeout fallback** (NotebookLM MCP has ~30s timeout — never use built-in polling):
   - `bash sleep 30` → `research_status` (max_wait: 0, single non-blocking check)
   - If completed → `research_import` → proceed to Phase 5
   - If in_progress or timeout error → `bash sleep 60` → retry `research_status` (max_wait: 0)
   - Repeat up to 3 total status checks (30s + 60s + 60s = ~2.5 min)
   - If still not complete after 3 retries:
     - Fall back to `research_start` (mode: "fast")
     - Poll fast research: `bash sleep 15` → `research_status` (max_wait: 0) — completes in ~30s
     - Note in metadata: "Deep research timed out; fast research used as fallback"
4. **ALWAYS** call `research_import` before proceeding — this adds findings back as a notebook source

This runs every time — the depth of insight justifies the wait. Do NOT prompt the user to ask if they want deep research.

### Phase 5: NotebookLM AI Synthesis (~1 min)
Use `notebook_query` to fill specific gaps and get AI-synthesized answers:
- "What is this company's competitive position and key differentiators?"
- "What are the most significant recent developments in the last 12 months?"
- "What does their leadership team look like and have there been recent changes?"
- "What signals suggest they're investing in GTM transformation or AI adoption?"
- "What is their technology stack and how mature is their data infrastructure?"

### Phase 5.5: Generate NotebookLM Studio Artifacts (mandatory)
Generate all three artifacts — these are NOT optional:

1. `report_create` — format: "Briefing Doc", confirm: true
2. `infographic_create` — orientation: "landscape", detail_level: "detailed", focus_prompt based on the quick_take from Phase 5, confirm: true
3. `audio_overview_create` — format: "brief", length: "short", focus_prompt highlighting key GTM/strategic findings, confirm: true
4. Poll `studio_status` every 15 seconds (`bash sleep 15` → `studio_status`) until all 3 show "completed" (max 5 min wait)
5. Capture `audio_url` and `infographic_url` from completed studio items for inclusion in deliverables

> If any studio artifact fails after 5 minutes, proceed without it and note the failure in metadata.

### Phase 6: Data Assembly
Merge all sources into the standard data model. Every field must be populated — use "Not found" for missing data so the structure is always consistent:

```yaml
account:
  name, website, industry, founded, headquarters, employee_count
  revenue_estimate, funding_stage, funding_total
  pe_ownership: { firm, fund, investment_date, hold_period_stage }
  quick_take: "2-3 sentence executive summary"

  overview:
    what_they_do, products_services, target_customers, competitive_landscape, acquisitions

  news:
    - headline, date, source, source_url, why_it_matters
    # "Why it matters" = sales relevance (buying signal, risk, opportunity)

  people:
    - name, title, linkedin_url, tenure, background, talking_points, email
    # Include up to 8 key people, prioritize: CRO, VP Sales, CEO, CTO, VP Marketing

  hiring:
    total_open_roles, departments (by count), growth_indicators, tech_stack_from_jobs

  qualification:
    positive_signals: [{ signal, evidence }]
    caution_signals: [{ signal, evidence }]
    unknown_gaps: [{ signal, evidence }]
    icp_score: 1-5
    icp_criteria:
      pe_backed: { score: 1-5, note }
      revenue_range: { score: 1-5, note }
      gtm_transformation: { score: 1-5, note }
      decision_maker_access: { score: 1-5, note }
    recommended_action: "Strong fit / Moderate fit / Weak fit — [specific next step]"

  approach:
    entry_points: ["Person — reason they're the right entry"]
    opening_hooks: ["Insight-based hook tied to research findings"]
    discovery_questions: ["Question tied to specific finding"]

  metadata:
    generated_date, sources_used, notebooklm_notebook_url, audio_url, infographic_url
```

**ICP Scoring Guide:**
- First check `memory/clients/` for any client-specific ICP criteria
- If no client-specific ICP exists, use Mycel.io's default ICP:
  - PE-backed B2B software company
  - $10M-$500M revenue range
  - Active GTM transformation or AI adoption initiative
  - Decision-maker accessible
- Score each criterion 1-5, calculate average for overall ICP score

### Phase 7: HTML Dossier via `/frontend-design`
1. Read `dossier-template-spec.md` from this skill's directory (`/Users/mdmac/Projects/Mycel/.claude/skills/research/dossier-template-spec.md`)
2. Invoke `/frontend-design` with:
   - The template spec (brand constraints, component specs, tokens)
   - The assembled data model from Phase 6
   - Instruction: "Generate a self-contained HTML dossier following the template spec exactly. Use the Mycel light theme tokens. Inject the research data into the 6-tab structure."
3. The spec constrains structure and brand; `/frontend-design` handles visual execution
4. File naming: `[company-name]-account-dossier-[YYYY-MM-DD].html` (lowercase, hyphens for spaces)

### Phase 8: Save & Deliver
1. **HTML dossier** saved to `/Users/mdmac/Projects/Mycel/memory/companies/[company-name]-account-dossier-[date].html`
2. **Raw research markdown** saved to `/Users/mdmac/Projects/Mycel/memory/companies/[company-name].md`
   - Structured markdown with all research data for future reference
   - Includes source attributions and NotebookLM notebook link
3. **Present summary** to user:
   - 2-3 sentence executive summary
   - ICP score and recommended action
   - Audio briefing: direct link from `audio_url`
   - Infographic: direct link from `infographic_url`
   - Briefing Doc: note that it's inside the NotebookLM notebook
   - NotebookLM notebook link (for ongoing reference)
   - Path to HTML dossier
4. **Offer optional next steps:**
   - "Draft outreach to [suggested entry point contact]?" (triggers `/outreach`)
   - "Add key contacts to Notion Stakeholders DB?" (triggers `/new-contact` for each)

### Graceful Degradation
- **No Clay?** → Proceed with web search only. Note "Clay unavailable" in metadata.
- **No NotebookLM?** → Skip Phases 3-5.5. Build dossier from web + Clay data. Note "NotebookLM unavailable" in metadata.
- **No Notion CRM data?** → Skip Phase 1 CRM check. Note "No existing CRM records" in metadata.
- **No Firecrawl?** → Use Brave Search + basic fetch for website content.
- **Partial data?** → Always produce the dossier. Missing fields show "Not found" with muted styling.

---

## Person Research

### Step 5: Person Research — Data Gathering (parallel)
Run ALL simultaneously:
- **Clay enrichment** (`find-and-enrich-list-of-contacts`) — LinkedIn profile, work history, email
- **Web search** — Recent posts, publications, speaking engagements, podcast appearances
- **LinkedIn** (via Clay or web search) — Current role, tenure, career trajectory
- **Notion search** — Existing stakeholder record in Stakeholders DB
- **Outlook email search** — Past correspondence (both Sent and Received)

### Step 6: Person Research — Synthesis
Produce a structured brief:
- **Contact snapshot:** Name, title, company, location, LinkedIn URL, email
- **Background:** Career path, education, key expertise, years in current role
- **Talking points:** Shared connections, mutual interests, recent public activity, conversation starters
- **Engagement strategy:** How to approach, what they care about, warm intro paths
- Save to `memory/people/[person-name].md`

---

## Competitive Analysis

### Step 7: Competitive Analysis
When triggered by competitive keywords ("competitive analysis", "battlecard", "vs [competitor]"):
1. Research the target competitor(s) using web search + Clay
2. Compare against the relevant client offering or Mycel.io
3. Produce a structured battlecard:
   - Strengths vs. weaknesses (side-by-side)
   - Key differentiators
   - Target accounts / ideal customer comparison
   - Pricing intel (if available)
   - Win/loss patterns
4. Format as scannable HTML or markdown
5. Save to `memory/companies/[competitor]-battlecard.md`

---

## ICP Fit Check

### Step 8: ICP Fit Check
When triggered by ICP/qualification keywords ("ICP fit", "qualify", "is this a good fit"):
1. First, check `memory/clients/` for any client-specific ICP criteria
2. If no client-specific ICP exists, use Mycel.io's default ICP:
   - PE-backed B2B software company
   - $10M-$500M revenue range
   - Active GTM transformation or AI adoption initiative
   - Decision-maker accessible
3. Run quick company research (abbreviated Phase 2 — web search + Clay only, no NotebookLM)
4. Score each criterion 1-5 with evidence
5. Overall rating: **Strong Fit** (4-5) / **Moderate Fit** (3) / **Weak Fit** (1-2) with reasoning
6. Note which ICP criteria were used (client-specific or default)

---

## Output Format
- Always lead with a 2-3 sentence executive summary
- Use headers and scannable sections (no walls of text)
- For company research: deliver HTML dossier + offer next steps
- For person research: deliver markdown brief + offer to add to Notion
- End with actionable next step suggestions

## Constraints
- Use MS365 for email search, not Gmail
- **Always search Sent Items too** — critical context is in emails Mike sent
- Check Notion before web search — we may already have context
- Clay enrichment is a bonus, not a blocker — proceed with web research if Clay tools unavailable
- NotebookLM deep research runs automatically — do not ask the user for permission
- Save all research artifacts to the appropriate `memory/` directory

IMPORTANT: NotebookLM MCP tools have a ~30s timeout. When polling:
- Always use max_wait: 0 (single non-blocking check)
- Use bash sleep between polls instead of the tool's built-in polling
- Pattern: sleep N → check (max_wait: 0) → sleep N → check → etc.
- Never use poll_interval or max_wait > 0 — they will timeout at the MCP layer
