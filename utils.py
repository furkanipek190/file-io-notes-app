"""
utils.py
--------

Contains helper functions used throughout the application.
"""

from datetime import datetime

def now_iso() -> str:
    """
    Returns the current date in ISO format. 
    Example: 2026-01-04T15:51:22
    """
    return datetime.now().isoformat(timespec="seconds")

def next_id(notes: list[dict]) -> int:
    """
    Generates the next ID by looking at the existing notes. 
    """
    if not notes:
        return 1
    return max(n["id"] for n in notes) + 1