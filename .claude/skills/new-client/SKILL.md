---
name: new-client
description: "Onboard a new client engagement. Creates folder structure, scaffolds memory context file, adds primary contact, and sets up CRM entries. Trigger with '/new-client [company name]' or '/new-client [company] with [contact name]'."
---

# /new-client -- Client Onboarding

## Objective
Set up all the infrastructure for a new client engagement in one step: folder, memory file, primary contact, and CRM entries.

## Step 1: Gather Client Info

If provided inline (e.g., `/new-client Acme Corp with Jane Smith`), parse the company name and optional primary contact. Otherwise, ask Mike for:
- **Company name** (required)
- **Engagement type** (what are we doing for them?)
- **Primary contact name** (if known)
- **How they connected** (referral, cold outreach, etc.)
- **Timeline** (if known)

## Step 2: Create Client Folder

Create `clients/[client-name]/` directory (lowercase, hyphens for spaces).

If Mike has any initial documents (proposals, decks), move or save them here.

## Step 3: Create Client Context File

Create `memory/clients/[client-name].md` using the template structure:

```markdown
# [Client Name] -- Client Context

> Last reviewed: [today's date]

## Engagement Overview
- **Client:** [company name and brief description]
- **Engagement:** [scope]
- **Timeline:** [dates]
- **Budget:** TBD
- **Team:** Mike Duncan (lead), [others if known]

## Key People
| Who | Role | Notes |
|-----|------|-------|
| [Primary contact] | [Title] | [Context] |

## Current Status
- [Initial status]

## Deliverables
- Client folder: `clients/[client-name]/`

## Operational Context
- [Communication preferences, email domains, special considerations]
```

Fill in what we know; leave TBD for unknowns.

## Step 4: Add Primary Contact

If a primary contact was provided:
1. Run the `/new-contact` workflow inline (research, enrich, save to contacts/, add to Notion)
2. Update the memory file's Key People table with the results

If no primary contact yet, note in the memory file that primary contact is TBD.

## Step 5: Summary

Present Mike with:
- Confirmation of what was created (folder, memory file, contact)
- Anything that needs manual follow-up (Notion setup, meeting scheduling)
- Suggested next steps ("Schedule intro call?", "Draft outreach?", "Research the company?")

## Constraints
- All files go in their canonical locations (clients/, memory/clients/, contacts/)
- Nothing at root level
- Use the naming convention: lowercase, hyphens for spaces
- Skills are client-agnostic -- this skill creates the structure, other skills operate on it
