# File I/O Notes App (Python) — Filo-Io-App

## Versioning

This project follows a simple semantic versioning approach.

### v1.0 – Initial Stable Release
- Core File I/O functionality
- Add, list, delete, and search notes
- JSON-based data persistence
- Modular architecture (main, storage, utils, models)
- Basic error handling for missing or invalid data files

This version represents the first stable and fully functional release.


A simple, modular **File Read/Write** (JSON-based) notes application built with Python.
It allows you to add, list, delete, and search notes while persisting data into a local JSON file.

## Features
- Add notes
- List saved notes
- Delete notes by ID
- Search notes by keyword
- JSON persistence (`data.json`)
- Basic error tolerance (missing/empty/invalid file scenarios)

## Project Structure
Filo-Io-App/
main.py
storage.py
utils.py
models.py
data.json.example
README.md
LICENSE
.gitignore


## Code Architecture
## Code Architecture

This project follows a **simple, modular architecture** to demonstrate
clean separation of responsibilities and readable Python code structure.

Each file has a clear and single responsibility.

### Entry Point
**`main.py`**
- Application entry point
- Handles user interaction (menu, input, output)
- Controls program flow
- Calls other modules when needed

> Rule: The program is always started via `main.py`

---

### Data Persistence Layer
**`storage.py`**
- Responsible for file input/output operations
- Reads notes from `data.json`
- Writes updated notes back to disk
- Uses absolute paths to avoid working-directory issues
- Gracefully handles missing, empty, or invalid files

This layer isolates all file system logic from the rest of the application.

---

### Utility Layer
**`utils.py`**
- Provides helper functions used across the project
- Generates timestamps
- Calculates the next unique note ID

This keeps repetitive logic out of the main application flow.

---

### Data Model
**`models.py`**
- Defines the conceptual structure of a Note
- Uses a `dataclass` for clarity and future extensibility

Currently used for documentation and architectural clarity.
Can be expanded for validation or type enforcement in future versions.

---

### Data File
**`data.json`**
- Stores notes as a list of dictionaries
- Each note contains:
  - `id`
  - `text`
  - `created_at`

This file is intentionally excluded from version control
to protect personal data.

---

### Architectural Principles
- Single Responsibility Principle (SRP)
- Clear separation of concerns
- Readable and beginner-friendly structure
- Designed for incremental extension (logging, backups, tests)

This architecture is intentionally simple,
but follows real-world software development practices.




## Requirements
- Python 3.10+ (works on newer versions too)

## Setup & Run
> Open a terminal in the project folder and run:

```powershell
python .\main.py


First run data file

This repo includes data.json.example.
Create your local data.json as:
[]
Note: data.json is gitignored to avoid uploading personal notes.


Usage (Menu)

Add note
List notes
Delete note
Search notes
Exit


Data Format
Each note is stored like:
{
  "id": 1,
  "text": "Sample note",
  "created_at": "2026-01-04T15:51:22"
}


Troubleshooting
"No such file or directory"

Make sure you run the app from the project folder:
pwd
dir
python .\main.py
