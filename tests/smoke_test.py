from __future__ import annotations
import os, runpy
from pathlib import Path
os.environ.setdefault('MPLBACKEND', 'Agg')
root = Path(__file__).resolve().parents[1]
os.chdir(root)
for script in sorted((root / 'programme').glob('*.py')):
    print('SMOKE', script.name)
    runpy.run_path(str(script), run_name='__main__')
print('SMOKE TEST BESTANDEN')
