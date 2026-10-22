#!/usr/bin/env bash
set -euo pipefail
python --version
git --version
python -m venv .venv
.venv/bin/python -m pip install -r requirements-notebook.txt
.venv/bin/python -m ipykernel install --sys-prefix --name ml-template --display-name 'Python (.venv)'
.venv/bin/python tests/vorabcheck.py --notebook
.venv/bin/python tests/materialcheck.py
