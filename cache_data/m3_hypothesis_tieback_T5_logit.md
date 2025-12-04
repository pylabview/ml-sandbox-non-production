# Hypothesis tie-back — T=5, model=BaselineLogit

## H1. Inverted-U for Breadth_T (Breadth ≥ 1)
- **PDP peak breadth:** 1  (drop to tail: 0.0684; drop to b=1: 0.0000)
- **ICE peaks:** median=1 (IQR 1–1), share in [1,2,3] = 100.0%; post-peak ↓ share≥60% = 100.0%
- **Evidence:** moderate

## H2. PaceSlack_T helps then plateaus
- **Avg early slope:** 0.054083   |   **Avg late slope:** 0.057211   |   **Turning slack (≈ plateau):** 0.575
- **Evidence:** weak

## H3. Interaction — fast-focused vs slow-scatter
- **Fast-focused (low breadth, high slack):** p=0.39653
- **Slow-scatter (high breadth, low slack):** p=0.17583
- **Slack lift @low breadth:**  Δ=0.03565   |   **@high breadth:**  Δ=0.03026   |   **Synergy (low−high):** +0.00539
- **High-slack gap (low breadth − high breadth):** +0.19045
- **Evidence:** strong

> Notes: Evidence levels are heuristic (strong/moderate/weak) based on peak location, declines after peak, slope patterns, and Δ-of-Δ interaction. For CIs, bootstrap ICE rows and recompute summaries.