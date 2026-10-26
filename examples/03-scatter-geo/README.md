# 03 — Scatter geo

A scatter map over synthetic points: seven lat/lon pairs with sized
markers and labels, on a land-showing base map. All coordinates are a
made-up grid — not a real place.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv).

## Expected output

```text
Points: 7, size sum: 122
```

Derivation: sizes 10 + 20 + 15 + 25 + 12 + 18 + 22 = 122. The
assertions that must hold are: 7 latitudes, 7 longitudes, 7 names,
size sum 122, and a non-empty HTML file mentioning "P1" and "P7".

## Failure behavior

- A different point count or size sum — the coordinate/label/size
  lists were edited; restore them from `run.py`.
- Points missing from the saved file — the figure data was edited;
  the first and last labels must both appear in the HTML.
- `ModuleNotFoundError: plotly` — you are not in the wave11 venv; use
  the full venv Python path above.

## Versions and evidence

- Tool: plotly 7.1.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked).
- Evidence level: design-only (gate 1 target). Point count and size
  sum were derived during drafting; running them against the fleet
  plotly environment is **to confirm at validation**.
