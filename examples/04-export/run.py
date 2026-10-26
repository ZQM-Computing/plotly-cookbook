# 04-export (plotly) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Exporting a standalone HTML figure: write_html with the full plotly.js
# bundle embedded, so the file opens in a browser with no server and no
# network. The CDN variant (smaller file, needs network at view time)
# is noted in the README, not used here. Synthetic values ONLY.
# Writes standalone_figure.html; prints a summary.
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(x=["A", "B", "C"], y=[5, 9, 4], name="bars"))
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 7, 5],
                         mode="lines+markers", name="line"))
fig.update_layout(title="Standalone export (synthetic data)")

assert len(fig.data) == 2
assert list(fig.data[0].y) == [5, 9, 4]

out = "standalone_figure.html"
fig.write_html(out, include_plotlyjs=True)
html = open(out, encoding="utf-8").read()
assert len(html) > 0 and "plotly" in html.lower()
print(f"Standalone file: {out}, bytes: {len(html)}, traces: {len(fig.data)}")
