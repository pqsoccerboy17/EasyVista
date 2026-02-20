# EasyVista — Client Context

## Engagement Overview
- **Client:** EasyVista (ITSM/ESM software company)
- **Engagement:** Q1 2026 AI/GTM consulting
- **Timeline:** Jan–Mar 2026 (Mar 7 Go/No-Go, Mar 31 hard stop)
- **Budget:** $10-15K across 3 workstreams
- **Team:** Mike Duncan (lead), Henry Yelin (partner), Russell Beggs (co-delivery)

## Workstreams
1. **Lemlist** — Outbound email automation for BDR teams (US, France, DACH, UK, Spain, Italy)
2. **Loopio** — RFP/presales knowledge management tool rollout
3. **Tech Due Diligence** — AI readiness assessment for PE investor narrative

## Key People

| Who | Role | Notes |
|-----|------|-------|
| **Evan Carlson** | COO @ EasyVista | Primary exec sponsor, weekly 1:1s with Mike |
| **Patrice Barbedette** | CEO @ EasyVista | Board-level updates, travels London/Paris |
| **Chris Hult** | VP RevOps @ EasyVista | Handles NetSuite POs, Lemlist admin, based in Colorado |
| **Tim Brouillard** | VP Global BD | Champion, dual-hatted as West Coast AE + BD |
| **Dalila Souiah** | Global Head of Presales | Co-leads Loopio adoption with Yann |
| **Yann Mercier** | PreSales Manager France | Global knowledge management owner, Loopio product owner |
| **Todd Russell** | Solution Consultant (US) | US Loopio point person, Minnesota |
| **Jon Ryman** | Presales Manager South Europe & UK | Loopio translation workstream |
| **Alessio De Santis** | Marketing Operations | Owns HubSpot, 6sense, website. Reports to CMO |
| **Enrico** | CMO | Co-owner of HubSpot scoring decisions |
| **Sean Herbert** | VP Sales Northern Europe & ME | Custom ChatGPT for RFPs, Gong advocate |
| **Alexander Klinner** | External Consultant | PMI/OTRS integration, joins ExCom |
| **Christopher T. Kuhn** | COO OTRS AG | Germany works council constraints |
| **Cédric Cibot-Voisin** | SVP Sales Europe | Critical for France adoption ("needs to be France's idea") |
| **Ismael Sabbagh** | Country Manager Spain | Spain BDR coordination |
| **Stefano Marrucci** | Head of Sales Italy | Italy BDR coordination |
| **Raphael Hugnet** | Directeur Commercial France | France new-client BDR coordination |
| **Laure Ruperas** | Directrice Commerciale | France, role TBD |
| **Rod** | US Sales | Power user, prefers ChatGPT — adoption risk for Loopio |
| **Jan** | EasyVista France | Translation/Loopio library work |
| **Eduardo** | Lemlist Enterprise AE | Enterprise tier contact |
| **Esteban Yanischevsky** | Lemlist CSM | Customer success, onboarding |

→ Full profiles: memory/people/
→ Notion Stakeholders DB: `1447853a-4ae0-4cc2-b560-0879e5f97374`

## Architecture (EasyVista-specific)

**Static-first, config-driven timeline:**
- Source of truth: [config.json](../../../config.json) (12KB JSON file)
- Generator: [generate_timeline.py](../../../generate_timeline.py) → produces 4 artifacts
- Dashboard: [index.html](../../../index.html) (Mermaid.js, works offline)

**Update Workflow:**
1. Edit config.json only (never edit derivative files directly)
2. Run `python3 generate_timeline.py`
3. Review: `git diff`
4. Commit all modified files together

**Generated artifacts (auto-updated by script):**
- easyvista-gantt.mermaid
- easyvista-stakeholders.mermaid
- easyvista-timeline.md
- index.html (stakeholder class assignments)

**Git (dual-remote):**
- **origin** (dev): `git@github.com:pqsoccerboy17/EasyVista.git`
- **production**: `git@github.com:yelin-io/EasyVista.git`
- Default: `git push` → origin | `git push production main` → client-facing

**Multi-System Sync:** When updating project status, sync all three: Notion → config.json → git push

## Stakeholder Status Model (5 states)
- `engaged` ✓ — Committed, scheduled meetings
- `scheduled` 📅 — Call booked
- `outreach_sent` 📧 — Waiting for response
- `cold` — Not yet contacted
- `risk` ⚠️ — Adoption resistance

## Regional Scoping
- **DACH** (Germany/Austria/Switzerland): Lemlist pilot, works council constraints
- **US**: Baseline validation
- **France**: Secondary rollout phase
- **UK/Spain/Italy**: BDR coordination in progress

## Operational Context
- **Milestone gating:** Mar 7 Go/No-Go decision, Mar 31 hard stop
- **Budget:** $10-15K across 3 workstreams (Lemlist, Loopio, Tech DD)
- See [TEMPLATE-README.md](../../../TEMPLATE-README.md) for schema docs
