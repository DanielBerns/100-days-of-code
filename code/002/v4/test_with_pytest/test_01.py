import pytest
from pathlib import Path 
import calendar

from context import my_calendar as mc

class TestMyCalendar:
    def __init__(self):
        p = Path('~', 'Data', '100-days-of-code', '001', 'v3')
        self.test_root = p
    
    def test_html_calendar(self):
        test_root = Path('~', 'Data', '100-days-of-code', '001', 'v4')
        year = 2022
        html_calendar_root = Path(test_root, f'html_calendar-{year:d}')
        mc.generate_html_calendar(year, html_calendar_root)
        
    def test_filesystem_calendar(self):
        test_root = Path('~', 'Data', '100-days-of-code', '001', 'v4')        
        year = 2024
        filesystem_calendar_root = Path(test_root, str(year))
        mc.generate_filesystem_calendar(year, filesystem_calendar_root)

    def test_text_calendar(self):
        year = 2026
        yd, ym, wd = mc.generate_text_calendar(year)

    def test_locale(self):
        test_root = Path('~', 'Data', '100-days-of-code', '001', 'v4')
        mc.generate_text_calendar_with_locale(2026, test_root)

    
