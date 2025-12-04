
from pathlib import Path

# --- Core project paths ---
PROJECT_DIR = Path(r"..")
DATA_DIR    = PROJECT_DIR / "data"
OUT_DIR     = PROJECT_DIR / "cache_data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
OUT_DIR.mkdir(parents=True, exist_ok=True)

# --- Window + feature constants ---
T_MIN = 5
BREADTH_TO_PACE_COEFF = 1.0 / T_MIN  # -> 0.2 when T=5
FASTFOCUSED_PACE_MIN = 1.2
FASTFOCUSED_BREADTH_MAX = 2

# --- Splits ---
TRAIN_MONTHS = ("2019-Oct", "2019-Nov", "2019-Dec")
TEST_MONTHS  = ("2020-Jan", "2020-Feb", "2020-Mar")

# Canonical cache filenames (already built)
TRAIN_COMBINED_ENRICHED_TARGETS = (
    f"session_features_{TRAIN_MONTHS[0]}_to_{TRAIN_MONTHS[-1]}_T{T_MIN}_LEAKFREE_ENRICHED_COMBINED_TARGETS.parquet"
)
TEST_COMBINED_ENRICHED_TARGETS = (
    f"session_features_{TEST_MONTHS[0]}_to_{TEST_MONTHS[-1]}_T{T_MIN}_LEAKFREE_ENRICHED_COMBINED_TARGETS.parquet"
)

# Output suffix for engineered caches (we do NOT overwrite source)
ENGINEERED_SUFFIX = "_ENGINEERED"

# IO settings
OVERWRITE = True
PARQUET_COMPRESSION = "zstd"
