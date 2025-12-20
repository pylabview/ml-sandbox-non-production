"""
configm4.py — Milestone 4 (Revise & Evaluate ML Model) configuration

Goals:
- Single source of truth for paths + month split + shared constants.
- Colab-free: no /content paths, no drive mounting, no notebook-only assumptions.
- Matches the Milestone-2 "config.py" vibe (paths + month tags + yyyymm helper + print_cfg).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple


# ---------------------------------------------------------------------
# Project paths (robust across machines)
# ---------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent        # e.g., .../notebooks/
PROJECT_DIR = _THIS_DIR.parent                      # e.g., .../project/
DATA_DIR = PROJECT_DIR / "data"
OUT_DIR = PROJECT_DIR / "cache_data"

# IO defaults
PARQUET_COMPRESSION: str = "zstd"
OVERWRITE: bool = True


# ---------------------------------------------------------------------
# Time window + split policy (M4 required scope)
# ---------------------------------------------------------------------
T_MIN: int = 5  # early-session window in minutes (keep consistent with M2/M3 caches)

# Month tags (human readable)
TRAIN_TAG: Tuple[str, ...]    = ("2019-Oct", "2019-Nov")
VAL_TAG: Tuple[str, ...]      = ("2019-Dec",)
TEST_TAG: Tuple[str, ...]     = ("2020-Jan", "2020-Feb", "2020-Mar")
BOUNDARY_TAG: Tuple[str, ...] = ("2020-Apr",)

# Convenience
TRAINVAL_TAG: Tuple[str, ...] = TRAIN_TAG + VAL_TAG
ALL_TAGS: Tuple[str, ...] = TRAIN_TAG + VAL_TAG + TEST_TAG + BOUNDARY_TAG

# ---- month-tag helpers ("2019-Oct" -> "2019-10")
_MON = {
    "Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06",
    "Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12",
}
def yyyymm(tag: str) -> str:
    """Convert a month tag like '2019-Oct' to '2019-10'."""
    y, mon = tag.split("-")
    return f"{y}-{_MON[mon]}"

TRAIN_MONTHS: Tuple[str, ...]    = tuple(yyyymm(m) for m in TRAIN_TAG)
VAL_MONTHS: Tuple[str, ...]      = tuple(yyyymm(m) for m in VAL_TAG)
TEST_MONTHS: Tuple[str, ...]     = tuple(yyyymm(m) for m in TEST_TAG)
BOUNDARY_MONTHS: Tuple[str, ...] = tuple(yyyymm(m) for m in BOUNDARY_TAG)

MONTHS_ORDERED: Tuple[str, ...] = TRAIN_MONTHS + VAL_MONTHS + TEST_MONTHS + BOUNDARY_MONTHS


# ---------------------------------------------------------------------
# Canonical cache file names (consistent templates)
# ---------------------------------------------------------------------
ENGINEERED_SUFFIX: str = "_ENGINEERED"
AGG_SUFFIX: str = "_AGG"  # append after ENGINEERED to avoid "ENGINEERED_ENGINEERED_AGG"


def month_enriched_targets_name(month_tag: str) -> str:
    """Per-month leakfree engineered+target cache (preferred source for M4)."""
    return f"session_features_{month_tag}_T{T_MIN}_LEAKFREE_ENRICHED_TARGETS.parquet"

def month_enriched_targets_path(month_tag: str) -> Path:
    return OUT_DIR / month_enriched_targets_name(month_tag)

def combined_enriched_targets_name(start_tag: str, end_tag: str) -> str:
    """Combined multi-month leakfree engineered+target cache."""
    return f"session_features_{start_tag}_to_{end_tag}_T{T_MIN}_LEAKFREE_ENRICHED_COMBINED_TARGETS.parquet"

def combined_enriched_targets_path(start_tag: str, end_tag: str) -> Path:
    return OUT_DIR / combined_enriched_targets_name(start_tag, end_tag)

# These mirror the typical combined caches you’ve been generating:
TRAINVAL_COMBINED_ENRICHED_TARGETS: str = combined_enriched_targets_name(TRAINVAL_TAG[0], TRAINVAL_TAG[-1])
TEST_COMBINED_ENRICHED_TARGETS: str     = combined_enriched_targets_name(TEST_TAG[0], TEST_TAG[-1])


# ---------------------------------------------------------------------
# Shared M4 feature-engineering constants
# ---------------------------------------------------------------------
# PaceSlack_T is defined as max(0, Breadth_to_pace_limit - ViewPace_T)
BREADTH_TO_PACE_COEFF: float = 1.0 / T_MIN  # -> 0.2 when T=5
FASTFOCUSED_PACE_MIN: float = 1.2
FASTFOCUSED_BREADTH_MAX: int = 2


# ---------------------------------------------------------------------
# Shared random seed (use across models for reproducibility)
# ---------------------------------------------------------------------
SEED: int = 539

# ---------------------------------------------------------------------
# Shared random seed + evaluation/reporting knobs (used in Cell 17)
# ---------------------------------------------------------------------
SEED: int = 539

# Sampling caps for evaluation (keep runtime/RAM sane)
VAL_SAMPLE_ROWS: int  = 1_000_000   # rows to sample from Dec-2019 (VAL)
TEST_SAMPLE_ROWS: int = 1_500_000   # rows to sample from Jan–Mar 2020 (TEST)

# Bootstrap settings (paired across models)
N_BOOT: int = 120                   # bootstrap replicates
BOOT_RESAMPLE_FRA: float = 1.00     # 1.0 = same-size resample; <1.0 faster CI

# Whether to apply 16.1 calibrators if present
APPLY_CALIBRATION: bool = True

# ---------------------------------------------------------------------
# Pretty-print (like M2)
# ---------------------------------------------------------------------
@dataclass(frozen=True)
class _CfgView:
    DATA_DIR: str
    OUT_DIR: str
    T_MIN: int
    TRAIN_TAG: Tuple[str, ...]
    VAL_TAG: Tuple[str, ...]
    TEST_TAG: Tuple[str, ...]
    BOUNDARY_TAG: Tuple[str, ...]
    TRAIN_MONTHS: Tuple[str, ...]
    VAL_MONTHS: Tuple[str, ...]
    TEST_MONTHS: Tuple[str, ...]
    BOUNDARY_MONTHS: Tuple[str, ...]
    PARQUET_COMPRESSION: str
    OVERWRITE: bool
    SEED: int
    VAL_SAMPLE_ROWS: int
    TEST_SAMPLE_ROWS: int
    N_BOOT: int
    BOOT_RESAMPLE_FRA: float
    APPLY_CALIBRATION: bool


def as_dict() -> Dict:
    return _CfgView(
        DATA_DIR=str(DATA_DIR),
        OUT_DIR=str(OUT_DIR),
        T_MIN=T_MIN,
        TRAIN_TAG=TRAIN_TAG,
        VAL_TAG=VAL_TAG,
        TEST_TAG=TEST_TAG,
        BOUNDARY_TAG=BOUNDARY_TAG,
        TRAIN_MONTHS=TRAIN_MONTHS,
        VAL_MONTHS=VAL_MONTHS,
        TEST_MONTHS=TEST_MONTHS,
        BOUNDARY_MONTHS=BOUNDARY_MONTHS,
        PARQUET_COMPRESSION=PARQUET_COMPRESSION,
        OVERWRITE=OVERWRITE,
        SEED=SEED,
        VAL_SAMPLE_ROWS=VAL_SAMPLE_ROWS,
        TEST_SAMPLE_ROWS=TEST_SAMPLE_ROWS,
        N_BOOT=N_BOOT,
        BOOT_RESAMPLE_FRA=BOOT_RESAMPLE_FRA,
        APPLY_CALIBRATION=APPLY_CALIBRATION,

    ).__dict__

def print_cfg(prefix: str = "=== M4 Config ===") -> None:
    import pprint
    print(prefix)
    pprint.pprint(as_dict(), width=110)
