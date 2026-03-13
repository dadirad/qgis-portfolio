"""
Project 02 — HHS Breach Data Pre-Processing
Cybersecurity Incident Heatmap | Rashidah Carr QGIS Portfolio

This script cleans and aggregates the HHS OCR public breach dataset
for import into QGIS as a tabular join to state boundary shapefiles.

Input:  hhs_breach_raw.csv  (downloaded from HHS OCR portal)
Output: hhs_breach_by_state.csv  (aggregated by state for QGIS join)
"""

import pandas as pd

# --- Load raw HHS breach data ---
df = pd.read_csv("hhs_breach_raw.csv")

# --- Preview columns ---
print("Columns:", df.columns.tolist())
print("Shape:", df.shape)

# --- Standardize column names (HHS column names vary by download date) ---
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# --- Filter to hacking/IT incidents only ---
df_hacking = df[df["type_of_breach"].str.contains("Hacking", case=False, na=False)]

print(f"\nTotal records: {len(df)}")
print(f"Hacking/IT incidents: {len(df_hacking)}")

# --- Aggregate by state ---
state_summary = df_hacking.groupby("state").agg(
    incident_count=("name_of_covered_entity", "count"),
    total_individuals_affected=("individuals_affected", "sum")
).reset_index()

state_summary.columns = ["state_abbr", "incident_count", "total_individuals_affected"]

# --- Sort by incident count descending ---
state_summary = state_summary.sort_values("incident_count", ascending=False)

print("\nTop 10 States by Incident Count:")
print(state_summary.head(10).to_string(index=False))

# --- Export for QGIS ---
output_path = "hhs_breach_by_state.csv"
state_summary.to_csv(output_path, index=False)
print(f"\nExported: {output_path}")

# --- Note for QGIS join ---
# In QGIS: join this CSV to the state shapefile on state_abbr = STUSPS field
# Use Vector > Joins > Add vector join in layer properties
