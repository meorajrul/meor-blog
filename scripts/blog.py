"""Project entry point; maintained implementation lives in the plugin."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parents[1]/'plugins/meor-journal/scripts/blog.py'),run_name='__main__')
