# Sanitization Rules — Customer-Facing Content

The EasyVista GitHub Pages site (index.html) is visible to Evan, Patrice, and other EasyVista stakeholders. Every update must be scanned for content that's appropriate for internal tracking but NOT for customer eyes.

## Grep Patterns to Check

Run this across all output files after regeneration:

```bash
grep -inE "(\$[0-9,]+|budget|pricing|cost|invoice|quote.*\$|per.?seat|ARR|MRR)" config.json index.html easyvista-timeline.md
grep -inE "(bypass|shadow.?IT|instead of|refusing|resist|won't use|100x|ChatGPT)" config.json index.html easyvista-timeline.md
grep -inE "(investor|capital raise|fundrais|Series [A-Z]|valuation|runway)" config.json index.html easyvista-timeline.md
grep -inE "(internal only|do not share|confidential|NDA|off the record)" config.json index.html easyvista-timeline.md
grep -inE "(Rod.*ChatGPT|ChatGPT.*Rod|Rod.*bypass|Rod.*alternative)" config.json index.html easyvista-timeline.md
```

## Categories & Replacement Guidance

### 1. Pricing / Budget Specifics
- **Pattern:** Dollar amounts, per-seat costs, annual contract values
- **Examples:** "$11,009/yr", "$150/seat/mo", "budget: $10-15K"
- **Fix:** Remove dollar amounts entirely. Use "Licensing secured" or "Procurement complete" instead.

### 2. Individual Names in Negative Context
- **Pattern:** "[Person] bypassing X", "[Person] refusing to use Y", "[Person] prefers ChatGPT"
- **Fix:** Replace with neutral, action-oriented language:
  - ❌ "Rod bypassing Loopio with ChatGPT"
  - ✅ "Individual tool preference divergence — workflow interview pending"
  - ❌ "Rod using ChatGPT 100x/day instead of Loopio"
  - ✅ "Prefers alternative tools over Loopio. Workflow interview pending to understand requirements."

### 3. Internal Strategy Language
- **Pattern:** "investor narrative", "capital raise", "fundraising readiness", "Series X"
- **Fix:** Replace with business-neutral framing:
  - ❌ "Deliverables must support investor communications"
  - ✅ "AI-enhanced workflows driving measurable improvements"

### 4. Shadow IT References
- **Pattern:** "shadow IT", "using ChatGPT instead of", "100x/day", "unauthorized tool"
- **Fix:** Frame as adoption opportunity, not compliance problem:
  - ❌ "Shadow IT risk — Rod using ChatGPT"
  - ✅ "Adoption optimization — workflow alignment in progress"

### 5. Consultant-Internal Notes
- **Pattern:** Budget gauges, stretch targets, internal-only commentary
- **Fix:** Remove entirely or replace with milestone-level summary.

## Where to Fix

- **config.json**: Rewrite notes diplomatically (they feed the generator and are not directly customer-facing, but they propagate)
- **index.html hardcoded sections**: Edit directly — the generator does NOT touch risks tables, open questions, task detail cards, or the executive summary section
- **Generated files** (mermaid, markdown): Fix in config.json first, then re-run `python3 generate_timeline.py`

## Post-Sanitization Verification

After all fixes, run the full grep suite above again. Expected result: **zero matches** across all output files for pricing, negative-name-context, and investor language patterns.
