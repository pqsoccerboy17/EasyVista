# Plan: `/update-project` Skill

## What It Does
A single on-demand command (`/update-project`) that pulls all data sources, updates the EasyVista project timeline, sanitizes customer-facing content, syncs to Notion, flags stale stakeholders, and pushes to both GitHub remotes — the full update cycle we just did manually, plus new capabilities.

## Skill Location
`/sessions/gracious-hopeful-heisenberg/mnt/.local-plugins/marketplaces/local-desktop-app-uploads/sales/skills/update-project/`

This keeps it alongside the other sales skills in the same plugin directory.

## Files to Create

### 1. `SKILL.md` — Main skill prompt (~200 lines)
The core instruction set, structured in 6 phases:

**Phase 1: Data Gathering (parallel)**
- Outlook email (Inbox + Sent Items, last 7 days) for EasyVista threads
- Outlook calendar for upcoming EasyVista meetings (next 30 days)
- Notion Granola Notes for recent meeting transcripts (last 7 days)
- MS Teams chat for EasyVista threads
- Read current `config.json` to understand baseline state

**Phase 2: Analysis & Diff**
- Compare gathered data against current config.json
- Identify: new milestones, task completions, stakeholder status changes, new risks, resolved questions
- Build a structured "change set" before touching any files

**Phase 3: Update config.json**
- Apply all identified changes to config.json (source of truth)
- Update `meta.last_updated` timestamp
- Present the change set summary to user for confirmation before proceeding

**Phase 4: Regenerate & Sanitize**
- Run `python3 generate_timeline.py`
- Scan ALL output files for customer-facing sensitivity:
  - Specific dollar amounts / pricing
  - Individual names in negative context (e.g., "Rod bypassing X")
  - Internal strategy language ("investor narrative", "capital raise")
  - Shadow IT references
  - Consultant-internal notes
- Auto-fix common patterns, flag ambiguous ones for user review

**Phase 5: Stale Stakeholder Alerts** (NEW)
- Compare each stakeholder's last known interaction date against today
- Flag anyone with no contact in 7+ days
- Cross-reference with upcoming calendar to check if meetings are already booked
- Output a prioritized "follow-up needed" list with suggested actions

**Phase 6: Sync & Deploy**
- Notion sync: Update the EasyVista project page in Notion with latest status
- Git: commit all changes with descriptive message
- Git: push to `origin` (dev) and `production` (client-facing)
- If push fails (SSH key issue), output the exact commands for user to run locally

### 2. `references/sanitization-rules.md` (~50 lines)
Customer-facing content rules that the skill checks against:
- Grep patterns for sensitive terms
- Replacement templates
- What's OK vs. what needs scrubbing

### 3. `references/data-sources.md` (~40 lines)
Quick reference for all MCP tool names, search parameters, and folder conventions so the skill doesn't have to re-discover them each time.

## How It Triggers
- User says `/update-project` or "update the project" or "sync everything" or "pull latest"
- Skill description will be written to trigger aggressively on these phrases

## Key Design Decisions

1. **Confirmation gate after Phase 3** — The skill shows you the proposed changes before regenerating/pushing. This prevents bad data from going live.

2. **Sanitization is automated, not manual** — We encode the patterns we fixed today (pricing, names-in-negative-context, internal strategy) as grep-able rules so the skill catches them every time.

3. **Stale stakeholder detection** — Uses config.json stakeholder notes (which contain dates) plus calendar/email data to calculate last contact. This is net-new functionality beyond what we did manually.

4. **Notion sync** — After GitHub is updated, push a summary to the EasyVista page in Notion so the team can see status without visiting the GitHub Pages site.

5. **Graceful git failure handling** — If SSH keys aren't available, the skill outputs the exact `git push` commands instead of failing silently.

## What's NOT in Scope (yet)
- Auto-scheduling (you chose on-demand only)
- generate_timeline.py improvements (the hardcoded HTML sections like risks table, task tables, budget gauge are not auto-updated by the script — that's a separate enhancement)
- Automated Notion → config.json bidirectional sync (currently one-directional: config.json is source of truth)

## Implementation Steps
1. Create skill directory and SKILL.md
2. Create references/sanitization-rules.md
3. Create references/data-sources.md
4. Test the skill with a dry run
5. Verify it triggers correctly on `/update-project`
