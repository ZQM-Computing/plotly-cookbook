# 02-choropleth (plotly) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Choropleth map from a synthetic GeoJSON dict + value list.
# No GeoPandas required: locations and colors are plain lists keyed
# to the GeoJSON properties. Synthetic regions and values ONLY.
# The fitbounds/scope behavior is a validation item (see README).
# Writes choropleth.html; prints a summary.
import plotly.express as px

GEOJSON = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature", "properties": {"name": "North"},
         "geometry": {"type": "Polygon", "coordinates": [[[20.00, 10.04], [20.02, 10.04], [20.02, 10.05], [20.00, 10.05], [20.00, 10.04]]]}},
        {"type": "Feature", "properties": {"name": "Central"},
         "geometry": {"type": "Polygon", "coordinates": [[[20.00, 10.02], [20.02, 10.02], [20.02, 10.04], [20.00, 10.04], [20.00, 10.02]]]}},
        {"type": "Feature", "properties": {"name": "South"},
         "geometry": {"type": "Polygon", "coordinates": [[[20.00, 10.00], [20.02, 10.00], [20.02, 10.02], [20.00, 10.02], [20.00, 10.00]]]}},
    ],
}

LOCATIONS = ["North", "Central", "South"]
VALUES = [12, 30, 48]
mean_value = sum(VALUES) / len(VALUES)

fig = px.choropleth(
    geojson=GEOJSON,
    locations=LOCATIONS,
    featureidkey="properties.name",
    color=VALUES,
    color_continuous_scale="Viridis",
    title="Synthetic choropleth",
)
fig.update_geos(fitbounds="locations", visible=False)

assert len(LOCATIONS) == 3 and mean_value == 30.0

out = "choropleth.html"
fig.write_html(out)
html = open(out, encoding="utf-8").read()
assert len(html) > 0 and "North" in html
print(f"Regions: {len(LOCATIONS)}, mean value: {mean_value}")
