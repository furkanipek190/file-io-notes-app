"""
models.py
---------
Contains the definition of the data structures used in the application.
Note: Currently, the model is for conceptual purposes only.
"""

from dataclasses import dataclass

@dataclass
class Note:
    id: int
    text: str

    created_at: str
