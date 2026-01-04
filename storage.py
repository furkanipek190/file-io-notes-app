"""
storage.py
-----------

It is responsible for writing and reading notes to and from the file.
This file is the I/O (Input/Output) layer.
"""

from pathlib import Path
import json

# Based on the folder where this file is located
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data.json"

def load_notes() -> list[dict]:
    """
    Reads the data.json file and returns the notes as a list.
    If the file does not exist, is empty, or is corrupted, an empty list is returned. 
    """
    if not DATA_FILE.exists():
        return []
    try:
        content = DATA_FILE.read_text(encoding="utf-8").strip()
        if not content:
            return []
        data = json.loads(content)
        # Return empty safely if JSON content is not a list
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []

def save_notes(notes: list[dict]) -> None:
    # It writes the list of notes to the data.json file
    DATA_FILE.write_text(
        json.dumps(notes, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
