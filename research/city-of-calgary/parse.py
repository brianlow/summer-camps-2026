#!/usr/bin/env python3
"""
Parse City of Calgary liveandplay.calgary.ca camp registration pages.

Each saved JSON file is a Playwright snapshot/navigate result containing an
accessibility tree. This script extracts session blocks from those trees.

Usage:
    python3 parse.py <file1.json> [file2.json ...]
    python3 parse.py arts-ventures-p*.json          # all pages for one camp
    python3 parse.py *.json                          # all camps

Output: one line per session:
    CAMP_TYPE | DATE_RANGE | AGE_GROUP | PRICE | SPACES | LOCATION
"""

import json, re, sys, os
from pathlib import Path


# ── helpers ──────────────────────────────────────────────────────────────────

def load_lines(path):
    """Load a Playwright tool-result JSON and return the accessibility-tree lines."""
    with open(path) as f:
        data = json.load(f)
    # result is either a list of {type, text} objects or a single dict
    if isinstance(data, list):
        text = "\n".join(item["text"] for item in data if item.get("type") == "text")
    else:
        text = data.get("text", "")
    return text.split("\n")


def extract_text(line):
    """Pull the plain text out of a snapshot line like '- text: Foo Bar'."""
    m = re.search(r"text: (.+)", line)
    return m.group(1).strip() if m else ""


def find_value_after(lines, start, keyword, max_lookahead=3):
    """
    From lines[start], scan forward up to max_lookahead lines for a line
    containing keyword, then return the *next* line's value (quotes stripped).
    """
    for j in range(start, min(start + 60, len(lines))):
        if keyword in lines[j]:
            for k in range(j + 1, min(j + max_lookahead + 1, len(lines))):
                raw = lines[k].strip()
                # grab content inside quotes if present, else a bare $X.XX
                m = re.search(r'"([^"]+)"', raw) or re.search(r"(\$[\d.]+)", raw)
                if m:
                    return m.group(1)
                if raw:
                    return raw
    return ""


def find_date_after(lines, start, keyword):
    for j in range(start, min(start + 60, len(lines))):
        if keyword in lines[j]:
            for k in range(j + 1, min(j + 4, len(lines))):
                m = re.search(r"\w{3}, \d{2}-\w{3}-\d{2}", lines[k])
                if m:
                    return m.group()
    return ""


def find_location_after(lines, start_j, max_lookahead=30):
    """Find the first venue name (contains 'Centre', 'Arena', 'Park', …) after the To: date."""
    keywords = ["Centre", "Arena", "Park", "School", "Community", "Field"]
    for k in range(start_j, min(start_j + max_lookahead, len(lines))):
        if "text: " in lines[k]:
            val = extract_text(lines[k])
            if any(kw in val for kw in keywords) and len(val) > 5:
                return val
    return ""


def find_to_index(lines, start):
    """Return the line index where 'To:' value is resolved, so we can scan for location after it."""
    for j in range(start, min(start + 60, len(lines))):
        if '"To:"' in lines[j] or "text: \"To:\"" in lines[j] or "- text: To:" in lines[j]:
            return j
    return start


def parse_sessions(lines, heading_pattern):
    """
    Walk lines looking for session headings matching heading_pattern.
    Returns list of dicts: heading, age, price, spaces, from_date, to_date, location.
    """
    sessions = []
    i = 0
    while i < len(lines):
        if re.search(heading_pattern, lines[i], re.IGNORECASE):
            heading = lines[i].strip()

            # extract age group from heading like "(5 - 7 years)"
            age_m = re.search(r"\((\d[\d\s\-]+(?:years?)?)\)", heading)
            age = age_m.group(1).strip() if age_m else ""

            price   = find_value_after(lines, i, '"Price:"')
            spaces  = find_value_after(lines, i, '"Spaces:"')
            from_dt = find_date_after(lines, i, '"From:"')
            to_idx  = find_to_index(lines, i)
            to_dt   = find_date_after(lines, i, '"To:"')
            location = find_location_after(lines, to_idx + 1)

            sessions.append({
                "heading":   heading,
                "age":       age,
                "price":     price,
                "spaces":    spaces,
                "from":      from_dt,
                "to":        to_dt,
                "location":  location,
            })
        i += 1
    return sessions


def pagination_page_count(lines):
    """Return the highest page number found in pagination links."""
    pages = []
    for line in lines[-150:]:
        m = re.search(r'link "(\d+)"', line)
        if m:
            pages.append(int(m.group(1)))
    return max(pages) if pages else 1


# ── camp type detection ───────────────────────────────────────────────────────

CAMP_PATTERNS = {
    "Arts Ventures":    r'heading "Arts Ventures',
    "Arts & Dance":     r'heading "Arts & dance',
    "Rock Climbing":    r'heading "Rock Climbing',
    "Rec Adventures":   r'heading "Rec Adventures: summer day camp - kids',
    "Field Sports":     r'heading "Field sports',
    "Sports":           r'heading "Sports: summer day camp',
}


def detect_camp_type(filename, lines):
    """Guess camp type from filename or first matching heading."""
    fn = Path(filename).stem.lower()
    for key in CAMP_PATTERNS:
        if key.lower().replace(" ", "-").replace("&", "dance") in fn or \
           key.lower().replace(" ", "") in fn.replace("-", "").replace("_", ""):
            return key
    # fall back: scan lines
    for key, pat in CAMP_PATTERNS.items():
        for line in lines[:200]:
            if re.search(pat, line, re.IGNORECASE):
                return key
    return "Unknown"


# ── main ─────────────────────────────────────────────────────────────────────

def process_file(path):
    lines = load_lines(path)
    camp  = detect_camp_type(path, lines)
    pat   = CAMP_PATTERNS.get(camp, r'heading "')
    sessions = parse_sessions(lines, pat)
    total_pages = pagination_page_count(lines)
    return camp, sessions, total_pages


def fmt_date(d):
    # "Mon, 06-Jul-26" → "Jul 6"
    m = re.match(r"\w+, (\d+)-(\w+)-(\d+)", d)
    if m:
        day, mon, yr = m.groups()
        return f"{mon} {int(day)}"
    return d


def print_sessions(camp, sessions):
    if not sessions:
        print(f"  (no sessions found)")
        return
    for s in sessions:
        sp = s['spaces']
        sp_str = "FULL" if sp == "0" else f"{sp} spots"
        date_str = f"{fmt_date(s['from'])}–{fmt_date(s['to'])}"
        print(f"  {date_str:20} | {s['age']:12} | {s['price']:8} | {sp_str:10} | {s['location'][:55]}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    # group by camp type across multiple pages
    by_camp = {}
    page_counts = {}
    for path in sys.argv[1:]:
        camp, sessions, total_pages = process_file(path)
        if camp not in by_camp:
            by_camp[camp] = []
        by_camp[camp].extend(sessions)
        page_counts[camp] = max(page_counts.get(camp, 1), total_pages)

    for camp, sessions in sorted(by_camp.items()):
        print(f"\n{'='*70}")
        print(f"  {camp}  (pages on site: {page_counts[camp]})")
        print(f"{'='*70}")
        print_sessions(camp, sessions)

    print()
