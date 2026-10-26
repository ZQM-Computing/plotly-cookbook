# 03-scatter-geo (plotly) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Scatter map over synthetic points: lat/lon + sized markers + labels.
# Synthetic coordinates ONLY (a made-up grid, not a real place).
# Writes scatter_geo.html; prints a summary.
import plotly.graph_objects as go

LATS = [10.010, 10.020, 10.030, 10.040, 10.050, 10.015, 10.035]
LONS = [20.010, 20.030, 20.010, 20.040, 20.020, 20.035, 20.015]
NAMES = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]
SIZES = [10, 20, 15, 25, 12, 18, 22]

fig = go.Figure(go.Scattergeo(
    lat=LATS, lon=LONS, text=NAMES,
    marker={"size": SIZES, "color": "darkblue"},
    mode="markers+text",
))
fig.update_layout(title="Synthetic scatter-geo")
fig.update_geos(showland=True)

assert len(LATS) == 7 and len(LONS) == 7 and len(NAMES) == 7
assert sum(SIZES) == 122  # 10+20+15+25+12+18+22

out = "scatter_geo.html"
fig.write_html(out)
html = open(out, encoding="utf-8").read()
assert len(html) > 0 and "P1" in html and "P7" in html
print(f"Points: {len(LATS)}, size sum: {sum(SIZES)}")
