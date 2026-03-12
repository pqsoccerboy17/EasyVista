# Tool Preferences & Integrations

> Last reviewed: 2026-03-11
> This file tells Claude which tools to use by default for Mycel.io consulting work.

## Email & Calendar

| Function | Tool | Account | Notes |
|----------|------|---------|-------|
| **Email (Primary)** | Microsoft 365 | michael@yelin.io | Use `outlook_email_search`, NOT Gmail |
| **Calendar (Primary)** | Microsoft 365 | michael@yelin.io | Use `outlook_calendar_search`, NOT GCal |
| **Email (Personal)** | Gmail | michaelduncan17@gmail.com | Only for personal items |

**Critical:** When running sales skills (daily-briefing, call-prep, etc.), ALWAYS:
1. Search **Sent Items** in addition to Inbox -- sent emails contain critical context
2. Use MS365 tools first, Gmail only as fallback for personal items
3. Include emails from the past 7 days minimum for full context

## Database & CRM

| Function | Tool | Workspace | Notes |
|----------|------|-----------|-------|
| **CRM/Pipeline** | Notion | "AI Sales Enablement Assessment" | Primary system of record |
| **Meeting Notes** | Granola → Notion | Auto-syncs to "Granola Notes" database | Notes appear automatically after meetings |
| **Client Timeline** | GitHub Pages + config.json | mikeduncan17.github.io/client-timelines | Visual dashboard |

**Notion Access (two paths):**
- **Notion MCP connector** -- Use for search, fetch, create-pages, AND page updates. The old Cowork MCP had a param bug on writes, but the current Claude Code Notion MCP works correctly (confirmed Mar 2026).
- **Direct API** (token in `.claude/settings.local.json`) -- Fallback if MCP fails. Token starts with `ntn_`, stored under `NOTION_API_KEY`.

**Notion API usage pattern:**
```bash
# Read a page
curl -s "https://api.notion.com/v1/pages/{page_id}" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2022-06-28"

# Update page properties
curl -s -X PATCH "https://api.notion.com/v1/pages/{page_id}" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  -d '{"properties":{"Phone":{"phone_number":"512-555-1234"}}}'
```

**Key Notion IDs:**
- Stakeholders DB: `1447853a-4ae0-4cc2-b560-0879e5f97374`
- Stakeholders data source: `d7c002ba-a914-45ea-9f33-27af8ed2fd62`

**Notion Structure:**
- `EasyVista Main` -- Hub page with workstreams, contacts, critical dates
- `Granola Notes` -- Auto-synced meeting transcripts
- `AI Sales Enablement Assessment` -- Project details
- `Stakeholders` -- Contact database (Name, Email, Phone, Role/Title, Location, LinkedIn, Relationship Strength, Stakeholder Type, Notes, Last Contact)

## Chat & Communication

| Function | Tool | Notes |
|----------|------|-------|
| **EasyVista Team** | Microsoft Teams | Search for EasyVista-related threads |
| **Internal (Mycel.io)** | Email (MS365) | Henry, Russell communications |

## File & Document Management

| Function | Tool | Location |
|----------|------|----------|
| **Shared Docs** | OneDrive/SharePoint | Via MS365 connector |
| **Local Project Files** | clients/easyvista/ | Git-tracked config.json |
| **Attachments** | MS365 email attachments | Action trackers, templates |

## Sync Workflow (EasyVista)

When updating project status, sync ALL THREE systems:

```
1. Notion (EasyVista Main)     → Primary UI for stakeholders
2. config.json                 → Source of truth for timeline
3. GitHub Pages                → Public dashboard
```

**Sync Command Pattern:**
```bash
# After updating config.json:
cd clients/easyvista/
python3 generate_timeline.py
git add . && git commit -m "Update: [description]" && git push
```

## Search Priorities

When gathering context for briefings or research:

| Priority | Source | What to Search |
|----------|--------|----------------|
| 1 | MS365 Inbox | Unread from key accounts |
| 2 | MS365 Sent Items | Recent actions/commitments I made |
| 3 | Notion | Pipeline status, meeting notes, stakeholders |
| 4 | MS365 Calendar | Today's meetings + recent meetings |
| 5 | Teams | Threaded discussions with EasyVista team |

## Key Accounts to Track

| Account | Primary Contacts | Domain |
|---------|-----------------|--------|
| **EasyVista** | Evan Carlson (COO), Patrice Barbedette (CEO), Chris Hult (RevOps) | @easyvista.com |
| **Greenridge Growth** | Andrew Bell (VP, Value Creation) | @greenridgegrowth.com |
| **TBI** | (see memory/clients/tbi.md) | TBD |
| **Mycel.io** | Henry Yelin, Russell Beggs | @yelin.io |
| **Lemlist** | Eduardo | @lemlist.com, @lempire.co |

## MS365 MCP Workflow Patterns

These are interactive workflows (Claude Code sessions), not headless automation -- the correct security model for MS365 OAuth.

### Daily Briefing
1. `outlook_email_search` -- Unread from @easyvista.com + Sent Items (last 3 days)
2. `outlook_calendar_search` -- Today's EasyVista meetings
3. `notion-search` -- Recent Granola Notes for meeting transcripts
4. Review config.json stakeholders against email activity
5. Suggest status updates if warranted

### Call Prep
1. `outlook_email_search` -- Thread history with stakeholder
2. `notion-fetch` -- Stakeholder details from Notion DB
3. Read config.json for current status/notes
4. Generate prep brief

### Post-Meeting Update
1. `notion-search` -- Find Granola meeting note
2. Extract status changes, action items, dates
3. Update config.json
4. Run `python3 generate_timeline.py`
5. Update Notion via MCP
6. Commit & push

## NotebookLM MCP Server

| Function | Tool | Notes |
|----------|------|-------|
| **Create notebook** | `notebook_create` | One per account |
| **Add sources** | `notebook_add_url`, `notebook_add_text`, `notebook_add_drive` | URLs, text, Drive docs |
| **Query notebook** | `notebook_query` | AI-powered Q&A about sources |
| **Deep research** | `research_start` → `research_status` → `research_import` | 3-5 min, web-based |
| **Generate content** | `audio_overview_create`, `slide_deck_create`, `report_create` | Requires confirm=True |
| **Check progress** | `studio_status` | Poll for generation completion |

**Auth:** Authenticated via `notebooklm-mcp-auth` (browser-based Google login). Tokens cached locally.
**Note:** 32 tools total -- significant context usage. Used primarily by `/research` skill.

## Google Workspace CLI (gws)

| Function | Command | Notes |
|----------|---------|-------|
| **List Drive files** | `gws drive files list --limit 10` | Returns file names, IDs, MIME types |
| **Search Drive** | `gws drive files list --query "name contains 'proposal'"` | Drive query syntax |
| **Download file** | `gws drive files export --file-id FILE_ID --mime-type text/plain` | Export to local |
| **List Sheets** | `gws sheets spreadsheets list --limit 5` | Spreadsheet metadata |
| **Read Sheet data** | `gws sheets spreadsheets values get --spreadsheet-id ID --range "Sheet1!A1:D10"` | Cell range reads |
| **List Gmail** | `gws gmail users messages list --user-id me --max-results 10` | Personal Gmail only |
| **Search Gmail** | `gws gmail users messages list --user-id me --query "from:someone@example.com"` | Gmail search syntax |
| **Read email** | `gws gmail users messages get --user-id me --id MSG_ID` | Full message content |
| **List Calendar events** | `gws calendar events list --calendar-id primary` | Personal calendar only |
| **Create Calendar event** | `gws calendar events insert --calendar-id primary --summary "Meeting" --start "2026-03-15T10:00:00" --end "2026-03-15T11:00:00"` | Personal calendar only |
| **List Docs** | `gws docs documents list` | Google Docs metadata |
| **Get Doc content** | `gws docs documents get --document-id DOC_ID` | Full document content |

**Auth & Setup:**
- OAuth2 Desktop App flow -- tokens cached at `~/.config/gws/`
- Google Cloud project: `mycel-cli-tools` (project number: 976809045428)
- OAuth client: "gws CLI" (Desktop app type)
- Credentials file: `~/.config/gws/client_secret.json`
- Auth is **per-machine** -- each Mac needs its own `gws auth login` (tokens are not synced)
- If auth expires, run `gws auth login` to re-authenticate in browser

**Usage Rules:**
- **Work email/calendar = MS365 ONLY** -- never use `gws gmail` or `gws calendar` for michael@yelin.io work
- `gws gmail` and `gws calendar` are for **personal** items only (michaelduncan17@gmail.com)
- `gws drive`, `gws sheets`, `gws docs` -- always use these for Google Workspace file access
- Use space-separated subcommands (e.g., `gws gmail users messages list`), not dot notation
- gws is a CLI tool called via Bash, NOT an MCP server

**Mac Mini Setup (when on that machine):**
```bash
npm install -g @googleworkspace/cli
# Copy client_secret.json from MacBook Air or use same OAuth credentials
gws auth setup    # enter same client ID/secret from mycel-cli-tools project
gws auth login    # opens browser -- separate auth per machine
```

## Lessons Learned

1. **Always check Sent Items** -- Critical decisions (like Dripify->Lemlist pivot) are often in emails I sent, not received
2. **Granola syncs to Notion** -- Don't search email for meeting notes; check Notion's Granola Notes database
3. **config.json is the timeline source** -- Always update this FIRST, then run generator
4. **Multi-system updates require all three** -- Notion, config.json, and git push
5. **Notion MCP works for writes now** -- The old Cowork MCP had a param bug, but the current Claude Code Notion MCP handles updates correctly. Use MCP first, curl as fallback
6. **Notion token lives in `.claude/settings.local.json`** -- If API calls return 401, the token is expired and Mike needs to regenerate at notion.so/profile/integrations
7. **gws Gmail/Calendar is personal only** -- Never use gws for work email/calendar (michael@yelin.io). Work stays on MS365. gws Gmail/Calendar is strictly for michaelduncan17@gmail.com personal items.
8. **gws auth is per-machine** -- Each Mac needs its own `gws auth login`. Tokens at `~/.config/gws/` are not synced via dotfiles or dev-sync. If gws commands fail with auth errors, re-run `gws auth login`.
