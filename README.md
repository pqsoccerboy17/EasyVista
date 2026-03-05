# Mycel

Operations hub for Mike Duncan's consulting practice at Yelin.io. This repo manages client engagements, contact profiles, research artifacts, and project automation through Claude Code skills and MCP integrations.

## Active Clients

| Client | Status | Folder |
|--------|--------|--------|
| **EasyVista** | Q1 2026 engagement (Lemlist, Loopio, Tech DD) | `clients/easyvista/` |
| **Eurazeo** | AI Hackathon proposal in progress | `clients/eurazeo/` |
| **Greenridge Growth** | Exploratory - relationship building | `clients/greenridge-growth/` |
| **TBI** | Proposal stage | `clients/TBI/` |

## Folder Structure

```
Mycel/
├── CLAUDE.md              # System playbook (how Claude operates here)
├── TASKS.md               # Active task tracking
├── .claude/skills/        # Consolidated Claude Code skills
├── memory/
│   ├── clients/           # Client context files (one per client)
│   ├── companies/         # Company research artifacts
│   └── context/tools.md   # Integration config (MS365, Notion, Clay, etc.)
├── contacts/              # Contact profiles (all clients)
├── templates/             # Reusable templates and checklists
└── clients/               # Client deliverables (one subfolder per engagement)
```

## Key Skills

- `/next-steps` -- Daily briefing, conversation discovery, follow-up flagging
- `/new-contact` -- Research + enrich + save contact profile
- `/call-prep` -- Pre-meeting briefing with attendee research
- `/research` -- Deep company/person research with HTML dossier output
- `/outreach` -- Personalized email/LinkedIn drafts
- `/pipeline` -- Deal health, forecasting, stage review
- `/update-project` -- Full project sync (config -> timeline -> git -> Notion)
- `/new-client` -- New client onboarding (folder, memory, contacts)

## Integrations

- **Email/Calendar:** Microsoft 365 (Outlook) - michael@yelin.io
- **CRM:** Notion Stakeholders DB
- **Enrichment:** Clay
- **Meeting Notes:** Granola (auto-syncs to Notion)
- **Research:** NotebookLM

## Full Playbook

See [CLAUDE.md](CLAUDE.md) for the complete operational playbook governing how Claude works in this repo.
