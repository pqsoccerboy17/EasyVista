# Yelin.io -- Statement of Work (SoW) Framework Guide

## Overview

This framework provides a reusable SoW structure for Yelin.io consulting engagements. It was built from Infocenter's proven SoW methodology (used across 20+ enterprise clients) and adapted for AI/technology consulting.

## When to Use

Create a SoW for every paid engagement. Even small advisory retainers benefit from a lightweight SoW -- it sets expectations and protects both sides.

## Engagement Types

| Type | Typical Duration | Pricing Model | Sections to Include |
|------|-----------------|---------------|-------------------|
| **Strategy Assessment** | 2-4 weeks | Fixed fee | All sections, lighter scope detail |
| **Implementation** | 4-12 weeks | Fixed fee or T&M | All sections, detailed scope by workstream |
| **Advisory / Retainer** | Ongoing (monthly) | Monthly retainer | Skip Timeline, lighter Scope, add retainer terms to Pricing |

## Template File

`yelin-consulting-sow-template.docx` -- Open, Save As with client name, replace all `[PLACEHOLDER]` values.

### Placeholder Variables

| Placeholder | Replace With | Example |
|-------------|-------------|---------|
| `[CLIENT_NAME]` | Client company name | TBI Bank |
| `[CLIENT_LOGO]` | Insert client logo image | -- |
| `[ENGAGEMENT_TITLE]` | Descriptive engagement name | AI Engineering Support |
| `[VERSION]` | Document version | v1.0 |
| `[DATE]` | Document date | March 5, 2026 |
| `[CONSULTANT_NAME]` | Lead consultant | Mike Duncan |
| `[ENGAGEMENT_TYPE]` | Strategy / Implementation / Advisory | Implementation |

## Section-by-Section Guide

### Cover Page
Always include. Use client's logo if available. The confidentiality statement stays on every SoW.

### 1. Engagement Overview
2-3 paragraphs max. Answer: What are we doing? Why? What's our approach? Name the engagement type.

### 2. About [Client]
Shows the client you understand their business. One paragraph -- pull from your research or /research skill output. Include industry, size, and why this engagement is relevant to their goals.

### 3. Business Objectives
The "why this matters" section. List 3-5 measurable objectives. Each should be testable -- at the end of the engagement, you can point to this list and say "done" or "not done."

**Good:** "Reduce manual data entry by 40% through AI-assisted automation"
**Bad:** "Improve operations"

### 4. Scope of Work
The most important section for preventing scope creep. Organize by workstream or phase. Use bullet lists of specific activities. Frame as "Yelin.io will..." to make ownership clear.

**Tip:** Everything NOT listed here is implicitly out of scope. For sensitive clients, add an explicit "Out of Scope" subsection.

### 5. Assumptions
This section protects you. Include:
- Client will provide timely access to systems, data, and personnel
- Client will designate a primary point of contact
- Work will be performed remotely unless otherwise specified
- Client is responsible for [specific things they own]
- Any material changes to scope will follow the Change Request Process (Appendix A)
- [Add engagement-specific assumptions]

### 6. Deliverables
Table format. Every deliverable gets a description, format (DOCX, PPTX, code repo, etc.), and due timing. Clients sign off on deliverables -- this is how you close the project cleanly.

### 7. Services & Approach
Phased approach table. Standard phases:
- **Discovery:** Requirements gathering, stakeholder interviews, current state analysis
- **Build:** Development, configuration, integration work
- **Deliver:** Testing, review, training, handoff
- **Close:** Final review, sign-off, project closeout

Adjust phases to fit the engagement. Strategy assessments might only have Discovery + Deliver.

### 8. Team & Roles
List both Yelin.io team members AND required client roles. The "Type" column (Yelin.io / Client / Both) makes ownership clear. Include expected time commitments for client roles.

### 9. Timeline
Phase breakdown with week targets. Include Go/No-Go decision points for larger engagements. Keep it realistic -- clients respect honesty over optimism.

### 10. Pricing & Payment
Include directly in the SoW (unlike Infocenter which used separate order forms). Options:
- **Fixed fee:** Best for well-defined scope. Payment at milestones.
- **Time & Materials:** Best for advisory or evolving scope. Hourly/daily rate with monthly invoicing.
- **Retainer:** Monthly fee for ongoing advisory. Define included hours and overage rates.

Standard terms: Net 30, expenses billed at cost.

### 11. Terms & Conditions
Keep it concise but cover:
- **Confidentiality:** Both parties protect shared information
- **IP/Work Product:** Clarify who owns deliverables, code, models, data. For AI work, this is critical -- specify if client gets full ownership or a license.
- **Limitation of Liability:** Cap at engagement value
- **Termination:** Either party with 30 days written notice; client pays for work completed

### Appendix A: Change Request Process
Include on every SoW. A material change is:
1. Substantial change to scope
2. Extension of timeline
3. Additional resources not in the original SoW

Process: Notify -> Discuss requirements -> Estimate cost/impact -> Get sign-off before work begins.

## File Naming Convention

- Template: `yelin-consulting-sow-template.docx`
- Client SoWs: `[Client Name] - [Engagement] - SoW [version].docx`
- Example: `TBI Bank - AI Eng Support - SoW v1.docx`
- Store in: `clients/[CLIENT]/`

## Tips from Experience

1. **Send as PDF** -- Convert to PDF before sending to clients. Prevents accidental edits.
2. **Version control** -- Increment version on every material change (v1, v1.1, v2).
3. **Get it signed** -- A SoW without a signature is just a proposal. Push for sign-off before starting work.
4. **Reference the proposal** -- If a proposal preceded the SoW, reference it: "This SoW formalizes the scope outlined in [Proposal Name] dated [date]."
5. **Keep assumptions honest** -- Better to over-specify assumptions than to fight about them later.
