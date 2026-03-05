---
name: call-prep
description: "Pre-meeting briefing with attendee research, account context, and suggested agenda. Trigger with '/call-prep [company or person]', 'prep me for my call with [name]', 'get me ready for [meeting]'."
---

# /call-prep -- Pre-Meeting Briefing

## Objective
Prepare Mike for an upcoming meeting with comprehensive context, attendee research, and a suggested agenda.

## Step 1: Identify the Meeting

If a company or person is provided, look up the meeting:
1. `outlook_calendar_search` for upcoming meetings matching the name
2. If multiple matches, ask Mike which one

If no name provided, check today's calendar and ask which meeting to prep for.

## Step 2: Attendee Research

For each attendee on the meeting:
1. Check `contacts/` for existing profiles
2. Check Notion Stakeholders DB for records
3. If unknown attendee: run quick web/Clay lookup for title, role, LinkedIn

Summarize each attendee:
- Name, title, role
- Last interaction (from email/Notion)
- Key context (what they care about, any open items)

## Step 3: Account Context

Pull context from the relevant client:
1. Read `memory/clients/[client].md` for engagement overview
2. Check recent email threads (`outlook_email_search` -- Inbox AND Sent Items)
3. Check Notion Granola Notes for recent meeting transcripts with this client
4. Review `clients/[client]/config.json` if it exists (for project status)

Summarize:
- Current engagement status
- Recent developments
- Open items / blockers
- Any commitments Mike made in recent emails

## Step 4: Suggested Agenda

Based on the context gathered, suggest:
1. **Opening** -- What to lead with (recent win, shared context)
2. **Key topics** -- 3-5 items based on open items and recent developments
3. **Questions to ask** -- Specific, insight-driven questions
4. **Next steps to propose** -- What should come out of this meeting

## Step 5: Briefing Output

Present a concise, scannable briefing:
- Meeting details (date, time, attendees)
- Attendee profiles (2-3 lines each)
- Account context summary
- Suggested agenda
- Talking points and questions

## Constraints
- Use MS365 for email/calendar, not Gmail
- Always search Sent Items too
- Check Notion Granola Notes for meeting transcripts (not email)
- Mike is not a developer -- run all technical commands directly

## Flywheel: Outcome Tracking

At the end of this skill run, append one line to `memory/feedback/skill-outcomes.md`:
```
## YYYY-MM-DD
- /call-prep | [time] | [SUCCESS/REVISED/FAILED] | [brief description]
```
- SUCCESS: Ran without Mike correcting the output
- REVISED: Mike corrected the output (note what was changed)
- FAILED: Skill couldn't complete or was abandoned

## Flywheel: Context Enrichment

After researching attendees:
- **Unknown attendee found** -> Flag: "Unknown attendee: [name]. Run /new-contact after the meeting?"
- **New info on known contact** -> Update their contact profile with latest title/role if changed
- **Contact interaction** -> Append to attendee contact profiles: `- YYYY-MM-DD: Call prep researched for [meeting name]`

## Flywheel: Skill Chain Suggestions

At the end of this skill run, suggest:
- "After the meeting, want me to draft a follow-up with /outreach [attendee]?"
- If unknown attendees found: "Want to profile [name] with /new-contact?"

## Flywheel: Skill Output Handoff

After completing, overwrite `memory/context/last-skill-output.md`:
```
# Last Skill Output
- Skill: /call-prep
- Ran: YYYY-MM-DD HH:MM
- Key outputs: [summary]
- Suggested next: [from chain suggestions above, or "none"]
```
