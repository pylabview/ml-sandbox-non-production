# Sensitivity — T=5

## A) Collinearity variants (Logit re-train on Oct–Nov)
- baseline       VAL   |  PR-AUC=0.50903  ROC-AUC=0.93302  LL=0.31027  Brier=0.09125
  baseline       TEST  |  PR-AUC=0.52225  ROC-AUC=0.94054  LL=0.27300  Brier=0.08166
- drop_breadth   VAL   |  PR-AUC=0.50386  ROC-AUC=0.93476  LL=0.30546  Brier=0.08941
  drop_breadth   TEST  |  PR-AUC=0.51544  ROC-AUC=0.94188  LL=0.27108  Brier=0.08071
- slack_only     VAL   |  PR-AUC=0.50386  ROC-AUC=0.93476  LL=0.30546  Brier=0.08941
  slack_only     TEST  |  PR-AUC=0.51544  ROC-AUC=0.94188  LL=0.27108  Brier=0.08071

**Reading:** if `drop_viewpace` ≈ baseline, `PaceSlack_T` is carrying pace signal with lower collinearity. If `slack_only` holds up, residualization worked.

## B) Robustness to censoring (best model: HistGB)
- VAL: full-coverage vs censored → ΔPR-AUC=-0.3500, ΔROC-AUC=-0.1536  (bases: full=0.1319, cens=0.0442)
- TEST: full-coverage vs censored → ΔPR-AUC=-0.3085, ΔROC-AUC=-0.1403  (bases: full=0.1250, cens=0.0417)

> Notes: No retraining for censoring; this isolates scoring sensitivity. If gaps are large, consider training with a coverage indicator or reweighting censored sessions.