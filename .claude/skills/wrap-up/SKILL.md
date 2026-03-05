---
name: wrap-up
description: "Session-close intelligence capture. Generates session log, captures corrections, updates memory, commits and pushes. Replaces /bye. Trigger with '/wrap-up', 'end session', 'close out', or 'that's it for today'."
---

# /wrap-up -- Session Close & Intelligence Capture

## Objective
Close the current session by capturing everything that happened -- skills used, decisions made, corrections given -- and persisting it for future sessions. This is how the flywheel turns.

## Step 1: Scan the Conversation

Review the full conversation history and extract:

### Skills Used
List every skill invoked this session with approximate time:
- Format: `- /[skill-name] ([time]) - [what it did]`

### Key Decisions
Any decisions Mike made or confirmed:
- Deferred items, approved drafts, changed direction, etc.

### Actions Taken
Concrete actions completed (emails sent, Notion updated, files created):
- Include what was changed and where

### Corrections
Any time Mike corrected Claude's output:
- Tone adjustments ("make it more casual")
- Format preferences ("use bullet points")
- Factual corrections ("that's not right, it's actually...")
- Process corrections ("check Granola first, not email")

For each correction, identify:
- The correction itself (quote it)
- The target file where this should be documented (client memory, skill file, CLAUDE.md, etc.)

### Signals Detected
New information discovered during the session:
- New stakeholders, leadership changes, competitor mentions, budget/timeline shifts

### Open Items
Anything explicitly deferred or left unfinished:
- Format: `- [item] (deferred to [when/reason])`

## Step 2: Generate Session Log

Create a session log file at `memory/sessions/YYYY-MM-DD-session.md`:

```
# Session Log - YYYY-MM-DD

## Skills Used
[from Step 1]

## Key Decisions
[from Step 1]

## Actions Taken
[from Step 1]

## Corrections
[from Step 1, with target files noted]

## Signals Detected
[from Step 1]

## Open Items Carried Forward
[from Step 1]
```

If a session log already exists for today (multiple sessions), append to it with a time separator.

## Step 3: Capture Pending Rules

For each correction found in Step 1 that is NOT already documented in the target file:
1. Read `memory/feedback/pending-rules.md`
2. Add the correction to the Pending section:
   ```
   - [YYYY-MM-DD] "[correction text]"
     - Target: [file path] -> [section]
     - Occurrences: 1
   ```
3. If the same correction already exists in Pending, increment the Occurrences count

## Step 4: Log Skill Outcomes

For each skill used this session, append to `memory/feedback/skill-outcomes.md`:
```
- /[skill] | [time] | [SUCCESS/REVISED/FAILED] | [brief description]
```
- SUCCESS = ran without corrections
- REVISED = Mike corrected the output
- FAILED = skill couldn't complete or was abandoned

## Step 5: Update Skill Handoff

Overwrite `memory/context/last-skill-output.md` with a summary of the last skill run this session.

## Step 6: Update Auto-Memory (if needed)

Check if any new quick-reference info should be added to the project MEMORY.md:
- New client status changes
- New tool issues discovered
- New user preferences expressed
- Updated dates or deadlines

Only update if there's genuinely new cross-session info. Don't bloat it.

## Step 7: Present Summary

Show Mike a concise wrap-up:
```
Session Summary:
- [X] skills run, [Y] corrections captured
- [Z] pending rules queued for next session
- [Notable items]

Open items for next session:
- [list]
```

## Step 8: Commit and Push

1. Stage all modified files (session log, feedback files, memory updates)
2. Commit with conventional message:
   ```
   docs: session log YYYY-MM-DD -- [brief summary]

   Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
   ```
3. Push to origin

## Constraints
- Never fabricate corrections -- only capture what Mike actually said
- Session logs are append-only -- never edit past sessions
- Keep the summary concise -- Mike should be able to glance and go
- If nothing happened (no skills, no corrections), say so briefly and skip the log
