# ml101

Small starter project for Python & Jupyter learning.

What I added:
- `.gitignore` — excludes virtualenvs and caches
- `requirements.txt` — minimal dependencies (kept small)
- `src/sample.py` — tiny example module
- `tests/test_sample.py` — unittest-based test

Usage
1. Create or activate a virtualenv (recommended):
   python -m venv .venv
   source .venv/bin/activate
2. Install (optional):
   pip install -r requirements.txt
3. Run tests:
   python -m unittest discover -v

Notes
- Avoid placing project files inside your virtualenv directory (move `notebook.ipynb` out of `.venv`).
- Consider adding linters (ruff) and formatters (black) for a consistent code style.
