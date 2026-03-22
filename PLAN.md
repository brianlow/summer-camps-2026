# Summer Camps 2026 — Research Plan

We are planning summer camps for my daughter

## Context
- **Child:**
  - 6-year-old girl, turning 7 during the summer, entering Grade 2 after summer
  - tends towards introverted, prefers indoors, prefers being around girls
  - play style: storytelling rather than building
  - top tier interests: arts, crafts, reading, unicorns,
  - mid tier interests: dancing, singing, lego, scootering, rollerskating
- **Family:**
  - location: West Hillhurst, Calgary (NW Calgary, ~10 min from UCalgary campus)
  - would like camps geared towards her interests but also want some that will be outdoors and/or skills focused

## Process

1. Research camp
2. Save results to CAMP-{provider}.md (e.g. CAMPS-UofC.md, CAMPS-SAIT.md) to keep files manageable and allow parallel research
3. Update TODO.md
4. Update README.md
5. Update CALENDAR.md
6. Update map.geojson


Notes:
- **TODO.md** tracks outstanding and in-progress work, keep this up to date
- **README.md** summarized list of camps for quick review
- **CALENDAR.md** info organized by week
- Keep **PLAN.md** updated with decisions and process learnings
- Camp files are split by provider
- Do not use Facebook as a research source
- Ask user to confirm when unsure before making changes
- **Do NOT make up camp descriptions.** If website content is unavailable, leave descriptions blank or note "description needed" — never invent placeholder text. Ask the user to provide the content instead.
- Prefer WebFetch over the Playwright MCP. Fetch is much faster and uses fewer tokens.


## Camp Entry Template

```
## Camp Name *(Grade range | Girls-only or Mixed)*

**For her:** [What's fun/exciting, plain language]
**For you:** [Skills/themes, indoor/outdoor, swimming info]

- **Indoor/Outdoor:** ...
- **Hours:** ... Mon–Fri (full week) or note if shorter
- **Price:** $X/week (note if first week is cheaper)
- **Location:** ... — ~X min from West Hillhurst ([map](https://maps.google.com/?q=ADDRESS))
- **Prerequisites:** None / [what's needed]
- **More info / Book:** [URL]
- **Spots:**

| Dates | Spots |
|---|---|
| ... | ... |
```

## Filtering Rules
- **Hours:** End time must be 3:30pm or later. Half-day camps excluded. Check for aftercare.
- **Skating:** Child does not know how to skate — exclude skating camps
- **Distance:** Nearby Calgary (~10-15 min) is ideal. Cochrane (~40 min) — keeping as backup
- **Gender:** Girls-only and mixed both OK


## Interactive Map

An interactive map of all camps lives at `map.geojson`. GitHub renders it automatically as a Leaflet.js map — just open the file on GitHub to see it.

### Categories (pin colours)

| Category | Marker colour | Examples |
|---|---|---|
| STEM & Tech | Blue `#0075A2` | Robotics, coding, engineering, electronics |
| Arts & Design | Purple `#7B2D8B` | Architecture, game design, animation, drama |
| Science | Green `#1E8449` | Detective science, geography, crafty science |
| Outdoor & Nature | Orange `#D4680A` | Nature hikes, outdoor exploration |
| Sports | Red `#C0392B` | Soccer, climbing, track & field, gymnastics |

### GeoJSON feature properties

| Property | Notes |
|---|---|
| name | Short form: `Provider (Topic)` |
| address | Full street address. UCalgary downtown camps are at 801 7 Ave SW (SAPL building). |
| category | One of the five categories above |
| description | 1–2 sentence summary + link to the CAMPS-*.md file |
| marker-color | Hex colour matching category above |
| marker-symbol | Maki icon name (`star`, `art-gallery`, `college`, `park`, `swimming`, `music`) |

### Keeping the map up to date

- **When adding a new camp:** add a Feature entry to `map.geojson` with coordinates (use Nominatim or similar to geocode) and properties following the format above
- **When a provider is removed:** delete the corresponding Feature entries
- **When spots change:** update the description property if the status note is relevant (e.g. waitlisted)
- **UCalgary downtown address:** Confirmed as **801 7 Ave SW, Calgary, AB** — UCalgary's SAPL building (office tower conversion, opened Winter 2026), one block from 8th Street LRT station
