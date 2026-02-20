# Data Sources — MCP Tool Reference

Quick reference for all data source tools used by the `/update-project` skill. Tool IDs are stable MCP server identifiers.

## Microsoft 365 (Outlook)

**Server prefix:** `mcp__f94d56e9-d249-4ef1-ad10-6e9f2088b48b`

### Email Search
**Tool:** `mcp__f94d56e9-d249-4ef1-ad10-6e9f2088b48b__outlook_email_search`

| Parameter | Inbox Search | Sent Items Search |
|-----------|-------------|-------------------|
| `query` | `"EasyVista"` | `"EasyVista"` |
| `afterDateTime` | 7 days ago (ISO 8601) | 7 days ago (ISO 8601) |
| `folderName` | _(omit for Inbox)_ | `"Sent Items"` |
| `limit` | `20` | `15` |

**Why Sent Items?** Mike's outbound emails often contain critical decisions, approvals, and action items that don't appear in Inbox threads.

### Calendar Search
**Tool:** `mcp__f94d56e9-d249-4ef1-ad10-6e9f2088b48b__outlook_calendar_search`

| Parameter | Value |
|-----------|-------|
| `query` | `"EasyVista OR Yelin OR Lemlist OR Loopio"` |
| `afterDateTime` | today (ISO 8601) |
| `beforeDateTime` | 30 days from today (ISO 8601) |
| `limit` | `20` |

### Read Full Email/Event
**Tool:** `mcp__f94d56e9-d249-4ef1-ad10-6e9f2088b48b__read_resource`

| Resource Type | URI Format |
|---------------|-----------|
| Email | `mail:///messages/{messageId}` |
| Calendar event | `calendar:///events/{eventId}` |

## Microsoft Teams

**Server prefix:** `mcp__f94d56e9-d249-4ef1-ad10-6e9f2088b48b`

### Chat Message Search
**Tool:** `mcp__f94d56e9-d249-4ef1-ad10-6e9f2088b48b__chat_message_search`

| Parameter | Value |
|-----------|-------|
| `query` | `"EasyVista"` |
| `afterDateTime` | 7 days ago (ISO 8601) |
| `limit` | `15` |

## Notion

**Server prefix:** `mcp__3c554394-ee46-4ae8-9550-f341b3cad2c8`

### Search (Granola Notes)
**Tool:** `mcp__3c554394-ee46-4ae8-9550-f341b3cad2c8__notion-search`

| Parameter | Value |
|-----------|-------|
| `query` | `"EasyVista Granola Notes"` |
| `query_type` | `"internal"` |
| `filters` | `{ "created_date_range": { "start_date": "YYYY-MM-DD" } }` (7 days ago) |

### Fetch Full Page
**Tool:** `mcp__3c554394-ee46-4ae8-9550-f341b3cad2c8__notion-fetch`

| Parameter | Value |
|-----------|-------|
| `id` | Page URL or UUID from search results |

### Update Page
**Tool:** `mcp__3c554394-ee46-4ae8-9550-f341b3cad2c8__notion-update-page`

Used in Phase 6 to sync status summary to the EasyVista project page in Notion.

## Local Files

| File | Path | Purpose |
|------|------|---------|
| Config (source of truth) | `config.json` | All project data — milestones, tasks, stakeholders, risks |
| Generator script | `generate_timeline.py` | Reads config.json → produces 4 derivative files |
| Customer-facing site | `index.html` | GitHub Pages dashboard (has hardcoded + generated sections) |
| Gantt chart | `easyvista-gantt.mermaid` | Generated — do not edit directly |
| Stakeholder map | `easyvista-stakeholders.mermaid` | Generated — do not edit directly |
| Timeline doc | `easyvista-timeline.md` | Generated — do not edit directly |

## Git Remotes

| Remote | URL | Purpose |
|--------|-----|---------|
| `origin` | `git@github.com:pqsoccerboy17/Mycel.git` | Dev repo (Mike's personal) |
| `production` | `git@github.com:yelin-io/EasyVista.git` | Client-facing org repo (GitHub Pages) |

**Push command:** `git push origin main && git push production main`

If SSH fails in the VM, output the commands for Mike to run locally:
```
cd ~/Projects/EasyVista && git push origin main && git push production main
```
