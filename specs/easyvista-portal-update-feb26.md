# Spec: EasyVista Portal Update — Feb 26, 2026

## What
Update the client-facing portal site (GitHub Pages) to reflect everything that has happened since the last update (Feb 10-16). The portal is significantly stale — milestones that already happened are still showing as "upcoming," progress percentages are behind, and major events from the past two weeks are missing.

## Why
Evan, Patrice, and the EasyVista team use this portal to track project status. It needs to reflect reality before/after today's meetings. Stale data erodes trust.

## Scope

### 1. Update `config.json` (source of truth)
These tasks are already complete but not marked in config:

**Lemlist workstream — mark complete:**
- "Send training invites (French + English tracks)" — complete (sent Feb 25)
- Note: French BDR Training (Feb 26) is PUSHED to week of Mar 2 (Laure + Raphael OOO). Update task status and notes accordingly.
- English BDR Training (Feb 27) — keep as pending (tomorrow)

**Lemlist — update phase description:**
- Phase label: "BDR Training Rollout" is now the active phase
- Pilot Setup phase tasks are all complete

**Config milestones to add:**
- Feb 20: "Loopio first RFP completed in platform (Todd Russell / Mohawk)" — already there but description should note Mohawk (not Smartcat)
- Feb 24: "Alessio De Santis HubSpot/Lemlist integration meeting" — already there
- Feb 25: "AI at EasyVista: Project Update (Evan/Patrice)" — already there
- Feb 25: "Lemlist BDR training invites sent" — already there
- Feb 26: Update French training milestone to note it was pushed to week of Mar 2
- Feb 26: "Alessio De Santis AI & GTM Strategy meeting" (today)
- Feb 26: "Project Update with Evan, Patrice, Henry, Russell, Alex" (today)
- Feb 26: "Engineering catch-up with Patrice" (today)
- Feb 26: "Research Agent demo shown to Evan + Patrice — well received" (today)

**Config risks to update:**
- French BDR training risk — update to reflect it was officially pushed, rescheduling to week of Mar 2
- HubSpot integration timeline — Alessio confirmed "straightforward," meeting this week to finalize

**Config meta:**
- `last_updated` → `2026-02-26T18:00:00`

### 2. Update `portal/index.html` (home page)

**Hero stats:**
- Lemlist progress: 35% → **55%** (pilot live, training invites sent, 1 of 2 sessions this week)
- Loopio progress: 50% → **60%** (first RFP completed, NAM team comfortable, training sessions scheduled)

**Status banner:**
- Update text: "US pilot live since Feb 20. BDR training sessions this week. First Loopio RFP completed — 3x time savings confirmed. Both workstreams on track for Mar 7 Go/No-Go."

**"Latest" callout:**
- Change to: "Research Agent demo well received by CEO & COO (Feb 26)"

**Milestones section — mark completed:**
- Feb 14 (Lemlist Quote & PO): Done
- Feb 21 (Lemlist US Pilot Launch): Done (actually launched Feb 20)
- Feb 25 (Project Update): Done

**Milestones section — add upcoming:**
- Feb 27: English BDR Training (MANDATORY)
- ~Mar 2: French BDR Training (rescheduled)
- Mar 7: Lemlist Pilot Results Review (keep)

**Workstream cards:**
- Lemlist phase: "BDR Training Rollout"
- Loopio phase: "Implementation — Training Scheduling"

**Footer:**
- "Last updated: Feb 26, 2026"

**Footer milestones JS array:**
- Update to reflect current upcoming milestones

### 3. Update `portal/progress.html`

**Summary stats:**
- Overall progress: 59% → **68%**
- Milestones complete: 15/21 → count from updated config (should be ~18/24)

**Workstream progress bars:**
- Lemlist: 45% → **55%**, label: "US Pilot Live → BDR Training"
- Lemlist description: "US pilot launched Feb 20. Enterprise contract signed. BDR training sessions: English Feb 27, French rescheduled to week of Mar 2. Go/No-Go decision Mar 7."
- Loopio: 50% → **60%**, label: "Implementation → Training"
- Loopio description: "First RFP completed in Loopio (Mohawk, Todd Russell) — 3x time savings. NAM team trained and comfortable. US pre-sales training Feb 28, France Mar 14."

**Timeline — mark as complete:**
- Feb 18: Lemlist Onboarding Kickoff → Complete
- Feb 23: Lemlist US Pilot Launch → Complete (launched Feb 20)
- Feb 25: Project Update → Complete

**Timeline — add new items:**
- Feb 20: "First Loopio RFP Completed (Mohawk)" — Complete
- Feb 24: "HubSpot/Lemlist Integration Meeting" — Complete
- Feb 26: "Research Agent Demo to CEO/COO — Well Received" — Complete
- Feb 27: "MANDATORY English BDR Training" — Next Up
- ~Mar 2: "French BDR Training (rescheduled)" — Upcoming

**Lemlist phase checklist:**
- Phase 4 (US Pilot Launch): mark Complete
- Add Phase: "BDR Training Rollout (In Progress — English Feb 27, French ~Mar 2)"

**Lemlist task table — update statuses:**
- Configure Lemlist: Complete
- Onboarding call: Complete
- Templates & train champion: Complete
- Launch US pilot: Complete
- Add: "English BDR Training" — Feb 27 — Next Up
- Add: "French BDR Training" — ~Mar 2 — Upcoming (rescheduled)

**Loopio task table — update statuses:**
- Define usage metrics: Complete
- Interview Rod: Complete
- Training materials: Complete
- Add: "First RFP completed (Mohawk)" — Feb 20 — Complete
- US pre-sales training: Feb 28 — In Progress

**Footer:**
- "Last updated: Feb 26, 2026"

### 4. Run `generate_timeline.py`
After config.json edits, run the generator to update:
- `easyvista-gantt.mermaid`
- `easyvista-stakeholders.mermaid`
- `easyvista-timeline.md`
- `index.html` (internal Mermaid dashboard — separate from portal)

### 5. Git commit & push
- Commit all changes to origin (dev)
- Push to production remote (`git push production main`) — **ask Mike first**

## Out of Scope
- ROI page updates (no new data)
- Guide pages (lemlist.html, loopio.html) — no structural changes needed
- Design system CSS changes
- New portal pages

## Risks
- French training date is approximate ("week of Mar 2") — use "~Mar 2" until confirmed
- Research Agent demo follow-up specs are TBD — don't add to portal milestones yet

## Implementation Order
1. Edit `config.json`
2. Run `generate_timeline.py` (updates internal dashboard + mermaid files)
3. Edit `portal/index.html`
4. Edit `portal/progress.html`
5. Review with `git diff`
6. Commit and push
