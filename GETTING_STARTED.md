# Getting Started — QGIS Portfolio Setup

## Step 1: Install QGIS
Download the LTS version from: https://qgis.org/en/site/forusers/download.html
(LTS = Long Term Release — most stable for learning)

---

## Step 2: Set Up This Repo

```bash
git init qgis-portfolio
cd qgis-portfolio
git remote add origin https://github.com/YOUR_USERNAME/qgis-portfolio.git
```

---

## Step 3: Download Data (in order)

### Project 01
- [ ] Download US state shapefiles from Census TIGER (see project-01/data/README.md)
- [ ] Download 2-3 HIFLD layers from hifld-geoplatform.opendata.arcgis.com

### Project 02
- [ ] Download HHS breach CSV from ocrportal.hhs.gov
- [ ] Run `docs/preprocess_hhs_data.py` to generate the aggregated CSV
- [ ] Reuse state shapefiles from Project 01

### Project 03
- [ ] Use Overpass Turbo to export OSM GeoJSON for a chosen urban area
- [ ] See project-03/data/README.md for the query to use

---

## Step 4: Build Each Project in QGIS

### Suggested order:
1. **Project 01** — Best introduction to QGIS layer management and symbology
2. **Project 02** — Builds on 01, adds table joins and heatmap rendering
3. **Project 03** — Introduces geometry tools, topology checker, and editing

### For each project:
- Save your QGIS project file as `.qgz` into the project folder root
- Export your final map as PNG (300 DPI) to the `maps/` folder
- Export a PDF version as well

---

## Step 5: Commit and Push

```bash
git add .
git commit -m "Add Project 01: Critical Infrastructure Mapping"
git push origin main
```

Push after completing each project — this shows active development history.

---

## Recommended QGIS Learning Resources

| Resource | Format | Best for |
|----------|--------|---------|
| [QGIS Official Training Manual](https://docs.qgis.org/3.34/en/docs/training_manual/) | Web docs | Structured foundation |
| [Spatial Thoughts — QGIS Beginner](https://www.youtube.com/@spatialthoughts) | YouTube | Visual, hands-on |
| [QGIS Tutorials and Tips](https://www.qgistutorials.com/) | Web tutorials | Task-specific how-tos |

---

## Tips for Working Efficiently

- Save your QGIS project often (Ctrl+S) — QGIS can be memory-intensive
- Use the **Browser Panel** to navigate and drag layers directly onto the canvas
- The **Layer Properties > Symbology** tab is where most visual styling happens
- **Processing Toolbox** (Ctrl+Alt+T) contains most spatial analysis functions
- When in doubt: right-click the layer > Open Attribute Table to inspect your data
