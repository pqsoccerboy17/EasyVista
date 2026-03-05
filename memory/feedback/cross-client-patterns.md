# Cross-Client Patterns

Intelligence that applies across all client engagements. Updated by /review-week.

## Outreach
- Plain text only in customer-facing emails -- no markdown formatting
- Concise, scannable formatting preferred
- Match language to recipient's region (English for US/UK, note French/German contacts)

## Stakeholder Engagement
- Weekly 1:1 cadence with exec sponsors maintains engagement
- Regional rollouts require local champion buy-in ("needs to be France's idea")
- Works council constraints in DACH region affect tool adoption timelines

## Tool Reliability
- Notion MCP update-page: known param bug, always use curl PATCH
- Notion token: check .claude/settings.local.json, may expire (401 = regenerate)
- Granola Notes: syncs to Notion, not email -- search Notion for meeting transcripts
- MS365: always search Sent Items too -- critical decisions live in sent mail

## Proposal Patterns
- Tier-based pricing (Gold/Silver/Lean) gives clients choice without anchoring low
- PE-backed companies respond to EBITDA impact framing
- Include post-engagement tracking (90/180 day) to demonstrate lasting value
