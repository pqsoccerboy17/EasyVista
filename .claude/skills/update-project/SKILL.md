---
name: update-project
description: "Full client project update — pulls Outlook email/calendar, Notion Granola Notes, and Teams, then updates config.json, regenerates all timeline artifacts, sanitizes customer-facing content, flags stale stakeholders, syncs to Notion, and pushes to GitHub. Trigger with /update-project, 'update the project', 'sync everything', 'pull latest', 'refresh the timeline', or 'update all sites'."
---

# Client Project Update — Full Sync Workflow

You are performing a complete project status update for a consulting engagement. This is Mike Duncan's (michael@yelin.io) config-driven static timeline workflow.

## Before You Start

1. **Determine which client** — If Mike specifies (e.g., "update EasyVista"), use that. If ambiguous, check `memory/clients/` for active engagements and ask.
2. Read the client context file at `memory/clients/[client].md` for key people, architecture, and current state.
3. Read reference files in this skill directory:
   - `references/data-sources.md` — MCP tool names and search parameters
   - `references/sanitization-rules.md` — customer-facing content rules
4. Client deliverables live in `clients/[client]/` — that's where config.json, timeline artifacts, and generated files are.

## Phase 1: Data Gathering

Run ALL of these searches in parallel. Cast a wide net — it's better to over-fetch than miss something. Replace `[CLIENT]` with the client name/keywords from the client context file.

### 1a. Outlook Email — Inbox (last 7 days)
Search for "[CLIENT]" in Inbox using `outlook_email_search`:
- `query`: "[CLIENT]"
- `afterDateTime`: 7 days ago
- `limit`: 20

### 1b. Outlook Email — Sent Items (last 7 days)
Same search but in Sent Items. Mike's sent emails often contain critical decisions:
- `query`: "[CLIENT]"
- `afterDateTime`: 7 days ago
- `folderName`: "Sent Items"
- `limit`: 15

### 1c. Outlook Calendar — Upcoming meetings (next 30 days)
Search for client meetings using `outlook_calendar_search`:
- `query`: "[CLIENT] OR Yelin OR [key tool names from client context]"
- `afterDateTime`: today
- `beforeDateTime`: 30 days from now
- `limit`: 20

### 1d. Notion — Granola Notes (last 7 days)
Search Notion using `notion-search`:
- `query`: "[CLIENT] Granola Notes"
- `query_type`: "internal"
- `filters`: created_date_range with start_date = 7 days ago
For each result, use `notion-fetch` to pull the full meeting note content.

### 1e. MS Teams Chat (last 7 days)
Search Teams using `chat_message_search`:
- `query`: "[CLIENT]"
- `afterDateTime`: 7 days ago
- `limit`: 15

### 1f. Current State
Read the current `clients/[client]/config.json`. Note the `meta.last_updated` timestamp — everything since that date is new context.

## Phase 2: Analysis & Change Set

Compare gathered data against config.json and build a structured change set. Look for:

### Milestones
- New events that should be tracked (meetings that happened, decisions made, deliverables completed)
- Existing milestones that can now be marked `"complete": true`
- Upcoming meetings from calendar that should be added

### Task Status Updates
- Tasks in workstream phases that have been completed (evidence from email/notes)
- Tasks with shifted due dates
- New tasks that emerged from recent conversations

### Stakeholder Status Changes
The 5-state model: `cold` → `outreach_sent` → `scheduled` → `engaged` → `risk`
- Who was contacted since last update? (outreach_sent → scheduled or engaged)
- Who responded or attended meetings? (→ engaged)
- Any new stakeholders mentioned in emails/notes?
- Anyone showing resistance? (→ risk, but phrase diplomatically)

### Risks & Open Questions
- New risks identified in conversations
- Open questions that got resolved (prefix with "RESOLVED:")
- New open questions raised

### Present Change Set to User
Before editing any files, present a concise summary:
```
## Proposed Updates
**Milestones:** [list new/completed]
**Tasks:** [list status changes]
**Stakeholders:** [list status changes]
**Risks:** [new/resolved]
**Open Questions:** [new/resolved]

Proceed with these updates?
```
Wait for user confirmation. If they want changes, adjust before proceeding.

## Phase 3: Update config.json

Apply the confirmed change set to `clients/[client]/config.json`:
1. Update `meta.last_updated` to current ISO timestamp
2. Apply all milestone additions/completions
3. Apply all task status updates
4. Apply all stakeholder status changes and notes
5. Apply risk and open question changes
6. Validate JSON is well-formed after editing

Only edit config.json — never edit derivative files directly.

## Phase 4: Regenerate & Sanitize

### Regenerate
Run the generator from the client directory:
```bash
cd clients/[client] && python3 generate_timeline.py
```
This updates the mermaid diagrams, timeline markdown, and index.html.

### Sanitize Customer-Facing Content
See `references/sanitization-rules.md` for the full pattern list. Key categories:
- **Pricing/budget specifics**: Dollar amounts, specific contract terms
- **Individual names in negative context**: "X bypassing Y", "X refusing to use Y"
- **Internal strategy language**: "investor narrative", "capital raise", "fundraising"
- **Shadow IT references**: "using ChatGPT instead of", "100x/day"
- **Consultant-internal notes**: Budget gauges, stretch targets

For each match:
- If it's in config.json: rewrite the note diplomatically
- If it's in index.html hardcoded sections: edit directly with neutral language
- If it's in generated files: fix in config.json, re-run generator

## Phase 5: Stale Stakeholder Alerts

For each stakeholder in config.json, determine last known interaction:
1. Check stakeholder notes for dates mentioned
2. Cross-reference with recent email/calendar data from Phase 1
3. Check if any upcoming meetings are booked with them

Flag stakeholders who meet ANY of these criteria:
- No email/calendar interaction in last 7 days AND status is "engaged" or "scheduled"
- Status is "outreach_sent" for more than 5 business days with no response
- Status is "cold" and they're in an active workstream

## Phase 6: Sync & Deploy

### 6a. Notion Sync
Search Notion for the client project page. If found, update it with a brief status summary.

### 6b. Notion Stakeholders — Last Contact Sync
Query the Stakeholders DB, compare discovered interaction dates against existing Last Contact values, and update any stale records via direct API (curl -X PATCH). See CLAUDE.md for the sync procedure.

### 6c. Git Commit
Stage all modified files in the client directory and commit:
```bash
git add clients/[client]/
git commit -m "update: [date] [client] project status sync

[2-3 line summary of key changes]

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

### 6d. Git Push
Push to the appropriate remote(s). Check the client context file for which remotes apply.

If push fails (SSH key issues, permission denied), output the exact commands Mike needs to run from his local terminal.

### 6e. Final Summary
Present a concise update report:
- What changed (milestone count, task completions, stakeholder moves)
- Stale stakeholder alerts (from Phase 5)
- Upcoming critical dates
- Any items that need Mike's attention

## Important Reminders
- config.json is the ONLY file you edit directly — everything else is generated
- Always search Sent Items in Outlook — Mike's decisions live there
- Granola Notes are in Notion, not email — don't confuse the sources
- Customer-facing sites may be visible to client stakeholders — be mindful of what goes on them
- Mike is not a developer — run all git commands for him, don't just show them
- Client-specific context lives in `memory/clients/[client].md` — always read it first
