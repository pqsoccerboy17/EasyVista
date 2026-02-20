---
name: next-steps
description: "Surface recent conversations, calls, and meetings across all connected sources — then draft actionable next steps for each. No name required. Trigger with /next-steps."
---

# Next Steps — Automated Conversation Recap & Action Drafting

## Objective
Automatically identify who the user (Mike Duncan, michaelduncan17@gmail.com) recently spoke with, pull context from every connected source, and draft clear next steps for each conversation — without requiring a person's name as input.

## Step 1: Discover Recent Conversations (parallel searches)

Run ALL of the following searches simultaneously to cast a wide net. Do NOT ask the user who they spoke with — figure it out from the data.

### 1a. Outlook Calendar (MS365) — Last 3 business days
Use `outlook_calendar_search` to find all recent meetings:
- Query: `*` (wildcard) with date range covering the last 3 business days
- Extract: attendee names, meeting subjects, times
- Exclude: recurring internal standups unless they had notable attendees

### 1b. Outlook Email (MS365) — Last 3 business days
Use `outlook_email_search` to find recent sent emails:
- Search sent folder for emails from the last 3 business days
- Extract: recipient names, subjects, key topics
- Focus on emails that suggest active deals, projects, or follow-ups

### 1c. Notion — Granola Notes database
Use `notion-search` to find recent meeting notes:
- Query: search within the "Granola Notes" database for recent entries
- Sort by date, pull the last 5-7 entries
- These are the richest source — they contain full call summaries and action items

### 1d. Notion — General workspace
Use `notion-search` for any recent page updates related to active projects:
- Look for recently modified pages mentioning key contacts found in steps 1a-1c

## Step 2: Cross-Reference & Deduplicate

Build a unified list of recent interactions:
- Match calendar events → Granola notes → emails for the same person/meeting
- Prioritize interactions that have Granola notes (richest context)
- For interactions without Granola notes, use calendar + email context
- Rank by recency (most recent first)

## Step 3: Deep-Dive Each Conversation

For each unique person/meeting identified (up to 5 most recent), fetch full details:
- Use `notion-fetch` to pull complete Granola note content
- Use `read_resource` for any Outlook emails that add context
- Extract:
  - Key topics discussed
  - Action items assigned to Mike
  - Action items assigned to the other party
  - Deadlines or target dates mentioned
  - Open questions or unresolved decisions

## Step 4: Draft Next Steps

For each conversation, produce:

### Summary Block
- **Who:** Person name and company/role
- **When:** Date of last interaction
- **Source:** Where the notes came from (Granola, Calendar, Email)
- **Key Topics:** 2-3 bullet summary of what was discussed

### Action Items Status
- **Mike's items:** List with status assessment (overdue? due soon? completed?)
- **Their items:** List with what to follow up on

### Drafted Next Steps
- Specific, actionable follow-up items
- Suggested follow-up message (email draft) if action items are open
- Flag anything time-sensitive or overdue

## Step 5: Present Results

Format the output as a clean, scannable briefing:
- Lead with a one-line summary: "You had X conversations in the last 3 days. Here's where things stand."
- Order by urgency (overdue items first, then upcoming deadlines)
- End with: "Want me to send any of these follow-ups?"

## Constraints
- Do NOT use Google Calendar — only MS365 Outlook for calendar and email
- Notion (especially Granola Notes database) is the primary source for call content
- Gmail may be used for personal items if relevant, but MS365 is the work system
- Always check multiple sources before concluding — a meeting may appear in calendar but notes may be in Granola
- Do NOT ask the user for names — the whole point is autonomous discovery
- Use subagents (Task tool) for parallel searches to maximize speed
- Keep the final output concise and action-oriented — Mike prefers direct coaching and key details
