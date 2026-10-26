# 02 — Choropleth

A choropleth map from a synthetic GeoJSON dict: three regions colored
by value, no GeoPandas required. Locations and colors are plain lists
keyed to the GeoJSON `name` property.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv).

## Expected output

```text
Regions: 3, mean value: 30.0
```

Derivation: values 12 + 30 + 48 = 90; 90 / 3 = 30.0. The assertions
that must hold are: 3 regions, mean 30.0, and a non-empty HTML file
mentioning "North".

## Failure behavior

- A different mean — the value list was edited; restore `VALUES`
  from `run.py`.
- A blank map at view time — `fitbounds="locations"` behavior with a
  custom GeoJSON dict is a validation item: if the viewport does not
  frame the three regions, the fitbounds/scope settings need adjusting
  against fleet plotly, not the data.
- `ModuleNotFoundError: plotly` — you are not in the wave11 venv; use
  the full venv Python path above.

## Versions and evidence

- Tool: plotly 7.1.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked).
- Deviation, documented: the seed plans "Choropleth maps from
  DataFrames". This pattern uses plain lists + a GeoJSON dict so it
  runs without GeoPandas (not in the wave11 package list). The
  DataFrame variant is a validation item, not asserted here.
- Evidence level: design-only (gate 1 target). Region count and mean
  were derived during drafting; running them against the fleet plotly
  environment is **to confirm at validation**.
