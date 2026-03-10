#!/usr/bin/env python3
"""
Timeline Generator - Creates md/html/mermaid from config.json
Also updates portal pages (portal/index.html, portal/progress.html)
Usage: python generate_timeline.py [config_path] [output_dir]
"""

import html
import json
import re
import sys
from datetime import datetime
from pathlib import Path

def load_config(path: str) -> dict:
    with open(path) as f:
        return json.load(f)

def generate_gantt(cfg: dict) -> str:
    """Generate mermaid gantt chart from config"""
    lines = [
        "```mermaid",
        "gantt",
        f"    title {cfg['client']['name']} {cfg['client']['deadline_label']} Timeline",
        "    dateFormat YYYY-MM-DD",
        ""
    ]

    for ws in cfg['workstreams']:
        lines.append(f"    section {ws['name']}")
        for i, phase in enumerate(ws['phases']):
            status = "active" if i == 0 else ""
            task_id = f"{ws['id']}_p{i}"
            if i == 0:
                lines.append(f"    {phase['name']} :{status}, {task_id}, {phase['start']}, {phase['end']}")
            else:
                prev_id = f"{ws['id']}_p{i-1}"
                lines.append(f"    {phase['name']} :{task_id}, after {prev_id}, {phase['end']}")
        lines.append("")

    # Milestones
    lines.append("    section Milestones")
    for m in cfg['milestones']:
        crit = "crit, " if m.get('critical') else ""
        lines.append(f"    {m['event']} :{crit}milestone, {m['date']}, 0d")

    lines.append("```")
    return "\n".join(lines)

def generate_stakeholder_map(cfg: dict) -> str:
    """Generate mermaid flowchart from stakeholders"""
    lines = [
        "```mermaid",
        "flowchart TB"
    ]

    # Group stakeholders
    groups = {}
    for s in cfg['stakeholders']:
        g = s['group']
        if g not in groups:
            groups[g] = []
        groups[g].append(s)

    for group, members in groups.items():
        lines.append(f"    subgraph {group.title()}")
        for m in members:
            status_icon = {"engaged": "✓", "outreach_sent": "📧", "risk": "⚠️", "excluded": "❌"}.get(m['status'], "")
            lines.append(f"        {m['name'].replace(' ', '_')}[\"{m['name']}<br/>{m['role']} {status_icon}\"]")
        lines.append("    end")

    lines.append("```")
    return "\n".join(lines)

def calculate_metrics(cfg: dict) -> dict:
    """Calculate progress metrics from config"""
    # Count tasks
    total_tasks = 0
    complete_tasks = 0
    for ws in cfg['workstreams']:
        for phase in ws['phases']:
            for task in phase['tasks']:
                total_tasks += 1
                if task.get('status') == 'complete':
                    complete_tasks += 1

    # Count stakeholders
    total_stakeholders = len(cfg['stakeholders'])
    engaged_stakeholders = sum(1 for s in cfg['stakeholders'] if s['status'] == 'engaged')

    # Calculate days remaining
    deadline = datetime.strptime(cfg['client']['deadline'], '%Y-%m-%d')
    days_left = (deadline - datetime.now()).days

    # Determine urgency level
    if days_left >= 60:
        urgency = 'safe'
    elif days_left >= 30:
        urgency = 'warning'
    else:
        urgency = 'critical'

    # Count risks
    risk_count = len(cfg['risks'])

    return {
        'total_tasks': total_tasks,
        'complete_tasks': complete_tasks,
        'total_stakeholders': total_stakeholders,
        'engaged_stakeholders': engaged_stakeholders,
        'days_left': days_left,
        'urgency': urgency,
        'risk_count': risk_count
    }

def update_index_html_mermaid(cfg: dict, index_path: str = "index.html"):
    """Update Mermaid diagram source code in index.html from config data"""
    import re

    with open(index_path, 'r') as f:
        html = f.read()

    # Generate fresh diagram content and strip ```mermaid / ``` fences
    gantt_raw = generate_gantt(cfg)
    gantt_content = gantt_raw.replace("```mermaid\n", "").rstrip("`").strip()

    stakeholder_raw = generate_stakeholder_map(cfg)
    stakeholder_content = stakeholder_raw.replace("```mermaid\n", "").rstrip("`").strip()

    # Append classDef definitions and class assignments to stakeholder content
    classdefs = [
        "",
        "    classDef engaged fill:#2ecc71,stroke:#27ae60,color:#fff",
        "    classDef scheduled fill:#4dc0c7,stroke:#3aa8af,color:#fff",
        "    classDef outreach fill:#f1c40f,stroke:#d4ac0d,color:#333",
        "    classDef cold fill:#95a5a6,stroke:#7f8c8d,color:#fff",
        "    classDef risk fill:#f8568b,stroke:#e04477,color:#fff",
        ""
    ]

    # Group stakeholders by status for class assignments
    status_groups = {
        'engaged': [], 'scheduled': [], 'outreach': [], 'cold': [], 'risk': []
    }
    for s in cfg['stakeholders']:
        name_key = s['name'].replace(' ', '_')
        status = s['status']
        if status == 'engaged':
            status_groups['engaged'].append(name_key)
        elif status == 'scheduled':
            status_groups['scheduled'].append(name_key)
        elif status == 'outreach_sent':
            status_groups['outreach'].append(name_key)
        elif status in ('pending', 'cold'):
            status_groups['cold'].append(name_key)
        elif status == 'risk':
            status_groups['risk'].append(name_key)

    class_lines = []
    for css_class, names in status_groups.items():
        if names:
            class_lines.append(f"    class {','.join(names)} {css_class}")

    stakeholder_content += '\n' + '\n'.join(classdefs) + '\n'.join(class_lines)

    # Replace Gantt chart: first <div class="mermaid"> that does NOT have id="stakeholder-map"
    # Match: <div class="mermaid"> ... </div> (the first one, which is the gantt)
    html = re.sub(
        r'(<div class="mermaid">)\n.*?\n(                </div>)',
        r'\1\n' + gantt_content + r'\n\2',
        html,
        count=1,
        flags=re.DOTALL
    )

    # Replace Stakeholder map: <div class="mermaid" id="stakeholder-map"> ... </div>
    html = re.sub(
        r'(<div class="mermaid" id="stakeholder-map">)\n.*?\n(                </div>)',
        r'\1\n' + stakeholder_content + r'\n\2',
        html,
        count=1,
        flags=re.DOTALL
    )

    with open(index_path, 'w') as f:
        f.write(html)

    print(f"✓ Updated Mermaid diagrams in {index_path}")

def update_index_html_classes(cfg: dict, index_path: str = "index.html"):
    """Update stakeholder class assignments and progress metrics in index.html"""
    import re

    with open(index_path, 'r') as f:
        html = f.read()

    # Calculate metrics
    metrics = calculate_metrics(cfg)

    # Group stakeholders by status
    status_groups = {
        'engaged': [],
        'scheduled': [],
        'outreach': [],
        'cold': [],
        'risk': []
    }

    for s in cfg['stakeholders']:
        name_key = s['name'].replace(' ', '_').replace('-', '_')
        status = s['status']

        if status == 'engaged':
            status_groups['engaged'].append(name_key)
        elif status == 'scheduled':
            status_groups['scheduled'].append(name_key)
        elif status == 'outreach_sent':
            status_groups['outreach'].append(name_key)
        elif status == 'pending':
            status_groups['cold'].append(name_key)
        elif status == 'risk':
            status_groups['risk'].append(name_key)

    # Build new class assignment lines
    new_classes = []
    if status_groups['engaged']:
        new_classes.append(f"    class {','.join(status_groups['engaged'])} engaged")
    if status_groups['scheduled']:
        new_classes.append(f"    class {','.join(status_groups['scheduled'])} scheduled")
    if status_groups['outreach']:
        new_classes.append(f"    class {','.join(status_groups['outreach'])} outreach")
    if status_groups['cold']:
        new_classes.append(f"    class {','.join(status_groups['cold'])} cold")
    if status_groups['risk']:
        new_classes.append(f"    class {','.join(status_groups['risk'])} risk")

    # Replace the class assignments section
    pattern = r'(    classDef risk fill:#f8568b,stroke:#e04477,color:#fff\n\n)(    class .*?\n)+?(?=                </div>)'
    replacement = r'\1' + '\n'.join(new_classes) + '\n'
    html = re.sub(pattern, replacement, html, flags=re.MULTILINE)

    # Update progress stats
    # Tasks complete
    html = re.sub(
        r'<span class="stat-current" id="tasks-complete">\d+</span>\s*<span class="stat-total">/ \d+</span>',
        f'<span class="stat-current" id="tasks-complete">{metrics["complete_tasks"]}</span>\n                    <span class="stat-total">/ {metrics["total_tasks"]}</span>',
        html
    )

    # Stakeholders engaged
    html = re.sub(
        r'<span class="stat-current" id="stakeholders-engaged">\d+</span>\s*<span class="stat-total">/ \d+</span>',
        f'<span class="stat-current" id="stakeholders-engaged">{metrics["engaged_stakeholders"]}</span>\n                    <span class="stat-total">/ {metrics["total_stakeholders"]}</span>',
        html
    )

    # Days remaining with urgency color
    html = re.sub(
        r'<div class="stat-number urgency-\w+" id="days-remaining">\d+</div>',
        f'<div class="stat-number urgency-{metrics["urgency"]}" id="days-remaining">{metrics["days_left"]}</div>',
        html
    )

    # Deadline banner with urgency color
    html = re.sub(
        r'<div class="deadline-banner urgency-\w+" id="deadline-banner">.*?</div>',
        f'<div class="deadline-banner urgency-{metrics["urgency"]}" id="deadline-banner">🎯 Q1 Deadline: March 31, 2026 ({metrics["days_left"]} days remaining)</div>',
        html
    )

    # Active risks count
    html = re.sub(
        r'(<div class="stat-card">\s*<div class="stat-number">)\d+(</div>\s*<div class="stat-label">Active Risks</div>)',
        rf'\g<1>{metrics["risk_count"]}\g<2>',
        html
    )

    # Update footer date
    html = re.sub(
        r'Last updated: .*? \|',
        f'Last updated: {datetime.now().strftime("%b %d, %Y")} |',
        html
    )

    with open(index_path, 'w') as f:
        f.write(html)

    print(f"✓ Updated stakeholder class assignments in {index_path}")
    print(f"  Progress: {metrics['complete_tasks']}/{metrics['total_tasks']} tasks, {metrics['engaged_stakeholders']}/{metrics['total_stakeholders']} stakeholders engaged")
    print(f"  Countdown: {metrics['days_left']} days ({metrics['urgency']})")

def replace_marker(content: str, marker_name: str, new_inner: str, comment_style: str = "html") -> str:
    """Replace content between BEGIN/END markers. Returns updated content.
    Uses function replacement to avoid backreference issues with \\1, \\2 in content."""
    if comment_style == "js":
        pattern = rf'(// BEGIN:{marker_name}\n).*?(\n\s*// END:{marker_name})'
    else:
        pattern = rf'(<!-- BEGIN:{marker_name} -->\n).*?(\n\s*<!-- END:{marker_name} -->)'

    found = bool(re.search(pattern, content, flags=re.DOTALL))
    if not found:
        print(f"  WARNING: Marker '{marker_name}' not found -- skipped")
        return content

    def replacer(match):
        return match.group(1) + new_inner + match.group(2)

    return re.sub(pattern, replacer, content, count=1, flags=re.DOTALL)


def fmt_date(date_str: str) -> str:
    """Format YYYY-MM-DD as 'Mon D' (e.g. 'Mar 10')"""
    d = datetime.strptime(date_str, '%Y-%m-%d')
    return d.strftime('%b ') + str(d.day)


def esc(text: str) -> str:
    """HTML-escape text"""
    return html.escape(text, quote=True)


def _get_sorted_portal_milestones(cfg: dict, limit: int = 0, future_only: bool = False) -> list:
    """Get portal milestones sorted by date descending. Optionally filter to future-only."""
    today = datetime.now().strftime('%Y-%m-%d')
    milestones = cfg.get('portal_milestones', [])
    if future_only:
        milestones = [m for m in milestones if m['date'] >= today]
    milestones = sorted(milestones, key=lambda m: m['date'], reverse=True)
    if limit:
        milestones = milestones[:limit]
    return milestones


def update_portal_index(cfg: dict, portal_path: str):
    """Update portal/index.html using marker-based injection from config.json"""
    with open(portal_path, 'r') as f:
        content = f.read()

    metrics = calculate_metrics(cfg)
    workstreams = cfg['workstreams']
    today_str = datetime.now().strftime('%b ') + str(datetime.now().day)

    # 1. Hero stats (3 rings: days, lemlist %, loopio %)
    ws_rings = ""
    for ws in workstreams:
        pct = ws.get('progress_percent', 0)
        # Use short display name: "Lemlist" from "Lemlist (LinkedIn Automation)", "Loopio" from "Loopio Standardization"
        short_name = ws['name'].split('(')[0].split(' ')[0].strip()
        label = short_name + " Progress"
        ws_rings += f"""            <div class="hero-stat hero-stat--ring">
                <div class="hero-stat__ring-wrapper">
                    <svg class="progress-ring" width="80" height="80">
                        <circle class="progress-ring__bg" stroke="var(--color-border)" stroke-width="4" r="34" cx="40" cy="40"/>
                        <circle class="progress-ring__circle" stroke="var(--color-ev-teal)" stroke-width="4" stroke-linecap="round" r="34" cx="40" cy="40" data-percent="{pct}"/>
                    </svg>
                    <div class="hero-stat__value" data-count-to="{pct}" data-count-suffix="%">{pct}%</div>
                </div>
                <div class="hero-stat__label">{label}</div>
            </div>
"""

    hero_html = f"""        <div class="hero-stats">
            <div class="hero-stat hero-stat--ring">
                <div class="hero-stat__ring-wrapper">
                    <svg class="progress-ring" width="80" height="80">
                        <circle class="progress-ring__bg" stroke="var(--color-border)" stroke-width="4" r="34" cx="40" cy="40"/>
                        <circle class="progress-ring__circle" stroke="var(--color-ev-teal)" stroke-width="4" stroke-linecap="round" r="34" cx="40" cy="40" data-percent="0" id="days-ring"/>
                    </svg>
                    <div class="hero-stat__value" id="days-left" data-count-to="{metrics['days_left']}">{metrics['days_left']}</div>
                </div>
                <div class="hero-stat__label">Days to Q1 Deadline</div>
            </div>
{ws_rings}        </div>"""
    content = replace_marker(content, 'portal-hero-stats', hero_html)

    # 2. Latest milestone (most recent COMPLETE one)
    all_milestones = _get_sorted_portal_milestones(cfg)
    complete_only = [m for m in all_milestones if m['status'] == 'complete']
    if complete_only:
        m = complete_only[0]
        latest_text = f"{esc(m['title'])} ({fmt_date(m['date'])})"
    else:
        latest_text = "No milestones recorded"
    latest_html = f"""        <div class="last-milestone reveal">
            <span>Latest:</span> {latest_text}
        </div>"""
    content = replace_marker(content, 'portal-latest-milestone', latest_html)

    # 3. Status banner
    summaries = [ws.get('status_summary', '') for ws in workstreams if ws.get('status_summary')]
    banner_text = esc(' '.join(summaries)) if summaries else "Project in progress."
    banner_html = f"""        <div class="status-banner">
            <div class="status-banner__content">
                <h3>Project Status</h3>
                <p>{banner_text}</p>
            </div>
            <div class="status-badge status-badge--glow">On Track</div>
        </div>"""
    content = replace_marker(content, 'portal-status-banner', banner_html)

    # 4. Workstream cards
    # Static config for card display (icons, links, guide URLs)
    card_config = {
        'lemlist': {
            'icon': '📱',
            'display_name': 'Lemlist',
            'url': 'https://www.lemlist.com/',
            'subtitle': ' - LinkedIn Automation',
            'description': 'AI-powered outbound prospecting for BDR teams. Target: {goal}.',
            'links_html': '<a href="https://university.lemlist.com/" target="_blank" rel="noopener" style="color: var(--color-ev-teal);">University</a> &middot; <a href="https://help.lemlist.com/en/" target="_blank" rel="noopener" style="color: var(--color-ev-teal);">Help Center</a>',
            'guide': 'guides/lemlist.html'
        },
        'loopio': {
            'icon': '📝',
            'display_name': 'Loopio',
            'url': 'https://loopio.com/',
            'subtitle': ' Standardization',
            'description': 'Unified RFP response process across global pre-sales teams. {goal}.',
            'links_html': '<a href="https://support.loopio.com/hc/en-us" target="_blank" rel="noopener" style="color: var(--color-ev-teal);">Help Center</a> &middot; <a href="https://loopio.com/rfp-demo-video/" target="_blank" rel="noopener" style="color: var(--color-ev-teal);">Demo Video</a>',
            'guide': 'guides/loopio.html'
        }
    }

    cards_html = '            <div class="grid grid--2">\n'
    for ws in workstreams:
        cc = card_config.get(ws['id'], {})
        if not cc:
            continue
        phase_label = esc(ws.get('phase_label', ws.get('status', 'In Progress')))
        budget = esc(ws.get('budget_allocation', 'TBD') or 'TBD')
        desc = cc['description'].format(goal=esc(ws['goal']))
        cards_html += f"""                <div class="card card--interactive workstream-card">
                    <div class="workstream-card__icon">{cc['icon']}</div>
                    <h3 class="workstream-card__title"><a href="{cc['url']}" target="_blank" rel="noopener" style="color: inherit; text-decoration: none;">{cc['display_name']}</a>{cc['subtitle']}</h3>
                    <p class="workstream-card__description">
                        {desc}
                    </p>
                    <div class="workstream-card__meta">
                        <strong>Phase:</strong> {phase_label}<br>
                        <strong>Budget:</strong> {budget}<br>
                        <span style="font-size: 0.85rem; margin-top: 8px; display: inline-block;">{cc['links_html']}</span>
                    </div>
                    <a href="{cc['guide']}" class="workstream-card__link">
                        View Guide <span>&rarr;</span>
                    </a>
                </div>
"""
    cards_html += '            </div>'
    content = replace_marker(content, 'portal-workstream-cards', cards_html)

    # 5. Milestones list (last 7)
    recent_milestones = _get_sorted_portal_milestones(cfg, limit=7)
    complete_count = sum(1 for m in recent_milestones if m['status'] == 'complete')
    progress_pct = int((complete_count / max(len(recent_milestones), 1)) * 100)

    milestones_html = f"""            <div class="milestone-list">
                <div class="milestone-progress-track">
                    <div class="milestone-progress-fill" data-progress-height="{progress_pct}%"></div>
                </div>
"""
    for i, m in enumerate(recent_milestones):
        delay = i * 60
        is_complete = m['status'] == 'complete'
        dot_class = 'milestone-item__dot--complete' if is_complete else 'milestone-item__dot--upcoming'
        item_class = 'milestone-item--complete' if is_complete else ''
        if is_complete:
            badge = '<span class="milestone-item__badge" style="background-color: var(--color-success-bg); color: var(--color-success);">Done</span>'
        else:
            badge = '<span class="milestone-item__badge milestone-item__badge--next">Upcoming</span>'

        milestones_html += f"""                <div class="milestone-item {item_class} reveal" data-reveal-delay="{delay}">
                    <div class="milestone-item__date">{fmt_date(m['date'])}</div>
                    <div class="milestone-item__dot {dot_class}"></div>
                    <div class="milestone-item__content">{esc(m['title'])}</div>
                    {badge}
                </div>
"""
    milestones_html += '            </div>'
    content = replace_marker(content, 'portal-milestones', milestones_html)

    # 6. Footer JS milestones array
    future_milestones = _get_sorted_portal_milestones(cfg, future_only=True)
    future_milestones.sort(key=lambda m: m['date'])  # ascending for JS
    js_lines = []
    for m in future_milestones:
        js_lines.append(f"            {{ date: new Date('{m['date']}'), name: '{m['title'].replace(chr(39), chr(92) + chr(39))}' }}")
    js_array = "        var milestones = [\n" + ",\n".join(js_lines) + "\n        ];"
    content = replace_marker(content, 'portal-footer-milestones-js', js_array, comment_style="js")

    # 7. Footer date
    date_str = datetime.now().strftime('%b ') + str(datetime.now().day) + ', ' + str(datetime.now().year)
    footer_html = f'        <p style="margin-top: var(--space-2);">Last updated: {date_str}</p>'
    content = replace_marker(content, 'portal-footer-date', footer_html)

    with open(portal_path, 'w') as f:
        f.write(content)

    print(f"✓ Updated portal/index.html (hero stats, milestones, status banner, workstream cards)")


def update_portal_progress(cfg: dict, portal_path: str):
    """Update portal/progress.html using marker-based injection from config.json"""
    with open(portal_path, 'r') as f:
        content = f.read()

    metrics = calculate_metrics(cfg)
    workstreams = cfg['workstreams']
    portal_milestones = _get_sorted_portal_milestones(cfg)
    complete_milestones = sum(1 for m in portal_milestones if m['status'] == 'complete')
    total_milestones = len(portal_milestones)
    overall_pct = sum(ws.get('progress_percent', 0) for ws in workstreams) // max(len(workstreams), 1)

    # 1. Summary stats
    stats_html = f"""            <div class="summary-stats">
                <div class="stat-box reveal" data-reveal-delay="0">
                    <div class="stat-number" data-count-to="{overall_pct}" data-count-suffix="%">{overall_pct}%</div>
                    <div class="stat-label">Overall Progress</div>
                </div>
                <div class="stat-box reveal" data-reveal-delay="100">
                    <div class="stat-number">{complete_milestones}/{total_milestones}</div>
                    <div class="stat-label">Milestones Complete</div>
                </div>
                <div class="stat-box reveal" data-reveal-delay="200">
                    <div class="stat-number" id="progress-days-left" data-count-to="{metrics['days_left']}">{metrics['days_left']}</div>
                    <div class="stat-label">Days to Deadline</div>
                </div>
                <div class="stat-box reveal" data-reveal-delay="300">
                    <div class="stat-number" data-count-to="{len(workstreams)}">{len(workstreams)}</div>
                    <div class="stat-label">Active Workstreams</div>
                </div>
            </div>"""
    content = replace_marker(content, 'progress-summary-stats', stats_html)

    # 2. Progress bars
    bars_html = '            <div class="progress-bars">\n'
    for i, ws in enumerate(workstreams):
        delay = i * 150
        pct = ws.get('progress_percent', 0)
        label = esc(ws.get('phase_label', ws.get('status', 'In Progress')))
        summary = esc(ws.get('status_summary', ''))
        name = esc(ws['name'])
        bars_html += f"""                <div class="progress-card reveal" data-reveal-delay="{delay}">
                    <h3>{name}</h3>
                    <div class="progress-bar-container">
                        <div class="progress-bar" data-target-width="{pct}"></div>
                    </div>
                    <div class="progress-label">
                        <span>{label}</span>
                        <span class="progress-percentage">{pct}%</span>
                    </div>
                    <p class="progress-description">{summary}</p>
                </div>
"""
    bars_html += '            </div>'
    content = replace_marker(content, 'progress-bars', bars_html)

    # 3. Timeline (all portal milestones, reverse chronological)
    timeline_html = ""
    for i, m in enumerate(portal_milestones):
        delay = i * 40
        is_complete = m['status'] == 'complete'
        item_class = 'complete' if is_complete else 'upcoming'
        if is_complete:
            tag_html = '<span class="timeline-tag complete">✓ Complete</span>'
        else:
            tag_html = '<span class="timeline-tag upcoming">→ Upcoming</span>'

        tags = m.get('tags', [])
        extra_tags = ''.join(f'\n                            <span class="timeline-tag">{esc(t)}</span>' for t in tags)

        timeline_html += f"""                <div class="timeline-item {item_class} reveal" data-reveal-delay="{delay}">
                    <div class="timeline-date">{fmt_date(m['date'])}</div>
                    <div class="timeline-content">
                        <div class="timeline-title">{esc(m['title'])}</div>
                        <div class="timeline-description">{esc(m['description'])}</div>
                        <div class="timeline-meta">
                            {tag_html}{extra_tags}
                        </div>
                    </div>
                </div>
"""
    content = replace_marker(content, 'progress-timeline', timeline_html.rstrip())

    # 4. Phase breakdowns
    phases_html = '            <div class="phase-breakdown">\n'
    ws_icons = {'lemlist': '📱', 'loopio': '📝'}
    for i, ws in enumerate(workstreams):
        delay = i * 150
        icon = ws_icons.get(ws['id'], '📋')
        phases_html += f'                <div class="phase-card reveal" data-reveal-delay="{delay}">\n'
        phases_html += f'                    <h3>{icon} {esc(ws["name"])}</h3>\n'

        for phase in ws['phases']:
            tasks = phase['tasks']
            all_complete = all(t.get('status') == 'complete' for t in tasks)
            any_active = any(t.get('status') in ('in_progress', 'complete') for t in tasks) and not all_complete

            if all_complete:
                check_html = '<div class="phase-check complete">✓</div>'
                phase_suffix = "(Complete)"
            elif any_active:
                check_html = '<div class="phase-check" style="background-color: rgba(77, 192, 199, 0.2); color: var(--color-ev-teal);">●</div>'
                phase_suffix = "(In Progress)"
            else:
                check_html = '<div class="phase-check">◯</div>'
                phase_suffix = f"(Target: {fmt_date(phase['end'])})"

            phases_html += f"""                    <div class="phase-item">
                        {check_html}
                        <div class="phase-text">{esc(phase['name'])} {phase_suffix}</div>
                    </div>
"""
        phases_html += '                </div>\n'
    phases_html += '            </div>'
    content = replace_marker(content, 'progress-phases', phases_html)

    # 5. Task tables
    today = datetime.now().strftime('%Y-%m-%d')
    for ws in workstreams:
        marker_name = f"progress-tasks-{ws['id']}"
        rows_html = ""
        # Collect all tasks from all phases, newest first
        all_tasks = []
        for phase in ws['phases']:
            for task in phase['tasks']:
                all_tasks.append(task)
        # Sort: pending/in_progress first (by due date desc), then complete (by due date desc)
        def task_sort_key(t):
            status_order = {'in_progress': 0, 'pending': 1, 'complete': 2}
            return (status_order.get(t.get('status', 'pending'), 1), t.get('due', ''))

        all_tasks.sort(key=task_sort_key)

        for task in all_tasks:
            status = task.get('status', 'pending')
            due = task.get('due', '')

            if status == 'complete':
                badge = '<span class="status-badge status-complete">Complete</span>'
            elif status == 'in_progress':
                badge = '<span class="status-badge status-in-progress">In Progress</span>'
            elif due and due < today:
                badge = '<span class="status-badge status-overdue" style="background-color: rgba(239, 68, 68, 0.1); color: #ef4444;">Overdue</span>'
            else:
                badge = '<span class="status-badge status-upcoming">Upcoming</span>'

            due_display = fmt_date(due) if due else 'TBD'
            rows_html += f"""                    <tr>
                        <td class="task-name">{esc(task['task'])}</td>
                        <td>{esc(task.get('owner', ''))}</td>
                        <td>{due_display}</td>
                        <td>{badge}</td>
                    </tr>
"""
        content = replace_marker(content, marker_name, rows_html.rstrip())

    # 6. Footer date
    date_str = datetime.now().strftime('%b ') + str(datetime.now().day) + ', ' + str(datetime.now().year)
    footer_html = f'        <p style="margin-top: var(--space-2);">Last updated: {date_str}</p>'
    content = replace_marker(content, 'progress-footer-date', footer_html)

    with open(portal_path, 'w') as f:
        f.write(content)

    print(f"✓ Updated portal/progress.html (stats, progress bars, timeline, phases, task tables)")
    print(f"  Overall: {overall_pct}%, {complete_milestones}/{total_milestones} milestones, {metrics['days_left']} days left")


def generate_markdown(cfg: dict) -> str:
    """Generate full timeline markdown"""
    c = cfg['client']
    deadline = datetime.strptime(c['deadline'], '%Y-%m-%d')
    days_left = (deadline - datetime.now()).days

    md = f"""# {c['name']} Engagement Timeline
## Internal Review | {datetime.now().strftime('%B %d, %Y')}

**Contact:** {c['primary_contact']} ({c['contact_role']})
**Deadline:** {c['deadline_label']} ({c['deadline']})
**Days Remaining:** ~{days_left} days
**Budget:** Approved

---

## Executive Summary

"""

    # Workstreams
    for ws in cfg['workstreams']:
        md += f"""## {ws['name']}

**Goal:** {ws['goal']}
**Scope:** {ws['scope']}
**Success Metric:** {ws['success_metric']}

### Phases
"""
        for phase in ws['phases']:
            md += f"\n#### {phase['name']} ({phase['start']} - {phase['end']})\n\n"
            md += "| Task | Owner | Due |\n|------|-------|-----|\n"
            for t in phase['tasks']:
                milestone = " 🎯" if t.get('milestone') else ""
                md += f"| {t['task']}{milestone} | {t['owner']} | {t['due']} |\n"
        md += "\n---\n\n"

    # Risks
    md += "## Risks\n\n| Risk | Likelihood | Impact | Mitigation |\n|------|------------|--------|------------|\n"
    for r in cfg['risks']:
        md += f"| {r['risk']} | {r['likelihood']} | {r['impact']} | {r['mitigation']} |\n"

    # Milestones
    md += "\n---\n\n## Key Milestones\n\n"
    for m in cfg['milestones']:
        crit = "🎯 " if m.get('critical') else ""
        md += f"- **{m['date']}** — {crit}{m['event']}\n"

    # Open questions
    md += "\n---\n\n## Open Questions\n\n"
    for q in cfg['open_questions']:
        md += f"- [ ] {q}\n"

    md += f"\n---\n\n*Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n"
    return md

def main():
    config_path = sys.argv[1] if len(sys.argv) > 1 else "config.json"
    output_dir = Path(sys.argv[2] if len(sys.argv) > 2 else ".")

    cfg = load_config(config_path)
    client = cfg['client']['name'].lower().replace(' ', '-')

    # Generate files
    gantt = generate_gantt(cfg)
    stakeholders = generate_stakeholder_map(cfg)
    md = generate_markdown(cfg)

    # Write outputs
    (output_dir / f"{client}-gantt.mermaid").write_text(gantt)
    (output_dir / f"{client}-stakeholders.mermaid").write_text(stakeholders)
    (output_dir / f"{client}-timeline.md").write_text(md)

    # Update index.html Mermaid diagrams and stakeholder class assignments
    update_index_html_mermaid(cfg, output_dir / "index.html")
    update_index_html_classes(cfg, output_dir / "index.html")

    # Update portal pages
    portal_dir = output_dir / "portal"
    if portal_dir.exists():
        portal_index = portal_dir / "index.html"
        portal_progress = portal_dir / "progress.html"
        if portal_index.exists():
            update_portal_index(cfg, portal_index)
        if portal_progress.exists():
            update_portal_progress(cfg, portal_progress)

    print(f"✓ Generated files for {cfg['client']['name']}")
    print(f"  - {client}-gantt.mermaid")
    print(f"  - {client}-stakeholders.mermaid")
    print(f"  - {client}-timeline.md")
    print(f"  - index.html (Mermaid diagrams + stakeholder classes updated)")
    if portal_dir.exists():
        print(f"  - portal/index.html (hero stats, milestones, workstream cards)")
        print(f"  - portal/progress.html (timeline, tasks, progress bars)")

if __name__ == "__main__":
    main()
