#_Part_00100_defaults  [주석단위]
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
BUILD_DIR = ROOT_DIR / "_build"
BUILD_DIR.mkdir(exist_ok=True)

# Default Arduino board
DEFAULT_FQBN = "arduino:avr:uno"
DEFAULT_PORT = ""
