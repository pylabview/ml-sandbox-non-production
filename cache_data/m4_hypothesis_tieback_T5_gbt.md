# Hypothesis tie‑back — T=5, model=HistGB

## H1. Inverted‑U for Breadth_T (Breadth ≥ 1)
- **PDP peak breadth:** 1  (drop to tail: 0.3231; drop to b=1: 0.0000)
- **ICE peaks:** median=1 (IQR 1–1), share in [1,2,3] = 100.0%; post‑peak ↓ share≥60% = 99.9%
- **Evidence:** moderate

## H2. PaceSlack_T helps then plateaus
- **Avg early slope:** -0.268974   |   **Avg late slope:** -0.015125   |   **Turning slack (≈ plateau):** 0.000
- **Evidence:** moderate

## H3. Interaction — fast‑focused vs slow‑scatter
- **Fast‑focused (low breadth, high slack):** p=0.23968
- **Slow‑scatter (high breadth, low slack):** p=0.10388
- **Slack lift @low breadth:**  Δ=-0.35524   |   **@high breadth:**  Δ=-0.00479   |   **Synergy (low−high):** -0.35044
- **High‑slack gap (low breadth − high breadth):** +0.14059
- **Evidence:** moderate

> Notes: Evidence levels are heuristic (strong/moderate/weak) based on peak location, declines after peak, slope patterns, and Δ‑of‑Δ interaction. For statistical CIs, re‑sample ICE rows and recompute these summaries.