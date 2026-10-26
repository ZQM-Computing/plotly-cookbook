# 04 — Export

Exporting a standalone HTML figure: `write_html` with
`include_plotlyjs=True` embeds the full plotly.js bundle, so the file
opens in a browser with no server and no network. Two synthetic traces
prove the content survived the round trip.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv).

## Expected output

```text
Standalone file: standalone_figure.html, bytes: <positive integer>, traces: 2
```

The byte count varies with the plotly version because the bundle is
embedded — it is large by construction. The assertions that must hold
are: the file exists, is non-empty, mentions plotly, has 2 traces,
and the bar values are [5, 9, 4].

## Failure behavior

- An unexpectedly small file (a few KB) — the bundle did not embed;
  check the `include_plotlyjs` argument.
- A different trace count or bar values — the figure data was edited;
  restore `run.py`.
- `ModuleNotFoundError: plotly` — you are not in the wave11 venv; use
  the full venv Python path above.

## Tradeoff, documented

`include_plotlyjs="cdn"` writes a much smaller file but needs network
at view time; `include_plotlyjs=True` (used here) is fully standalone.
Choose per distribution: email/attach the standalone form, serve the
CDN form from a page that already loads plotly.js.

## Versions and evidence

- Tool: plotly 7.1.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked).
- Evidence level: design-only (gate 1 target). Trace count and bar
  values were derived during drafting; the actual exported byte count
  against fleet plotly is **to confirm at validation**.
