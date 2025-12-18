# =========================
# Cell 0.0 — Write config.py, declaring GLOBALS
# =========================
# ---- Config ----
from pathlib import Path
import polars as pl
import sys
import os

# Define the project directory path
PROJECT_DIR = Path("../")

# Create the directory if it doesn't exist
PROJECT_DIR.mkdir(parents=True, exist_ok=True)

# Add the directory containing config.py to the Python path
config_path = PROJECT_DIR
if str(config_path) not in sys.path:
    sys.path.insert(0, str(config_path))

# Project roots
DATA_DIR    = PROJECT_DIR / "data"
OUT_DIR     = PROJECT_DIR / "cache_data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Month scopes
MONTHS_FULL = ["2019-Oct","2019-Nov","2019-Dec","2020-Jan","2020-Feb","2020-Mar","2020-Apr"]
MONTHS      = ["2019-Oct","2019-Nov","2019-Dec","2020-Jan","2020-Feb","2020-Mar","2020-Apr"]  # starter focus
# MONTHS      = ["2019-Oct","2019-Nov","2019-Dec",]  # starter focus

# Session feature window
T_MIN = 5

# CSV schema (avoid guessing)
CSV_DTYPES = {
    "event_time":   pl.Utf8,     # parsed to tz-aware UTC downstream
    "event_type":   pl.Utf8,
    "product_id":   pl.Int64,
    "category_id":  pl.Int64,
    "category_code":pl.Utf8,
    "brand":        pl.Utf8,
    "price":        pl.Float64,
    "user_id":      pl.Int64,
    "user_session": pl.Utf8,
}

FEATURE_COLS = [
    "event_time","event_type","product_id","category_id",
    "category_code","brand","price","user_id","user_session",
]

# Leakage-safe train/test pairs
LEAK_PAIRS = [
    ("2019-Oct","2019-Nov"),
    ("2019-Dec","2020-Jan"),
    ("2020-Feb","2020-Mar"),
    ("2020-Apr",),  # tail single
]
LEAK_MONTHS = ["2020-Jan","2020-Feb","2020-Mar",]

MONTHS_ORDERED = MONTHS_FULL
WRITE_COMBINED = True
