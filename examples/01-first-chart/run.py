# 01-first-chart (plotly) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# A first figure: one line trace, one bar trace, one scatter trace.
# Synthetic values ONLY. Writes first_chart.html; prints a summary.
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5], y=[2, 5, 3, 8, 6],
                         mode="lines+markers", name="line"))
fig.add_trace(go.Bar(x=["A", "B", "C", "D"], y=[4, 7, 3, 9], name="bars"))
fig.add_trace(go.Scatter(x=[1, 2, 3, 4, 5, 6], y=[1, 4, 2, 5, 3, 6],
                         mode="markers", name="scatter"))
fig.update_layout(title="First chart (synthetic data)")

assert len(fig.data) == 3
line_y = list(fig.data[0].y)
assert sum(line_y) == 24  # 2 + 5 + 3 + 8 + 6

out = "first_chart.html"
fig.write_html(out)
html = open(out, encoding="utf-8").read()
assert len(html) > 0 and "plotly" in html.lower()
print(f"Traces: {len(fig.data)}, line sum: {sum(line_y)}")
