---
name: research
description: "Deep dive on a company or person — competitive intel, ICP fit, assessment generation. Trigger with 'research [company]', 'look up [person]', 'intel on [prospect]', 'who is [name]', 'competitive analysis', or 'ICP fit check'."
---

# /research — Unified Account & Contact Research

## Objective
Provide deep, actionable intelligence on a company or person. Consolidates: account-research, competitive-intelligence, icp-qualification, assessment-generation, stakeholder-mapping.

## Step 1: Determine Research Target
- If a **company** is mentioned → run company research (Steps 2-4)
- If a **person** is mentioned → run person research (Steps 5-6)
- If **competitive** keywords are used → run competitive analysis (Step 7)
- If **ICP** or **qualification** keywords → run ICP fit check (Step 8)

## Step 2: Company Research — Data Gathering (parallel)
Run ALL simultaneously:
- **Web search** — Recent news, funding, leadership changes, product launches
- **Clay enrichment** (`find-and-enrich-company`) — Headcount, tech stack, funding, competitors
- **Notion search** — Any existing records, meeting notes, email history for this company
- **Outlook email search** — Past correspondence with anyone @company domain

## Step 3: Company Research — Synthesis
Produce a structured brief:
- **Company snapshot:** Size, funding, industry, HQ, key products
- **Leadership team:** Key decision-makers with roles
- **Recent activity:** News, funding rounds, product changes (last 6 months)
- **Relevance:** Why this matters for Mike's consulting practice (check `memory/clients/` for active engagements)
- **Engagement angle:** Specific pain points or opportunities to lead with

## Step 4: Company Research — Save & Enrich
- If Clay tools are available, enrich with: tech stack, headcount growth, open jobs, recent news
- Save key findings to `memory/companies/[company-name].md`
- If stakeholders were identified, suggest running `/new-contact` for key people

## Step 5: Person Research — Data Gathering (parallel)
- **Clay enrichment** (`find-and-enrich-list-of-contacts`) — LinkedIn profile, work history, email
- **Web search** — Recent posts, publications, speaking engagements
- **LinkedIn** (via Clay or web) — Current role, tenure, background
- **Notion search** — Existing stakeholder record
- **Outlook email search** — Past correspondence

## Step 6: Person Research — Synthesis
Produce a structured brief:
- **Contact snapshot:** Name, title, company, location, LinkedIn
- **Background:** Career path, education, key expertise
- **Talking points:** Shared connections, mutual interests, conversation starters
- **Engagement strategy:** How to approach, what they care about

## Step 7: Competitive Analysis
When triggered by competitive keywords:
- Research the target competitor(s) using web search + Clay
- Compare against the relevant client or Mycel.io offering
- Produce: strengths, weaknesses, differentiation, key accounts, pricing intel
- Format as a scannable battlecard

## Step 8: ICP Fit Check
When triggered by ICP/qualification keywords:
- First, check `memory/clients/` for any client-specific ICP criteria
- If no client-specific ICP exists, use Mycel.io's default ICP:
  - PE-backed B2B software company
  - $10M-$500M revenue range
  - Active GTM transformation or AI adoption initiative
  - Decision-maker accessible
- Score: Strong Fit / Moderate Fit / Weak Fit with reasoning
- Note which ICP criteria were used (client-specific or default)

## Output Format
- Lead with a 2-3 sentence executive summary
- Use headers and scannable sections (not walls of text)
- End with: "Want me to add anyone to the Stakeholders DB?" or "Want me to draft outreach?"
- Save research artifact to appropriate memory/ directory

## Constraints
- Use MS365 for email search, not Gmail
- Check Notion before web search — we may already have context
- Clay enrichment is a bonus, not a blocker — proceed with web research if Clay tools unavailable
