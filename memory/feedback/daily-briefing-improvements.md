# Daily Briefing Skill - Improvement Recommendations

> Based on friction analysis from Feb 4, 2026 session

## Executive Summary

The `sales:daily-briefing` skill is tool-agnostic by design, which is good architecture. However, several gaps emerged when using it with Microsoft 365 as the primary email/calendar system.

## Friction Points Identified

### 1. Default Tool Selection
**Problem:** Skill defaulted to Gmail/GCal even when MS365 tools were available.

**Root Cause:** The skill uses generic `~~email` and `~~calendar` placeholders without checking CLAUDE.md for user preferences.

**Recommendation:**
- Read CLAUDE.md **first** before selecting email/calendar tools
- Look for explicit tool preference declarations like:
  ```markdown
  **Default Connectors:**
  - **Email:** Microsoft 365 (Outlook)
  ```
- Fall back to available tools only if no preference is declared

### 2. Sent Items Not Searched
**Problem:** Critical context was missed because only Inbox was searched, not Sent Items.

**Impact:** Missed the Dripify → Lemlist pivot decision that was communicated via sent email.

**Recommendation:**
- **Always search both Inbox AND Sent Items** when gathering context
- Add to daily-briefing flow:
  ```
  1. Search Inbox for unread/recent (existing)
  2. Search Sent Items for recent actions/commitments (NEW)
  ```
- Rationale: Decisions, commitments, and pivots are often captured in what we SEND, not what we receive

### 3. Meeting Notes Source
**Problem:** Skill checked email for meeting context when notes were in Notion (via Granola).

**Recommendation:**
- Check CLAUDE.md for meeting notes integration pattern
- Support `Granola → Notion` pattern common in many setups
- Add Notion search for "Granola Notes" database when available

### 4. Multi-System Awareness
**Problem:** After gathering intel, skill didn't know about multi-system sync requirements.

**Recommendation:**
- Check for sync patterns in CLAUDE.md (e.g., Notion ↔ config.json ↔ GitHub)
- Offer to trigger sync skills when updates are identified
- Reference custom skills like `easyvista-sync` when available

## Proposed Skill Enhancements

### Enhancement A: Pre-flight Tool Detection
```
BEFORE executing briefing:
1. Read CLAUDE.md
2. Parse "Tool Preferences" or "Default Connectors" section
3. Set tool mappings:
   - ~~email → detected preference OR available tool
   - ~~calendar → detected preference OR available tool
   - ~~CRM → detected preference OR available tool
4. Log which tools are being used for transparency
```

### Enhancement B: Comprehensive Email Search
```
WHEN gathering email context:
1. Search Inbox (existing)
   - Unread messages
   - Messages from key accounts (last 7 days)
2. Search Sent Items (NEW)
   - Recent sent emails (last 3-7 days)
   - Focus on: decisions, commitments, pivots
3. Merge and dedupe threads
```

### Enhancement C: Memory-Aware Context Building
```
WHEN building briefing context:
1. Check memory/ directory for:
   - context/tools.md (tool preferences)
   - context/accounts.md (key accounts)
   - feedback/*.md (previous learnings)
2. Check for meeting notes integrations:
   - Granola → Notion
   - Fireflies → CRM
   - Otter → Google Drive
3. Include relevant context in briefing
```

## Implementation Priority

| Priority | Enhancement | Effort | Impact |
|----------|-------------|--------|--------|
| P0 | Search Sent Items | Low | High |
| P1 | Read CLAUDE.md for tool prefs | Medium | High |
| P2 | Memory-aware context | Medium | Medium |
| P3 | Multi-system sync awareness | High | Medium |

## Lessons Learned

1. **Sent Items are gold** - Critical decisions often live in what we send, not what we receive
2. **CLAUDE.md is the preferences file** - Should be read before any skill execution
3. **Meeting notes ≠ email** - Many users have Granola/Fireflies → Notion/CRM flows
4. **Multi-system sync is common** - Skills should be aware of sync patterns

## Related Files

- [memory/context/tools.md](../context/tools.md) - Tool preferences documentation
- [CLAUDE.md](../../CLAUDE.md) - Project memory and preferences
- [skills/easyvista-sync/SKILL.md](../../../.claude/skills/easyvista-sync/SKILL.md) - Custom sync skill

---
*Generated: Feb 4, 2026*
*Session: Yelin.io / EasyVista consulting workflow optimization*
