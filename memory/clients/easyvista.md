# EasyVista -- Client Context

> Last reviewed: 2026-03-10

## Engagement Overview
- **Client:** EasyVista (ITSM/ESM software company)
- **Engagement:** Q1 2026 AI/GTM consulting
- **Timeline:** Jan-Mar 2026 (Lemlist fully deployed Mar 5, Mar 31 hard stop)
- **Budget:** $10-15K across 3 workstreams
- **Team:** Mike Duncan (lead), Henry Yelin (partner), Russell Beggs (co-delivery)

## Workstreams
1. **Lemlist** -- Outbound email automation for BDR teams (US, France, DACH, UK, Spain, Italy). FULLY DEPLOYED as of Mar 5.
2. **Loopio** -- RFP/presales knowledge management tool rollout
3. **Tech Due Diligence** -- AI readiness assessment for PE investor narrative

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
| **Christopher T. Kuhn** | COO OTRS AG | Germany works council constraints -- now engaged |
| **Cedric Cibot-Voisin** | SVP Sales Europe | Critical for France adoption -- now engaged |
| **Ismael Sabbagh** | Country Manager Spain | Spain BDR coordination |
| **Stefano Marrucci** | Head of Sales Italy | Italy BDR coordination |
| **Raphael Hugnet** | Directeur Commercial France | France new-client BDR -- now engaged |
| **Laure Ruperas** | Directrice Commerciale | France, fully resolved |
| **Rod** | US Sales | Power user, prefers ChatGPT -- adoption risk for Loopio |
| **Jan** | EasyVista France | Translation/Loopio library work |
| **Eduardo** | Lemlist Enterprise AE | Enterprise tier contact |
| **Esteban Yanischevsky** | Lemlist CSM | Handoff underway, Lemwarm launched Mar 10 |
| **Douae** | EasyVista (ESG/Sustainability) | New stakeholder -- surfaced in Loopio/ESG context Mar 6 |
| **Lucas Klotz** | BDR DACH | New BDR added Mar 10 |
| **Britton Hudson** | BDR US | New BDR added Mar 10 |
| **Olga Shonina** | BDR UK | New BDR added Mar 10 |
| **Claudia Marcelos** | BDR Italy | New BDR added Mar 10 |
| **Karim Senra Bensciri** | BDR Spain | New BDR added Mar 10 |
| **Pablo Pavon** | BDR Spain | New BDR added Mar 10, needs seat |
| **Cliff Jones** | BDR US | New BDR added Mar 10 |
| **Paulo Magalhaes** | BDR Southern EU | New BDR added Mar 10 |

-> Full profiles: contacts/
-> Notion Stakeholders DB: `1447853a-4ae0-4cc2-b560-0879e5f97374`

## Architecture (EasyVista-specific)

**Static-first, config-driven timeline:**
- Source of truth: `clients/easyvista/config.json` (12KB JSON file)
- Generator: `clients/easyvista/generate_timeline.py` - produces 4 artifacts
- Dashboard: `clients/easyvista/index.html` (Mermaid.js, works offline)

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
- Default: `git push` -> origin | `git push production main` -> client-facing

**Multi-System Sync:** When updating project status, sync all three: Notion -> config.json -> git push

## Stakeholder Status Model (5 states)
- `engaged` -- Committed, scheduled meetings
- `scheduled` -- Call booked
- `outreach_sent` -- Waiting for response
- `cold` -- Not yet contacted
- `risk` -- Adoption resistance

## Regional Scoping
- **DACH** (Germany/Austria/Switzerland): Lemlist pilot, works council constraints
- **US**: Baseline validation
- **France**: Secondary rollout phase
- **UK/Spain/Italy**: BDR coordination in progress

## Intelligence Maturity
- Contacts profiled: 8/31 (26%)
- Last /next-steps: 2026-03-06
- Last /update-project: 2026-03-10
- Research dossier: YES
- Maturity: DEVELOPING

## Operational Context
- **Lemlist fully deployed:** Mar 5 Go decision, all regions active
- **Budget:** $10-15K across 3 workstreams (Lemlist, Loopio, Tech DD)
- **Loopio KPIs (Mar 6):** 2,040 total entries (907 EN + 882 FR + 251 OTRS), 200+ documents, 23 projects (12 FR/9 EN/2 ES), 65.53% AI-generated (increasing), 18 pending opps. Todd completed 2 RFPs post-reload, "very happy." Yann doing 1:1 presales training on real RFPs.
- **Loopio security expansion:** Security team onboarded Mar 6. New workflow: presales import security grid -> AI first layer -> assign to security for review.
- **Loopio ESG expansion:** Evan requested Douae/ESG onboarding Mar 6. Douae populates ESG forms for RFPs. Scheduling TBD.
- **Lemlist Q2:** Commitment discussion active (Chris Hult thread). 10/10 seats used -- capacity confirmed.
- **Esteban transition:** Lemlist CSM handoff underway, Lemwarm launched Mar 10. New CSM assignment pending.
- **Apr 2 conclusion date:** Set per recent planning.
- **BDR governance:** 8 new BDRs added without formal onboarding process -- governance gap flagged as risk.
- **Open:** Douae ESG onboarding scheduling, Pablo seat needed, Project Conclusion meeting TBD, Rod workflow interview still pending.
- See `templates/TEMPLATE-README.md` for schema docs

## Lemlist Adoption Audit (Mar 10, 2026)

**Source:** Live Lemlist dashboard data via browser automation.

**Overall:** 113 total emails sent, 107 delivered (94.7%), 6 bounced (5.3%). Deliverability score 70.0, 100% inbox rate, 0 spam.

**Active Adopters (4/14 accounts):**
| BDR | Emails Sent | Delivery | Open Rate | Campaign | Last Active |
|-----|-------------|----------|-----------|----------|-------------|
| Blaise Lutete | 47 | 93.6% | 31.5% | BDR France Blaise (95 leads) | Mar 8 |
| Lucas Klotz | 35 | 100% | 55.6% | Lucas's First Campaign (252 leads) | Mar 9 |
| Britton Hudson | 28 | 89.3% | 7.9% | AI - Linkedin - Britton's Campaign (2,500 leads) | Mar 8 |
| Eric Montaron | 3 | 100% | 0.7% | BDR France Eric (141 leads) | Mar 5 |

**Inactive (have seats, zero activity):** Khalil Bedioui, Claudia Marcelos, Olga Shonina, Karim Senra, Raphael Hugnet, Stefano Marrucci, Ismael Sabbagh

**No seats:** Tim Brouillard, Seima Ishaq, Pablo Pavon

**Non-BDR accounts:** Chris Hult (admin, test campaign), Alessio De Santis (marketing), Michael Duncan (observer)

**Lemwarm warm-up:** Only 4 mailboxes connected (emontaron, bhudson, lklotz, blutete). All at score 70, daily limit 10, ramp-up day 1. Launched Mar 10 by Esteban.

**Key concern:** 60% of seated BDRs have not connected their mailbox or created any campaigns. This is a significant adoption gap with only 20 days until Q1 deadline.
