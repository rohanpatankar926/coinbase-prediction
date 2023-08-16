from pathlib import Path
import os

PARENT_DIR=Path(__file__).parent.resolve().parent
DATA_DIR=PARENT_DIR / "data"
MODEL_DIR=PARENT_DIR/ "models"

if not Path(DATA_DIR).exists():
    os.mkdir(DATA_DIR)

if not Path(MODEL_DIR).exists():
    os.mkdir(MODEL_DIR)
