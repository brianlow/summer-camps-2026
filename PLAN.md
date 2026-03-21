# Summer Camps 2026 — Research Plan

## Context
- **Child:** 6-year-old girl entering Grade 2
- **Parent location:** West Hillhurst, Calgary (NW Calgary, ~10 min from UCalgary campus)
- **Source:** `uofc-2026-03-16.pdf` — UCalgary camps with spots remaining as of 2026-03-16

## Process
- Keep **PLAN.md** updated with decisions and process learnings
- Keep **CAMPS.md** updated as we learn about each camp
- Include URL/reference for each camp for booking or reading more
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
- **Hours:** End time must be 3:30pm or later. Half-day camps excluded.
- **Skating:** Child does not know how to skate — exclude skating camps
- **Distance:** UCalgary campus (~10 min) is ideal. Cochrane (~40 min) — keeping as backup
- **Gender:** Girls-only and mixed both OK

## URL Pattern
Camp pages: `https://activelivingportal.ucalgary.ca/Program/[slug]`
Many pages load content dynamically (JS) — static fetch may return nothing.
Confirmed working slugs:
- `totsontreks`
- `climbon`
- `minibrickbuilders`
- `minioutdoorsports`
- `ElbowValley`
- `Stopmotionanimation`
Numeric IDs also work: e.g. `/Program/2193` (City Building), `/Program/2615` (Landscape Lab), `/Program/1346` (Dinos Soccer), `/Program/1554` (Dinos T&F), `/Program/2604` (Early Technology), `/Program/2080` (GeoVenture)

## Location Notes
- **UCalgary main campus** (~10 min from West Hillhurst): most camps
- **UCalgary downtown building** (~15 min): City Building, Landscape Lab, Achieve Architecture
- **Cochrane — Spray Lake Sawmills Family Sport Centre** (~40 min): Gymnastics Recreation

## Camps Status

| Camp | Grade Range | Hours | Status |
|---|---|---|---|
| Tots on Treks | Gr 1-2 | 8:00am–3:45pm | ✅ Done |
| Climb On! | Gr 2-3 | 8:00am–3:45pm | ✅ Done |
| Mini Brick Builders | Gr 2-3 | 8:00am–3:45pm | ✅ Done (1 spot!) |
| Mini Outdoor Sports & Games | Gr 2-3 | 9:00am–4:45pm | ✅ Done (1-2 spots!) |
| Achieve Architecture | Gr 2-4 | 8:00am–3:45pm | ✅ Done — needs URL |
| City Building | Gr 2-4 | 8:00am–3:45pm | ✅ Done — needs URL |
| GeoVenture | Gr 2-4 | 9:00am–4:45pm | ✅ Done — needs URL |
| Jr. LEGO Stop Motion Animation | Gr 2-4 | 9:00am–4:45pm | ✅ Done — needs URL |
| Landscape Lab | Gr 2-4 | 8:00am–3:45pm | ✅ Done — needs URL |
| Dinos Soccer — Girls | Girls Gr 2-3 | 8:30am–4:00pm | ✅ Done — needs URL |
| Dinos Track & Field | Gr 2-5 | 9:00am–3:15pm ⚠️ | ✅ Done — needs URL |
| Early Technology | Gr 1-2 | 9:00am–4:45pm | ✅ Done — needs URL |
| Gymnastics — Recreation, Cochrane | Age 6-13 | 8:30am–4:30pm | ✅ Done — needs URL |
| ~~Elbow Valley Outdoor Camp~~ | Gr 2-4 | — | ❌ Removed — Elbow Valley residents only |
| ~~Skating Camp~~ | Gr 2-3 | — | ❌ Removed — child doesn't know how to skate |
| ~~Shooting Stars Summer Intensive~~ | Gr 1-3 | 4:10–7:30pm | ❌ Removed — evening only |

## Flags / Open Questions
- **Dinos Track & Field** ends at 3:15pm — 15 min before our 3:30pm preference. Keep or cut?
- **Achieve Architecture** price not confirmed — estimated ~$370 based on similar design camps
- **Gymnastics Cochrane** price not on website — call 403-932-7373 or email cochranegym@ucalgary.ca

## Notes
- UCalgary pool closed Aug 18–22 for maintenance (affects camps with swimming)
- No swimming Aug 4 (statutory holiday) for relevant camps
- Several camps include pool time — swim test required, lifejackets available
- Before/after care available some weeks (see PDF listings)
