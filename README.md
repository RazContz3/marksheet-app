# School Marksheet Management Web App

This is a full-featured Flask web application for managing and reporting student marksheets. It supports:
- Pre-inserted marksheet data from CSVs
- Student search/filter
- Automated pass/fail and basket subject reports
- Term-wise and summary reports
- Special attention lists (May Be Pass, Withdrawn)
- Export/print options

## Structure
- `app/` - Main application code
  - `static/` - CSS, JS, images
  - `templates/` - HTML templates
  - `data/` - CSVs and SQLite database
  - `reports/` - Generated reports
- `.github/` - Copilot instructions

## Getting Started
1. Install requirements: `pip install flask pandas sqlite3`
2. Run the app: `python app/app.py`
3. Access via browser: `http://localhost:5000`

## Data Import
Place your cleaned CSVs in `app/data/` for automatic import on first run.

## Customization
Edit templates and static files for UI changes. Extend `app.py` for new features.

---

For more details, see copilot-instructions.md in `.github/`.
