# Sensitivity — T=5

## A) Collinearity variants (Logit re-train on Oct–Nov)
- baseline       VAL   |  PR-AUC=0.50573  ROC-AUC=0.93374  LL=0.30469  Brier=0.09124
  baseline       TEST  |  PR-AUC=0.51965  ROC-AUC=0.94315  LL=0.27044  Brier=0.08156
- drop_breadth   VAL   |  PR-AUC=0.50279  ROC-AUC=0.93625  LL=0.29956  Brier=0.08957
  drop_breadth   TEST  |  PR-AUC=0.51582  ROC-AUC=0.94490  LL=0.26871  Brier=0.08073
- slack_only     VAL   |  PR-AUC=0.50279  ROC-AUC=0.93625  LL=0.29956  Brier=0.08957
  slack_only     TEST  |  PR-AUC=0.51582  ROC-AUC=0.94490  LL=0.26871  Brier=0.08073

**Reading:** if `drop_viewpace` ≈ baseline, `PaceSlack_T` is carrying pace signal with lower collinearity. If `slack_only` holds up, residualization worked.

## B) Robustness to censoring (best model: HistGB)
- VAL: full-coverage vs censored → ΔPR-AUC=-0.3508, ΔROC-AUC=-0.1537  (bases: full=0.1319, cens=0.0442)
- TEST: full-coverage vs censored → ΔPR-AUC=-0.3092, ΔROC-AUC=-0.1403  (bases: full=0.1250, cens=0.0417)

> Notes: No retraining for censoring; this isolates scoring sensitivity. If gaps are large, consider training with a coverage indicator or reweighting censored sessions.