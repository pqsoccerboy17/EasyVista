---
name: new-contact
description: "Research a new contact, enrich via Clay/LinkedIn, save a structured profile, and add to Notion stakeholders DB. Trigger with '/new-contact [name] at [company]' or '/new-contact' to be prompted."
---

You are running the **new-contact** workflow. This automates the process of researching, enriching, and storing a new business contact when someone is introduced via email, meeting, or referral.

## 1. Gather Contact Info

If the user provided a name and company inline (e.g., `/new-contact Andrew Bell at Greenridge Growth`), parse those. Otherwise, ask the user for:
- **Full name** (required)
- **Company** (required)
- **Email address** (if known)
- **How they were introduced** (e.g., "Henry intro'd us", "met at conference", "cold outreach")
- **Any context** (role, location, relevance)

Use AskUserQuestion if any required fields are missing.

## 2. Web Research

Search the web for the contact and their company to build a profile:
- Search: `"[Name]" "[Company]" site:linkedin.com` → get LinkedIn URL
- Search: `"[Name]" "[Company]" [role/title]` → get bio, background, education
- Search: `"[Company]" [industry] [location]` → get company overview, size, funding, focus areas
- Fetch the company team/about page if available

Extract:
- Full name, title, LinkedIn URL
- Professional background (prior companies, education)
- Company overview (founded, size, sector, funding, HQ)
- Relevance to Mike's consulting practice (check `memory/clients/` for active engagements)

## 3. Clay Enrichment (if Clay MCP tools are available)

If Clay MCP tools (`find-and-enrich-contacts-at-company`, `add-contact-data-points`) are available in the current session:
- Run `find-and-enrich-contacts-at-company` with the contact's name, company, and email
- Extract: LinkedIn URL, title, location, company data, social profiles
- Run `add-contact-data-points` to tag the contact with enrichment metadata

If Clay tools are NOT available, skip this step — the web research in Step 2 provides sufficient coverage. Note in the output that Clay enrichment was skipped.

## 4. Save Contact Profile

Create a structured markdown file at:
```
contacts/[firstname]-[lastname]-[company].md
```
(Relative to the project root — works in both Cowork and Claude Code.)

Use this template:

```markdown
# [Full Name] — [Company]

## Contact Info
- **Email:** [email or "unknown"]
- **LinkedIn:** [URL]
- **Company:** [Company Name]
- **Title:** [Title]
- **Location:** [City, State/Country]

## Background
- [Education, prior roles, key career highlights]
- [Relevant experience or domain expertise]

## [Company Name]
- **Founded:** [year]
- **Focus:** [sector/industry]
- **Size:** [employees, revenue, funding if known]
- **Key details:** [any notable info]

## Relationship Context
- **Intro'd by:** [who introduced them, or how they connected]
- **Date:** [date of introduction]
- **Status:** [e.g., "warm intro → meeting scheduled", "cold outreach sent"]
- **Notes:** [any context from the user]

## Relevance to Mycel.io
- [Why this contact matters — potential for partnership, portfolio work, referrals, etc.]

## Status
- **Stage:** [warm intro / meeting scheduled / outreach sent / etc.]
- **Next action:** [what Mike should do next]
```

## 5. Add to Notion Stakeholders DB (if Notion MCP tools are available)

If Notion MCP tools (`search`, `create-pages`) are available in the current session:
1. Search Notion for the stakeholders database in the "AI Sales Enablement Assessment" workspace
2. Create a new page in that database with properties:
   - Name: [Full Name]
   - Company: [Company Name]
   - Email: [email]
   - Title: [Title]
   - Status: [appropriate status — e.g., "scheduled" if meeting booked, "outreach_sent" if email sent]
   - LinkedIn: [URL]
   - Source: [who intro'd or how they connected]
   - Notes: [brief context]

If Notion tools are NOT available, inform the user that the contact profile has been saved locally and they should manually add to Notion. Provide the key fields in a copy-pasteable format.

## 6. Summary Output

Present the user with:
- A brief summary of what was found (2-3 sentences)
- Link to the saved contact profile file
- Confirmation of Notion entry (or note that manual entry is needed)
- Confirmation of Clay enrichment (or note that it was skipped)
- Suggested next action (e.g., "Schedule coffee meeting", "Send intro email")

## Constraints
- **Tool preferences:** Use O365 tools for email/calendar, Notion for database, Clay for enrichment (per CLAUDE.md)
- **File location:** Always save contacts to `contacts/` at the project root
- **Privacy:** Never share contact's personal info with third parties or external tools beyond Clay/Notion
- **Mike is not a developer** — handle all file operations directly, don't show commands
