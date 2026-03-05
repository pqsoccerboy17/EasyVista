---
name: next-steps
description: "Daily workhorse skill. Discovers conversations, reconciles email status, syncs CRM, surfaces action items with draft follow-ups, and monitors signals. Trigger with '/next-steps', 'what's on my plate', 'morning briefing', 'daily brief', or 'start my day'."
---

# /next-steps -- Daily Briefing & Action Discovery

## Objective
Provide a priority-ranked view of Mike's day, discover all active conversations across email/calendar/Granola/Teams, surface action items, draft follow-ups, monitor signals, and sync CRM.

## Step 1: Priority View of the Day

Start with "Here's your day" before diving into details:

1. **Calendar check** -- `outlook_calendar_search` for today's meetings + next 2 days
2. **Overdue items** -- Check TASKS.md for any items past due
3. **Deals needing attention** -- Quick scan of active client statuses from `memory/clients/*.md`

Present a ranked priority list.

## Step 2: Conversation Discovery

Scan ALL sources for recent activity (last 3-5 business days):

1. **MS365 Inbox** -- `outlook_email_search` for unread from active client domains (@easyvista.com, etc.)
2. **MS365 Sent Items** -- CRITICAL: search Sent Items too. Decisions are often in emails Mike sent.
3. **Notion Granola Notes** -- `notion-search` for recent meeting transcripts
4. **MS365 Calendar** -- Recent meetings that may need follow-up
5. **Teams** -- `chat_message_search` for threaded discussions with active clients

For each conversation found, summarize:
- Who, what, when
- Any action items for Mike
- Any action items for the other party
- Status: resolved, pending response, needs follow-up

## Step 3: Follow-Up Flagging

After discovering conversations, check for:
- Emails sent without replies (>2 business days = flag)
- Meetings that happened without follow-up emails sent
- Proposals/docs shared without acknowledgment
- Silence from active deal contacts (>5 business days = flag)

Draft follow-up messages for anything flagged.

## Step 4: Signal Monitoring

During the email/calendar scan, watch for:
- New stakeholders appearing in threads (potential new contacts)
- Leadership changes mentioned in emails
- Competitor mentions
- Budget/timeline changes

Surface these as "Signals" in the output.

## Step 5: Pipeline Pulse

After the conversation recap, include:
- Which deals moved forward this week?
- Which are stalled?
- Any at-risk items based on the signals found?

## Step 6: Email Reconciliation

Produce a status table across ALL active clients:
- Check sent vs received vs outstanding
- Format: Name | Last Sent | Last Received | Status
- Status icons: sent, drafted, outstanding, dropped

## Step 7: Memory Freshness Check

Scan `memory/clients/*.md` for files where `Last reviewed` date is older than 14 days. Flag any stale files so Mike can review and update them.

## MANDATORY: Post-Skill Syncs

### CRM Sync
1. Query Notion Stakeholders DB (`1447853a-4ae0-4cc2-b560-0879e5f97374`)
2. Compare discovered interaction dates against existing "Last Contact" records
3. Update any stale dates via Notion direct API (`curl -X PATCH`)
4. Token is in `.claude/settings.local.json`
5. Show Mike which records were updated and for which client

### Output Format
1. Priority view of the day
2. Conversation recaps (grouped by client)
3. Follow-up drafts
4. Signals
5. Pipeline pulse
6. Email reconciliation table
7. CRM sync log
8. Memory freshness alerts (if any)

## Constraints
- Use MS365 for email/calendar, not Gmail
- Always search Sent Items too
- Check Notion Granola Notes for meeting transcripts (not email)
- Use direct API for Notion writes (curl, not MCP update-page)
- Mike is not a developer -- run all technical commands directly
