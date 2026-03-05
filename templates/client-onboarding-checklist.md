# Client Onboarding Checklist

Use this checklist when starting a new client engagement. The `/new-client` skill automates most of these steps.

## Setup Steps

### 1. Create Client Folder
- [ ] Create `clients/[client-name]/` directory
- [ ] Add any initial documents (proposals, decks, working notes)

### 2. Create Client Context File
- [ ] Create `memory/clients/[client-name].md` using `templates/client-context-template.md`
- [ ] Fill in: engagement overview, scope, key people, status, deliverables location
- [ ] Add `> Last reviewed: YYYY-MM-DD` header

### 3. Add Primary Contact
- [ ] Run `/new-contact [name] at [company]` for the primary contact
- [ ] Verify profile saved to `contacts/[name]-[company].md`
- [ ] Confirm added to Notion Stakeholders DB

### 4. CRM Setup
- [ ] Add key stakeholders to Notion Stakeholders DB
- [ ] Set initial status for each contact (engaged, scheduled, outreach_sent, cold)

### 5. Determine Tooling Needs
- [ ] Does this engagement need a config.json-driven timeline? (like EasyVista)
- [ ] Does it need a client portal?
- [ ] Does it need a separate git remote for client-facing deliverables?

### 6. Communication Setup
- [ ] Identify primary communication channels (email, Teams, Slack)
- [ ] Note key email domains for MS365 search filtering
- [ ] Schedule recurring meetings if applicable

### 7. First Deliverable
- [ ] Confirm all initial deliverables are in `clients/[client-name]/`
- [ ] Nothing at root level -- root is ops infrastructure only
