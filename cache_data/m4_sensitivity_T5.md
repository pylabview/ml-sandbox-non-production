# Sensitivity — T=5

## A) Collinearity variants (Logit re‑train on Oct–Nov)
- baseline       VAL   |  PR‑AUC=0.50424  ROC‑AUC=0.93356  LL=0.30982  Brier=0.09151
  baseline       TEST  |  PR‑AUC=0.51660  ROC‑AUC=0.94054  LL=0.27284  Brier=0.08186
- drop_breadth   VAL   |  PR‑AUC=0.50217  ROC‑AUC=0.93466  LL=0.30395  Brier=0.08953
  drop_breadth   TEST  |  PR‑AUC=0.51387  ROC‑AUC=0.94237  LL=0.27005  Brier=0.08071
- slack_only     VAL   |  PR‑AUC=0.50217  ROC‑AUC=0.93466  LL=0.30395  Brier=0.08953
  slack_only     TEST  |  PR‑AUC=0.51387  ROC‑AUC=0.94237  LL=0.27005  Brier=0.08071

**Reading:** if `drop_viewpace` ≈ baseline, `PaceSlack_T` is carrying pace signal with lower collinearity. If `slack_only` holds up, residualization worked.

## B) Robustness to censoring (best model: HistGB)
- VAL: full‑coverage vs censored → ΔPR‑AUC=-0.3503, ΔROC‑AUC=-0.1536  (bases: full=0.1319, cens=0.0442)
- TEST: full‑coverage vs censored → ΔPR‑AUC=-0.3109, ΔROC‑AUC=-0.1405  (bases: full=0.1250, cens=0.0417)

> Notes: No retraining for censoring; this isolates scoring sensitivity. If gaps are large, consider training with a coverage indicator or reweighting censored sessions.