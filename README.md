# Passport Management System (CLI)

A lightweight MVP for a **Passport Management System** built with **Python 3.7+**, using **SQLite** as the database and a modular project structure for easy future expansion.

---

## Overview

This project provides a simple command-line tool for managing passport records.

Features include:

* Add a new passport with validation and duplicate protection
* List all passports
* Search by National ID, Passport Number, or Full Name
* Update passport details
* Delete a passport by its number

This MVP acts as a foundation for future upgrades such as Web UI, API, authentication, and multi-user access.

---

## Features

* Simple and lightweight (SQLite-based)
* Modular and scalable project structure
* Built-in validation utilities (dates, National ID format)
* Safe error handling with friendly user messages

---

## Requirements

* **Python 3.7+**
* Dependencies (in `requirements.txt`):

  * `tabulate` (optional, for table output)

---

## Quick Start

### 1. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\\Scripts\\activate.bat   # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python main.py
```

Upon first launch, the app initializes the SQLite database and creates the `passports` table automatically.

---

## Project Structure

```
passport-cli/
├── main.py                      # CLI Entry point
├── requirements.txt             # Dependencies
├── README.md
├── database/
│   ├── __init__.py
│   ├── models.py                # Passport table definitions
│   └── database_manager.py      # DB initialization + connection
├── services/
│   ├── __init__.py
│   └── passport_service.py      # CRUD logic for passports
└── utils/
    ├── __init__.py
    └── validators.py           # Date / National ID validation functions
```

---

## Database Schema

Table: **passports**

Columns:

* `id` — Primary Key (Auto-increment)
* `national_id` — Unique, Required
* `passport_number` — Unique, Required
* `full_name` — Required
* `date_of_birth` — `YYYY-MM-DD`
* `nationality` — Required
* `issue_date`
* `expiry_date`
* `authority`
* `created_at` — Default: current timestamp

---

## CLI Menu

```
=== Passport Management System ===
1. Add new passport
2. View all passports
3. Search for passport
4. Update passport
5. Delete passport
6. Exit
```

Input is validated and errors are handled gracefully.

---

## Example

### Add Passport

```
National ID: 0123456789
Passport Number: A1234567
Full Name: Ahmed Ali
Date of Birth: 1985-02-14
Nationality: Saudi
Issue Date: 2020-05-01
Expiry Date: 2030-05-01
Authority: Ministry of Interior
```

---

## Development Notes

* CRUD logic is in `passport_service.py`
* Validation functions in `validators.py`
* Database setup in `database_manager.py`

---

## Future Enhancements

* Migrate to PostgreSQL
* Add authentication & user roles
* REST API (FastAPI / Flask)
* Export & Import (CSV / JSON)
* Unit tests
* Data encryption for sensitive fields

---

## Contribution

Pull requests and issues are welcome.

---

## License

MIT (recommended) — add a LICENSE file if needed.

---

If you want, I can now generate the **actual source code files** (main.py, database models, services, utils) ready to paste into your repo.
