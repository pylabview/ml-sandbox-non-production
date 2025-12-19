# =========================
# config.py — single source of truth for M2_EDA V6.1
# =========================
from __future__ import annotations

from pathlib import Path
import os
import sys
import polars as pl

# -------------------------
# Project paths
# -------------------------
# If your notebook lives in something like project/notebooks/, then "../" is the project root.
# You may override this by setting an environment variable:
#   os.environ["CS539_PROJECT_DIR"] = "/absolute/path/to/project"
PROJECT_DIR = Path(os.environ.get("CS539_PROJECT_DIR", "../")).resolve()
PROJECT_DIR.mkdir(parents=True, exist_ok=True)

# Ensure project root is importable (handy for sharing with others)
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

# Raw data (CSV) and derived artifacts (Parquet caches)
DATA_DIR = PROJECT_DIR / "data"
OUT_DIR  = PROJECT_DIR / "cache_data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Optional: keep Polars threads sane in Colab/shared boxes
os.environ.setdefault("POLARS_MAX_THREADS", "2")

PARQUET_COMPRESSION = "zstd"


# -------------------------
# Month scopes (STRICT chronological split)
# -------------------------
# Rule:
#   Train = Oct–Nov 2019
#   Val   = Dec 2019
#   Test  = Jan–Mar 2020
# Keep Apr 2020 available as a boundary month for sessions/purchases that spill over.
TRAIN_TAG    = ("2019-Oct", "2019-Nov")
VAL_TAG      = ("2019-Dec",)
TEST_TAG     = ("2020-Jan", "2020-Feb", "2020-Mar")
BOUNDARY_TAG = ("2020-Apr",)

TRAIN_MONTHS = list(TRAIN_TAG)
VAL_MONTHS   = list(VAL_TAG)
TEST_MONTHS  = list(TEST_TAG)

# Full month inventory available for building caches
MONTHS_FULL = list(TRAIN_TAG + VAL_TAG + TEST_TAG + BOUNDARY_TAG)

# Default processing scope (use full inventory unless you intentionally narrow)
MONTHS = list(MONTHS_FULL)

# Canonical chronological order
MONTHS_ORDERED = list(MONTHS_FULL)

# Convenience windows for running Cells 6–8
# NOTE: Cells 6–8 build "combined" files spanning LEAK_MONTHS[0] → LEAK_MONTHS[-1].
LEAK_MONTHS_TRAINVAL = list(TRAIN_TAG + VAL_TAG)   # produces 2019-Oct_to_2019-Dec combined targets
LEAK_MONTHS_TEST     = list(TEST_TAG)              # produces 2020-Jan_to_2020-Mar combined targets


# How you’ll use this (so your notebook builds all shareable caches)
# Run your notebook with LEAK_MONTHS = LEAK_MONTHS_TRAINVAL → run Cells 6–8 to produce the Oct–Dec combined targets file.
# Then change only in this config (Cell 0.0) to:

# LEAK_MONTHS = LEAK_MONTHS_TEST
# Default window processed by Cells 6–8 (change this in ONE place when needed)
LEAK_MONTHS = list(LEAK_MONTHS_TEST)

# Optional override used by some cells (leave empty to fall back to LEAK_MONTHS → MONTHS → MONTHS_FULL)
# IMPORTANT: keep this as a LIST (not None) so list(getattr(...)) never crashes
MONTHS_WINDOW: list[str] = []


# -------------------------
# Session feature window
# -------------------------
T_MIN = 5
# Optional alias (some older cells might refer to T)
T = T_MIN


# -------------------------
# Cache / rebuild knobs (centralized)
# -------------------------
# Cell 0.3 (CSV → Parquet)
#   None => convert all months in the driver list
#   or set ["2020-Apr"] etc. for targeted conversion
MONTH_FILTER = None          # None or list[str]
FORCE = True                 # overwrite existing OUT_DIR/{month}.parquet

# Cell 1.0 (sanity-check metrics cache)
USE_CACHE = True
CACHE_PATH = OUT_DIR / "_metrics_month.parquet"

# Cell 8 (targets build)
FORCE_REBUILD = False        # overwrite existing *_TARGETS outputs?

# Cells 6/7/8 combined outputs
WRITE_COMBINED = True


# -------------------------
# Cross-month helpers (used by some ingestion/sessionization cells)
# -------------------------
# Contiguous pairs across MONTHS_ORDERED + tail singleton
LEAK_PAIRS = [(MONTHS_ORDERED[i], MONTHS_ORDERED[i + 1]) for i in range(len(MONTHS_ORDERED) - 1)]
LEAK_PAIRS.append((MONTHS_ORDERED[-1],))


# -------------------------
# CSV schema (avoid guessing)
# -------------------------
CSV_DTYPES = {
    "event_time":    pl.Utf8,     # parsed to tz-aware UTC downstream
    "event_type":    pl.Utf8,
    "product_id":    pl.Int64,
    "category_id":   pl.Int64,
    "category_code": pl.Utf8,
    "brand":         pl.Utf8,
    "price":         pl.Float64,
    "user_id":       pl.Int64,
    "user_session":  pl.Utf8,
}

FEATURE_COLS = [
    "event_time", "event_type", "product_id", "category_id",
    "category_code", "brand", "price", "user_id", "user_session",
]
