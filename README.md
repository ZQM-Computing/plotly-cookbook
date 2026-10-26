# Plotly Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **Plotly cookbook** — interactive charts and geo charts from Python. Installed in wave-11 (Node-1 wave11-venv, Wally spot-checked 2026-10-25). First pattern pass written below (design-only, gate 1 target). It is intended for Python developers who publish interactive charts, including map-based ones. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public. First pattern pass written (design-only, gate 1 target — none runtime-validated on the fleet yet).

**What this repository is:** Plotly patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Python developers who publish interactive charts, including map-based ones.

## Prerequisites

- plotly 7.1.0 in Node-1's wave11-venv (`C:\geo-tools\wave11-venv`, Python 3.12.10) — invoke the venv Python by full path, never bare `python` (hermes venv)
- GeoJSON dicts for the geo passes; GeoPandas is optional, not required by any pattern here

## Patterns

| # | Example | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 01 | [examples/01-first-chart](examples/01-first-chart) | A first chart: lines, bars, and scatter | Written (design-only) |
| 02 | [examples/02-choropleth](examples/02-choropleth) | Choropleth maps from GeoJSON dicts | Written (design-only) |
| 03 | [examples/03-scatter-geo](examples/03-scatter-geo) | Scatter maps over points and regions | Written (design-only) |
| 04 | [examples/04-export](examples/04-export) | Exporting standalone HTML figures | Written (design-only) |

## Repository layout

```text
plotly-cookbook/
├── examples/
│   ├── 01-first-chart/
│   ├── 02-choropleth/
│   ├── 03-scatter-geo/
│   └── 04-export/
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: all four table rows (design-only, gate 1 target)
- Validation pass: run each pattern against the fleet environment and promote to gate 3

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [folium-cookbook](https://github.com/ZQM-Computing/folium-cookbook) — Interactive Leaflet maps from Python
- [keplergl-cookbook](https://github.com/ZQM-Computing/keplergl-cookbook) — Large-scale geospatial visualization in notebooks and apps
- [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame patterns: joins, overlays, and spatial analysis
