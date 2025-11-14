## Copilot / AI Agent Instructions for ml101

This repository is a small ML learning starter focused on Jupyter workflows and lightweight Python examples. Keep changes minimal and notebook-first: most project logic lives inside `src/ML Template.ipynb`.

- **Project layout:**
  - `AmesHousing.csv`, `train.csv`, `test.csv`, `target.csv` — dataset files live at the repo root.
  - `src/` — helper modules and notebooks. Notebooks of interest: `src/ML Template.ipynb`, `src/notebook.ipynb`.
  - `src/sample.py` — small example module used by tests.
  - `tests/test_sample.py` — unit tests (unittest style) that import `src` directly.
  - `requirements.txt` — dependencies for running notebooks and tests.

- **How to run / common commands:**
  - Install deps: `pip install -r requirements.txt` (use virtualenv/venv).
  - Run tests: `pytest -q` (run from repository root so `src` is importable).
  - Open notebooks: `jupyter lab` or `jupyter notebook` in repo root.

- **Testing notes:**
  - Tests use `unittest` assertions inside `tests/test_sample.py` and import `src.sample`.
  - Do not rename `src` package or move `sample.py` without updating imports in tests.

- **Key implementation patterns to follow / preserve:**
  - Notebook-first workflow: significant code and data-cleaning logic is inside `src/ML Template.ipynb`. When extracting logic to scripts, preserve original notebook behaviour and cell ordering.
  - Column-name normalization: the notebook uses a `to_snake(col)` helper (in `src/ML Template.ipynb`) that replaces spaces/hyphens with underscores; be conservative if changing it — other cells expect those column names.
  - Missingness flags: the notebook routinely adds boolean indicators like `df[col + "_was_missing"]` or `Has_Pool`, `Has_Garage` — keep this pattern when adding new imputation code so feature-engineering remains consistent.
  - Imputation patterns (examples to mirror):
    - `Lot_Frontage` imputed via median lot depth: compute `median_depth = (Lot_Area / Lot_Frontage).median()` then set missing `Lot_Frontage = Lot_Area / median_depth`.
    - Pool handling: create `Has_Pool = ((Pool_Area > 0) | Pool_QC.notna()).astype(int)` then set `Pool_QC` to explicit `"None"` for rows with no pool.
    - Garage, Basement, Fireplace, Fence, Alley, Mas_Vnr_Type: the notebook sets boolean flags (e.g. `Has_Garage`, `Has_Basement`) and fills missing categorical values with `"None"` or `"Unknown"` depending on context. Follow these exact string values when possible.

- **Data & dataset expectations:**
  - The template assumes `TARGET_COL = "SalePrice"` inside `src/ML Template.ipynb`. If you change the target, update the notebook cell that sets `TARGET_COL`.
  - Notebooks assume numeric columns detected via `df.select_dtypes(include=[np.number])` and categorical via `exclude=[np.number]` — avoid altering dtype detection without updating downstream cells.

- **When editing notebooks:**
  - Prefer adding helper functions into `src/*.py` if logic will be reused or tested. Keep the notebooks as orchestration and exploratory cells.
  - If you refactor code out of a notebook into `.py` files, add or update tests under `tests/` to cover the extracted functions.
  - Preserve the explicit imputation / cleaning strings (`None`, `Unknown`) since downstream encoding and model pipelines depend on them.

- **Development conventions:**
  - Keep edits small and focused: this is a learning repo, not a production codebase.
  - Use `pytest` from the repo root so that `src` is on the import path (no package installation is configured).

- **Examples to reference when making changes:**
  - Column normalization and missing-value summary: see the cleaning cell in `src/ML Template.ipynb` (search for `to_snake` and `missing_summary`).
  - Lot frontage imputation: search for `IMPUTE LOT_FRONTAGE` in `src/ML Template.ipynb`.
  - Pool / Garage / Basement cleaning examples: cells containing `Pool_QC`, `Garage_Type`, `Has_Basement`.

If anything here is unclear or you want me to expand a section (for example, add strict linting/formatting rules or a test harness for notebook code), tell me which part and I will iterate.
