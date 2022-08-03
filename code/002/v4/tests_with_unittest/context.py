from pathlib import Path
import sys

p = Path('./').absolute()
q = str(p.parent)
sys.path.insert(0, q)

import my_calendar
