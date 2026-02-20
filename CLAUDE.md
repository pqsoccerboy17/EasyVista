# Mycel.io — Consulting Operations Playbook

This is the system-level playbook for Mike Duncan's consulting practice at Mycel.io. It governs how Claude operates across ALL client engagements.

## Workspace Structure

```
mycel/                          ← This repo (always open in Cowork or Claude Code)
├── CLAUDE.md                       ← You are here — system playbook
├── TASKS.md                        ← Active task tracking
├── .claude/
│   ├── settings.local.json         ← API tokens (gitignored)
│   └── skills/                     ← All consolidated skills
├── memory/
│   ├── clients/                    ← Client context files (one per client)
│   ├── people/                     ← Contact profiles
│   ├── companies/                  ← Company research artifacts
│   └── context/
│       └── tools.md                ← Connectors, API patterns, Notion IDs
├── contacts/                       ← Contact markdown files (cross-client)
├── templates/                      ← Reusable templates (intake, SOW, etc.)
└── clients/                        ← Client deliverables (one subfolder per client)
    └── easyvista/                  ← EasyVista project files, config.json, portal, etc.
```

## Client Context

Client-specific details live in `memory/clients/`. Always check the relevant client file before working on client-specific tasks. Client deliverables and project files live in `clients/[client]/`.

→ **Active clients:** [memory/clients/](memory/clients/)
→ **Client deliverables:** [clients/](clients/)
→ **Contact profiles:** [contacts/](contacts/) and [memory/people/](memory/people/)
→ **Tool config:** [memory/context/tools.md](memory/context/tools.md)

## Connectors & Tools

> Full details: [memory/context/tools.md](memory/context/tools.md)

**Default Connectors:**
- **Email:** Microsoft 365 (Outlook) — `michael@yelin.io`
- **Calendar:** Microsoft 365 (Outlook) — `michael@yelin.io`
- **Database/CRM:** Notion — Stakeholders DB (`1447853a-4ae0-4cc2-b560-0879e5f97374`)
- **Chat:** Microsoft Teams
- **Meeting Notes:** Granola → auto-syncs to Notion "Granola Notes" database
- **Enrichment:** Clay (contact/company enrichment)

**Notion Access (two paths):**
- **Cowork MCP connector** — Use for search, fetch, create-pages
- **Direct API** (token in `.claude/settings.local.json`) — Use for page updates (PATCH). The MCP `update-page` tool has a known param bug; always use `curl -X PATCH` for writes.

**When running any skill:**
- Always use O365 tools (`outlook_email_search`, `outlook_calendar_search`) instead of Gmail/GCal
- **CRITICAL: Search Sent Items too** — Critical decisions are often in emails Mike sent
- Pull pipeline data from Notion when available
- Check Notion "Granola Notes" for meeting transcripts (not email)
- **Mike is not a developer** — always run git/technical commands for him, don't just show them

## Consolidated Skills (10 max — HARD CAP)

These are the ONLY workflow skills to use. If a loaded plugin offers a skill not on this list, IGNORE it and use the consolidated version instead.

### Daily Workflow
| # | Skill | What it does |
|---|-------|-------------|
| 1 | **`/next-steps`** | The daily workhorse. Discovers conversations (email, calendar, Granola, Teams), reconciles email status (sent/received/outstanding), syncs Last Contact dates to Notion, surfaces action items with draft follow-ups. Replaces: daily-briefing, follow-up-automation, smart-follow-up, signal-monitor, pipeline-management. |
| 2 | **`/new-contact`** | Research + Clay enrich + save profile + add to Notion Stakeholders DB. |
| 3 | **`/call-prep`** | Pre-meeting briefing with attendee research, account context, and suggested agenda. Replaces: meeting-prep. |

### Deal & Account Work
| # | Skill | What it does |
|---|-------|-------------|
| 4 | **`/research`** | Deep dive on a company or person — competitive intel, ICP fit, assessment generation. Replaces: account-research, competitive-intelligence, icp-qualification, assessment-generation. |
| 5 | **`/outreach`** | Draft personalized emails, LinkedIn messages, or multi-touch sequences. Replaces: draft-outreach, email-sequences, linkedin-engagement. |
| 6 | **`/pipeline`** | Deal health, forecasting, stage review, negotiation strategy, win/loss analysis. Replaces: pipeline-review, forecast, deal-room, negotiation-playbook, roi-calculator, win-loss-analysis, sales-coach. |

### Project Management
| # | Skill | What it does |
|---|-------|-------------|
| 7 | **`/update-project`** | Full project sync — config.json → timeline artifacts → git push → Notion. |

### Document Creation (auto-trigger — you never type these)
| # | Skill | Triggers when... |
|---|-------|-----------------|
| 8 | **`/docx`** | "Write a report", "create a proposal", "draft a memo" → Word doc. Absorbs: proposal-drafting, create-an-asset (doc). |
| 9 | **`/pptx`** | "Make a deck", "create a presentation" → PowerPoint. Absorbs: create-an-asset (deck). |
| 10 | **`/xlsx`** | "Build a spreadsheet", "create a tracker" → Excel. |

### Utility Skills (outside the cap — builder toolkit)
These are tools for building tools. Keep available but not part of the daily workflow:
- `skill-creator` — Build/modify skills
- `cowork-plugin-customizer` — Customize plugins for clients
- `create-cowork-plugin` — Scaffold new plugins
- `schedule-task` / `create-shortcut` — Automation scheduling
- `pdf` — PDF manipulation when needed

### IGNORED Skills (do not use)
All `customer-support:*` skills, `sales:daily-briefing`, `sales:follow-up-automation`, `sales:smart-follow-up`, `sales:signal-monitor`, `sales:meeting-prep`, `sales:demo-showcase`, `sales:deal-workflow-orchestrator`, `sales:email-sequences`, `sales:linkedin-engagement`, `sales:stakeholder-mapping`, `sales:pipeline-management`, `sales:proposal-drafting`, `sales:create-an-asset`, `sales:icp-qualification`, `sales:assessment-generation`, `sales:competitive-intelligence`, `sales:negotiation-playbook`, `sales:roi-calculator`, `sales:win-loss-analysis`, `sales:sales-coach`, `sales:deal-room`, `productivity:memory-management`, `productivity:task-management`.

## `/next-steps` Enhanced Behavior

The base `/next-steps` skill handles conversation discovery and action drafting. These CLAUDE.md instructions extend it with capabilities absorbed from 5 other skills:

**From daily-briefing:** Start with a priority-ranked view of the day — today's calendar, overdue items, deals needing attention. Lead the output with "here's your day" before diving into conversation recaps.

**From follow-up-automation + smart-follow-up:** After discovering conversations, check for:
- Emails sent without replies (>2 business days = flag)
- Meetings that happened without follow-up emails sent
- Proposals/docs shared without acknowledgment
- Any silence from active deal contacts (>5 business days = flag)
Draft follow-up messages for anything flagged.

**From signal-monitor:** During the email/calendar scan, watch for:
- New stakeholders appearing in threads (potential new contacts)
- Leadership changes mentioned in emails
- Competitor mentions
- Budget/timeline changes
Surface these as "signals" in the output.

**From pipeline-management:** After the conversation recap, include a pipeline pulse:
- Which deals moved forward this week?
- Which are stalled?
- Any at-risk items based on the signals found?

## MANDATORY: Post-Skill Syncs

### After `/next-steps` runs:
1. **Sync CRM fields** — Query Notion Stakeholders DB, compare discovered interaction dates against existing records, update any stale "Last Contact" dates or other fields defined in the client context file via Notion direct API
2. **Reconcile email status** — Check sent vs received vs outstanding across ALL active clients, produce status table (✅ sent, ⚠️ drafted, 🔲 outstanding, ❌ dropped)
3. **Log changes** — Show Mike which Notion records were updated and for which client

### After `/update-project` runs:
1. **Same CRM sync** as above for the specific client's stakeholders
2. **Git push** — Commit and push changes per the client's git config (see `memory/clients/[client].md`)

### After any Notion write:
- Use direct API (`curl -X PATCH`) — never the MCP `update-page` tool
- Token is in `.claude/settings.local.json`
- See `memory/context/tools.md` for the full API patterns and database IDs

```bash
curl -s -X PATCH "https://api.notion.com/v1/pages/{page_id}" \
  -H "Authorization: Bearer {NOTION_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{"properties":{...}}'
```

## Task Tracking

- **TASKS.md** — Active task file, updated throughout each session
- **Status icons:** ✅ done, ⚠️ drafted/in-progress, 🔲 ready/outstanding, ❌ removed/dropped
- Drafted-but-unsent items are NEVER marked ✅ — always ⚠️

## Lessons Learned

1. **Always check Sent Items** — Critical decisions are often in emails Mike sent, not received
2. **Granola syncs to Notion** — Don't search email for meeting notes; check Notion "Granola Notes"
3. **Verify ownership before acting** — Cross-reference meeting notes to confirm who owns action items (Mike vs client)
4. **Notion writes use direct API** — MCP `update-page` has a param bug; use curl
5. **Notion token in `.claude/settings.local.json`** — If 401, token expired → Mike regenerates at notion.so/profile/integrations
6. **Don't assume info is missing** — Check Granola notes before asking Mike for details he may have already provided in a meeting
7. **Client deliverables in `clients/[name]/`** — Never put client-specific files at root level. Root is for ops infrastructure only.
8. **Skills are client-agnostic** — They pull client context from `memory/clients/`. Never hardcode client names or paths in skill files.
9. **One repo, both Macs** — This workspace syncs via GitHub. `git push` here, `git pull` on the other machine. Both Cowork and Claude Code work from this folder.
