# 01 — First chart

A first Plotly figure: lines, bars, and scatter in three traces, all
synthetic values, saved as standalone HTML.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv).

## Expected output

```text
Traces: 3, line sum: 24
```

Derivation: line y-values 2 + 5 + 3 + 8 + 6 = 24. The assertions that
must hold are: 3 traces, line sum 24, and a non-empty HTML file
mentioning plotly.

## Failure behavior

- A different trace count or sum — the trace data was edited; restore
  `run.py`, do not adjust the assertions.
- Empty HTML — the write step failed; check the `write_html` call.
- `ModuleNotFoundError: plotly` — you are not in the wave11 venv; use
  the full venv Python path above.

## Versions and evidence

- Tool: plotly 7.1.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked).
- Evidence level: design-only (gate 1 target). Trace count and line
  sum were derived during drafting; running them against the fleet
  plotly environment is **to confirm at validation**.
