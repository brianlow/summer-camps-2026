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
  - would like camps geared towards her interests but also want one or two that will be outdoors and/or skills focused

## Process

1. Research camp
2. Save results to CAMP-{provider}.md (e.g. CAMPS-UofC.md, CAMPS-SAIT.md) to keep files manageable and allow parallel research
3. Update TODO.md


Notes:
- **TODO.md** tracks outstanding and in-progress work, keep this up to date
- Keep **PLAN.md** updated with decisions and process learnings
- Camp files are split by provider
- Do not use Facebook as a research source
- Ask user to confirm when unsure before making changes


## Camp Entry Template

```
## Camp Name *(Grade range | Girls-only or Mixed)*

**For her:** [What's fun/exciting, plain language]
**For you:** [Skills/themes, indoor/outdoor, swimming info]

- **Indoor/Outdoor:** ...
- **Hours:** ... Mon–Fri (full week) or note if shorter
- **Price:** $X/week (note if first week is cheaper)
- **Location:** ... — ~X min from West Hillhurst
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

An interactive map of all camps lives at `map.csv` and is intended for import into [Google My Maps](https://mymaps.google.com).

### Importing

1. Go to [mymaps.google.com](https://mymaps.google.com) → **Create a new map**
2. Click **Add layer** → **Import** → upload `map.csv`
3. Google will ask which column to use for location — choose **Address**
4. Google will ask which column to use for pin titles — choose **Name**
5. After import, click **Style by data column** → choose **Category** to colour pins by theme

### Categories (pin colours)

| Category | Examples |
|---|---|
| STEM & Tech | Robotics, coding, engineering, electronics |
| Arts & Design | Architecture, game design, animation, drama |
| Science | Detective science, geography, crafty science |
| Outdoor & Nature | Nature hikes, outdoor exploration |
| Sports | Soccer, climbing, track & field, gymnastics |

### CSV columns

| Column | Notes |
|---|---|
| Name | Short form: `Provider (Topic)` |
| Address | Full street address for geocoding. UCalgary downtown camps are at 801 7 Ave SW (SAPL building). |
| Category | One of the five categories above |
| Description | 1–2 sentence summary + link to the CAMPS-*.md file |

### Keeping the map up to date

- **When adding a new camp:** add a row to `map.csv` following the format above
- **When a provider is removed:** delete the corresponding rows
- **When spots change:** update the Description field if the status note is relevant (e.g. waitlisted)
- **UCalgary downtown address:** Confirmed as **801 7 Ave SW, Calgary, AB** — UCalgary's SAPL building (office tower conversion, opened Winter 2026), one block from 8th Street LRT station
