# AI Account Deep-Dive Playbook for AEs

**Purpose:** Run this playbook before engaging a target account. Output is a 1-2 page account brief that gives you everything you need to open the right conversations with the right people.

**Time to complete:** 20-30 minutes (most of it is wait time while tools run)

**Stack:** Claude/NotebookLM + Clay + HubSpot + company docs

---

## Before You Start

Gather these inputs:
- Target company name and website URL
- Any docs you already have (past proposals, meeting notes, case studies they shared)
- The HubSpot company record URL (if it exists)

---

## Step 1 -- Check What You Already Have (5 min)

**In HubSpot:**
1. Search the company record. Note:
   - Last activity date and owner
   - Open/closed deals and their stages
   - Contacts already in the system (titles, last contact dates)
   - Any notes or call logs from prior AEs
2. If no record exists -- create one now before moving on.

**In your files/email:**
- Pull any prior proposals, SOWs, or decks sent to this account
- Note any commitments or objections from prior conversations

**Checkpoint:** Summarize what you know in one sentence before adding AI research.

---

## Step 2 -- Clay Enrichment (3 min setup, runs in background)

**Company enrichment:**
1. Search the company in Clay (or use "Find and Enrich Company")
2. Capture: headcount, revenue estimate, tech stack, funding stage, recent hires
3. Note the growth trajectory -- are they hiring fast in sales/marketing? That signals GTM investment.

**Contact enrichment:**
- Run "Find Contacts at Company" for: CEO, CRO, VP Sales, VP Marketing, CTO
- Pull LinkedIn URLs, emails, and tenure for each
- Flag anyone you have a warm connection to

---

## Step 3 -- NotebookLM / Claude Deep Research (10-15 min)

**Create a new NotebookLM notebook** named "[Company] -- Account Deep-Dive [Date]".

**Add these sources:**
1. Company website (homepage + /about + /press or /newsroom)
2. 2-3 recent news articles about the company (from Google News or Clay results)
3. Any docs you collected in Step 1 (upload as PDFs or paste as text)
4. The Clay enrichment summary (paste as text)
5. Their HubSpot notes export (copy/paste from Step 1)

**Run the deep research query:**
> "Analyze [Company]'s strategic direction, recent developments, leadership changes, competitive position, and technology decisions. What signals suggest they are investing in sales, marketing, or operational transformation? What are the most important things an AE should know before an introductory call?"

**While that runs, move to Step 4.**

---

## Step 4 -- Competitive and News Scan (parallel with Step 3)

Open a Claude conversation and run:

**Prompt 1 -- Recent news:**
> "Search for news about [Company] in the last 6 months. Summarize the 3-5 most significant developments and explain why each matters from a sales perspective."

**Prompt 2 -- Competitive landscape:**
> "Who are [Company]'s top 3 competitors? How does [Company] differentiate? What does their competitive position tell us about their strategic priorities?"

Copy the outputs into your brief template (Section 3 below).

---

## Step 5 -- Assemble the Brief (5 min)

Use the template below. Fill in every section -- write "unknown" if you can't find something, not blank.

---

## Account Brief Template

**Account:** [Company Name]
**Date:** [YYYY-MM-DD]
**AE:** [Your name]
**HubSpot Record:** [URL]

---

### 1. Quick Take
*2-3 sentences: What does this company do, who do they sell to, and why are they relevant right now?*

[Write here]

---

### 2. Company Snapshot

| Field | Detail |
|-------|--------|
| Industry | |
| Headcount | |
| Revenue estimate | |
| Funding / ownership | |
| HQ location | |
| Founded | |
| Website | |

---

### 3. Recent Developments
*Top 3-5 news items with sales relevance. Format: Headline -- Why it matters for us.*

1.
2.
3.

---

### 4. Key People

| Name | Title | Tenure | LinkedIn | Email | Notes |
|------|-------|--------|----------|-------|-------|
| | | | | | |
| | | | | | |
| | | | | | |

**Warm connections:** [List any mutual contacts or LinkedIn connections]

---

### 5. Strategic Signals
*What tells us this account is -- or isn't -- ready to invest in what we offer?*

**Positive signals:**
- [Signal] -- [Evidence]
- [Signal] -- [Evidence]

**Caution signals:**
- [Signal] -- [Evidence]

**Unknown gaps:**
- [What we still need to find out]

---

### 6. HubSpot History
*What has happened before? Be honest.*

- Prior contact: [Yes/No -- if yes, when and outcome]
- Open deals: [Stage, value, last activity]
- Prior AE: [Name, if applicable]
- Key notes: [Any commitments, objections, or context from prior outreach]

---

### 7. Recommended Next Step

**ICP fit:** Strong / Moderate / Weak

**Entry point:** [Name] -- [Title] -- [Why they're the right first call]

**Opening hook:** [1-2 sentences grounded in your research -- what insight will open the conversation?]

**Discovery questions:**
1. [Question tied to a specific signal you found]
2. [Question about their current state / pain]
3. [Question about timeline, budget, or initiative ownership]

**Proposed action:** [First outreach -- email / LinkedIn / warm intro / call -- with target date]

---

## Checklist Before Sending Outreach

- [ ] HubSpot record created or updated
- [ ] At least 1 key contact enriched in Clay
- [ ] NotebookLM notebook saved (link it in HubSpot notes)
- [ ] Brief filed in the account folder or attached to HubSpot record
- [ ] Opening hook reviewed -- is it specific, not generic?
- [ ] Manager spot-checked the ICP fit rating

---

## Tips

**Do this every time, not just for big accounts.** A 20-minute brief before a cold call doubles your chances of a second conversation.

**The hook is everything.** "I noticed you hired 12 BDRs last quarter" beats "I work with companies like yours" every time. Use your research.

**Update the brief after every call.** Add what you learned. This becomes your account memory.

**Use Claude for drafting.** After filling out the brief, paste it into Claude and ask: "Draft a personalized cold email to [Name] using this brief." Edit before sending.

---

*Template version: 1.0 | Created: 2026-03-06 | Owner: Mycel.io*
