---
name: review-week
description: "Weekly intelligence digest. Analyzes session logs, skill outcomes, and patterns to extract rules, update maturity scores, and compound learning. Trigger with '/review-week', 'weekly review', 'week in review', or 'how did this week go'."
---

# /review-week -- Weekly Intelligence Digest

## Objective
Analyze the past week's sessions to find patterns, extract new rules, update client intelligence maturity, and measure system improvement. This is where corrections become permanent intelligence.

## Step 1: Gather Week's Data

Read all available data sources:
1. `memory/sessions/*.md` -- last 5-7 session logs
2. `memory/feedback/skill-outcomes.md` -- all entries from this week
3. `memory/feedback/pending-rules.md` -- any unapplied corrections
4. `memory/feedback/cross-client-patterns.md` -- existing patterns
5. `memory/clients/*.md` -- current client states

## Step 2: Skill Usage Stats

Analyze skill-outcomes.md for the week:
- Total skill runs
- Breakdown by skill (which ran most)
- Success rate per skill (SUCCESS vs REVISED vs FAILED)
- Which skills had the most corrections

Present as a scannable table.

## Step 3: Pattern Detection

Look for recurring patterns:
- **Same correction 2+ times** = propose a new rule
  - Check if it's already in Lessons Learned (CLAUDE.md) or cross-client-patterns.md
  - If new, draft the rule with source citation
- **Skill chains that happened naturally** = validate or add to chain table
- **Client-specific patterns** = update the relevant client memory
- **Cross-client patterns** = update cross-client-patterns.md

## Step 4: Propose Changes

For each detected pattern, present:
```
Proposed Rule: "[rule text]"
Source: [X] corrections across [Y] sessions
Target: [file to update]
Apply? [wait for Mike's approval]
```

Apply approved changes immediately. Move to Applied in pending-rules.md.

## Step 5: Update Client Intelligence Maturity

For each active client, recalculate:
- Contacts profiled: [count with profiles] / [total known]
- Last /next-steps: [date]
- Last /update-project: [date]
- Research dossier: YES/NO
- Maturity level: NASCENT / DEVELOPING / MATURE / EXEMPLARY

Maturity criteria:
- NASCENT: <25% contacts profiled, no research dossier
- DEVELOPING: 25-60% contacts, some skill usage
- MATURE: >60% contacts, research dossier, regular skill usage
- EXEMPLARY: >80% contacts, research dossier, weekly updates, cross-referenced intelligence

Update each client memory file's Intelligence Maturity section.

## Step 6: Update Lessons Learned

If new rules were approved in Step 4, add them to CLAUDE.md Lessons Learned with source citation:
```
[N]. **[Rule]** -- [brief explanation].
    (Source: [X] corrections, [Y] weeks. Applied YYYY-MM-DD)
```

## Step 7: Weekly Digest Output

Present a scannable digest:

```
# Week in Review -- [date range]

## Skill Performance
[table from Step 2]

## Patterns Detected
[from Step 3]

## Rules Applied
[from Step 4]

## Client Maturity
[from Step 5]

## Intelligence Growth
- New rules this week: [count]
- Total lessons learned: [count]
- Cross-client patterns: [count]
```

## Step 8: Commit Changes

Stage and commit any files updated during the review:
```
docs: weekly review [date range] -- [summary]

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

## Constraints
- Never auto-apply rules without Mike's approval
- Cite sources for every proposed rule
- Keep the digest scannable -- no walls of text
- If there aren't enough sessions to analyze, say so and suggest running more
