---
name: monthly-report
description: "Monthly compounding proof. Measures intelligence growth, skill trends, client maturity changes, and accumulated knowledge. Trigger with '/monthly-report', 'monthly review', 'how did this month go', or 'show me the flywheel'."
---

# /monthly-report -- Monthly Intelligence Compounding Report

## Objective
Prove that the system is getting smarter. Measure session volume, skill performance trends, client maturity progression, and accumulated intelligence capital.

## Step 1: Gather Month's Data

Read all available data:
1. `memory/sessions/*.md` -- all session logs from the current month
2. `memory/feedback/skill-outcomes.md` -- all entries from the month
3. `memory/feedback/pending-rules.md` -- applied rules this month
4. `memory/feedback/cross-client-patterns.md` -- pattern growth
5. `memory/clients/*.md` -- current vs. start-of-month maturity
6. CLAUDE.md Lessons Learned -- total count and new additions

## Step 2: Session Volume

- Total sessions this month
- Average skills per session
- Most active days
- Longest session (by skill count)

## Step 3: Skill Performance Trends

- Success rate by skill (compare to prior month if data exists)
- Most-used skills
- Skills with improving success rate
- Skills with declining success rate (need attention)

## Step 4: Client Maturity Progression

For each client:
- Maturity at start of month vs. now
- Contacts profiled this month
- Key intelligence gathered
- Engagement depth (skill runs against this client's context)

## Step 5: Intelligence Capital

Accumulated knowledge the system now has:
- Total lessons learned
- Total cross-client patterns
- Total contact profiles
- Total client memory files
- Total session logs (institutional memory)
- Rules auto-applied vs. corrections still needed (efficiency trend)

## Step 6: Highlights and Recommendations

- Top 3 intelligence gains this month
- Top 3 areas needing improvement
- Recommended focus for next month
- Any skills that should be modified based on performance data

## Step 7: Report Output

Present as a structured report:

```
# Monthly Intelligence Report -- [Month Year]

## Summary
[2-3 sentence overview of the month]

## Session Activity
- Sessions: [count]
- Skills run: [count]
- Skills per session: [average]

## Skill Performance
[table: skill | runs | success% | trend]

## Client Maturity
[table: client | start | end | delta]

## Intelligence Capital
- Lessons learned: [total] (+[new this month])
- Cross-client patterns: [total] (+[new])
- Contact profiles: [total]
- Session logs: [total]

## Highlights
[top 3 gains]

## Focus Areas
[top 3 improvements]

## The Flywheel
[1-2 sentences on how the system improved this month]
```

## Step 8: Save and Commit

1. Save the report to `memory/sessions/YYYY-MM-monthly-report.md`
2. Commit:
   ```
   docs: monthly report [Month Year] -- [summary]

   Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
   ```

## Constraints
- Be honest about metrics -- don't inflate success rates
- If this is the first month, note the baseline and skip trend comparisons
- Keep the report scannable -- Mike should grasp the picture in 30 seconds
- Offer to create a shareable artifact (deck/doc) if Mike wants to share with Henry/Russell
