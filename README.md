# Geospatial Analysis Portfolio — Rashidah Carr

**QGIS | Critical Infrastructure | Cybersecurity | AI Data Quality**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/rashidahcarr)
[![Email](https://img.shields.io/badge/Email-rcarr%40the97group.com-lightgrey)](mailto:rcarr@the97group.com)

---

## About This Portfolio

This repository documents geospatial analysis projects built with QGIS, developed at the intersection of **cybersecurity, critical infrastructure, and AI data quality**. Each project applies GIS methodology to real-world public datasets, with an emphasis on data integrity, annotation accuracy, and actionable visual outputs.

**Background:** I bring 20+ years of experience in cybersecurity, data architecture, and AI governance, including work supporting CISA/DHS, ISC2 exam development, and AI/ML data annotation. This portfolio bridges that domain expertise with geospatial analysis tools and techniques.

---

## Projects

| # | Project | Focus Area | Key Skills |
|---|---------|------------|------------|
| 01 | [Critical Infrastructure Sector Mapping](#project-01) | CISA / National Security | Layer styling, public data ingestion, choropleth maps |
| 02 | [Cybersecurity Incident Heatmap](#project-02) | Breach data visualization | Heatmaps, state-level aggregation, data cleaning |
| 03 | [Geospatial Data QA for AI Training](#project-03) | AI/ML data quality | Feature annotation, QA documentation, error flagging |

---

## Project 01

### Critical Infrastructure Sector Mapping
> *Visualizing the geographic distribution of US critical infrastructure using public CISA data*

**Objective:** Map and analyze the physical distribution of critical infrastructure assets across CISA's 16 designated sectors, identifying geographic concentration and coverage gaps relevant to national security planning.

**Data Sources:**
- [US Census Bureau TIGER/Line Shapefiles 2025](https://www.census.gov/cgi-bin/geo/shapefiles/index.php) — state boundaries base layer
- [HIFLD Open Data — Electric Power Transmission Lines](https://hifld-geoplatform.hub.arcgis.com/) — Energy sector
- [HIFLD Open Data — Hospitals 2020](https://hifld-geoplatform.hub.arcgis.com/) — Health & Public Health sector
- [EIA Natural Gas Inter/Intrastate Pipelines](https://www.eia.gov/maps/layer_info-m.php) — Energy sector

**Methodology:**
1. Ingested 2025 US Census TIGER state boundary shapefiles as the base layer (EPSG:4326)
2. Loaded and styled three CISA sector infrastructure layers:
   - Electric power transmission lines (Energy sector) — orange, 0.3mm stroke, 40% opacity
   - Natural gas inter/intrastate pipelines (Energy sector) — yellow, 0.2mm stroke, 30% opacity
   - HIFLD hospital locations (Health & Public Health sector) — red points, 0.8mm size, 70% opacity
3. Ordered layers by geometry type (points above lines above polygons) for optimal readability
4. Created print layout with title, legend, scale bar, and north arrow
5. Exported at 300 DPI in PNG and PDF formats

**Key Findings:**
- Electric power transmission and natural gas pipeline networks show highest density in the eastern US, particularly along the Gulf Coast and Mid-Atlantic corridors
- Hospital distribution closely mirrors population density, with notable gaps in rural western states indicating potential healthcare access vulnerabilities
- Energy infrastructure concentration in the Southeast aligns with CISA threat modeling priorities for grid resilience
- Alaska shows meaningful infrastructure presence across all three sectors despite its geographic isolation

**Tools Used:** QGIS 3.x, HIFLD Open Data, EIA Pipeline Data, US Census TIGER/Line Shapefiles 2025

**Files:**
```
project-01-critical-infrastructure/
├── data/               # Source shapefiles and CSV inputs (see data/README.md for sources)
├── maps/               # Exported PNG and PDF map outputs
└── docs/               # Methodology notes and field mapping documentation
```

**Map Preview:**

![US Critical Infrastructure — Electric Power Transmission, Natural Gas Pipelines, and Hospitals](project-01-critical-infrastructure/maps/Project-01-Critical-Infrastructure.png)

---

## Project 02

### Cybersecurity Incident Heatmap
> *State-level visualization of reported healthcare data breaches using HHS public breach data*

**Objective:** Transform publicly reported cybersecurity breach data into a geographic heatmap to identify regional vulnerability patterns and support risk-based resource prioritization.

**Data Sources:**
- [HHS Office for Civil Rights Breach Portal](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf) — "Wall of Shame" public dataset
- US Census Bureau state boundary shapefiles

**Methodology:**
1. Downloaded and cleaned HHS breach CSV (filtered for hacking/IT incidents)
2. Aggregated incident count and individuals affected by state
3. Joined tabular breach data to state polygon shapefile via state name field
4. Applied quantile choropleth classification across 5 break points
5. Created secondary heatmap layer using incident centroid point data
6. Exported dual-view layout: choropleth overview + regional zoom inset

**Key Findings:**
- States with higher population density and larger healthcare networks report significantly more incidents
- Hacking/IT incidents account for the majority of individuals affected, outpacing physical theft/loss
- Geographic clustering suggests regional factors (healthcare consolidation, attack campaigns) may drive incident patterns

**Tools Used:** QGIS 3.x, HHS OCR Public Data, Python (pandas) for pre-processing, US Census shapefiles

**Files:**
```
project-02-cybersecurity-incident-heatmap/
├── data/               # Cleaned HHS breach CSV and state shapefiles
├── maps/               # Choropleth and heatmap exports
└── docs/               # Data cleaning notes and classification methodology
```

**Map Preview:**

*[Map export will be added upon QGIS project completion]*

---

## Project 03

### Geospatial Data QA for AI Training
> *Simulating a geospatial data annotation and quality assurance workflow for AI/ML model training*

**Objective:** Demonstrate a structured QA process for geospatial training data — identifying labeling inconsistencies, flagging problematic features, and documenting corrections in a format suitable for AI model refinement pipelines.

**Background:** This project directly mirrors real-world AI data annotation workflows. Drawing on my experience as an AI Data Annotator at RWS and my work with CISA training content, this project applies those QA principles to geospatial feature data.

**Data Sources:**
- OpenStreetMap export via [Overpass Turbo](https://overpass-turbo.osm.ch/) — building footprints, road networks
- USGS National Map public layers

**Methodology:**
1. Exported a sample region from OpenStreetMap (approx. 5km x 5km urban area)
2. Loaded feature layers into QGIS and performed geometry validity checks
3. Identified and documented annotation issues:
   - Missing attribute fields
   - Overlapping polygons
   - Topology errors (gaps, slivers)
   - Misclassified feature types
4. Applied corrections using QGIS editing tools and documented each change
5. Produced a QA log (CSV) recording: feature ID, issue type, action taken, confidence score

**QA Issue Categories Identified:**

| Issue Type | Description | Action Taken |
|------------|-------------|--------------|
| Missing attributes | Feature present, label field null | Inferred from surrounding context; flagged low confidence |
| Overlapping polygons | Building footprints overlap roads | Adjusted vertices; documented for human review |
| Topology gaps | Slivers between adjacent parcels | Snapped to nearest vertex using topology checker |
| Misclassification | Residential labeled as commercial | Corrected via satellite imagery cross-reference |

**Tools Used:** QGIS 3.x, Overpass Turbo, QGIS Topology Checker plugin, Excel (QA log)

**Files:**
```
project-03-geospatial-data-qa/
├── data/               # OSM exports and source layers
├── maps/               # Before/after comparison exports
└── docs/               # QA log CSV, issue taxonomy, methodology notes
```

**Map Preview:**

*[Map export will be added upon QGIS project completion]*

---

## Technical Skills Demonstrated

| Skill | Projects |
|-------|---------|
| Shapefile ingestion and layer management | 01, 02, 03 |
| Attribute table joins | 01, 02 |
| Choropleth and graduated symbology | 01, 02 |
| Heatmap / density visualization | 02 |
| Topology checking and geometry validation | 03 |
| Feature annotation and QA documentation | 03 |
| Print layout and map export | 01, 02, 03 |
| Python pre-processing (pandas) | 02 |
| Public data sourcing (CISA, HHS, OSM, USGS) | 01, 02, 03 |

---

## Domain Expertise

This portfolio is informed by professional experience across:

- **Critical Infrastructure Security** — Cybersecurity Instructor/Technical Lead, Edgesource supporting CISA/DHS
- **AI Data Quality** — AI Data Annotator, RWS (machine learning dataset annotation)
- **Risk and Compliance** — CISSP, CySA+, ISO 27001/42001 Lead Auditor; NIST, GDPR, HIPAA frameworks
- **Data Architecture** — Data Architect, Delaware North America; master data governance and migration

---

## Contact

**Rashidah Carr**
Cybersecurity | AI Governance | Geospatial Analysis
Atlanta, GA
rcarr@the97group.com | 973.704.8317
[the97group.com](https://the97group.com)
