import unittest
from pathlib import Path 
import calendar

from context import my_calendar as mc


class MyCalendarTest(unittest.TestCase):
    def setUp(self):
        self.html_calendar = mc.CustomHTMLCalendar()
        p = Path('~').expanduser()
        q = Path(p, 'Data', '100-days-of-code', '002', 'v4')
        self.test_root = q
        
    def test_html_calendar(self):
        year = 2022
        html_calendar_root = Path(self.test_root, f'html_calendar-{year:d}')
        mc.generate_html_calendar(year, html_calendar_root)
        
    def test_filesystem_calendar(self):
        year = 2024
        filesystem_calendar_root = Path(self.test_root, str(year))
        mc.generate_filesystem_calendar(year, filesystem_calendar_root)

    def test_text_calendar(self):
        year = 2026
        yd, ym, wd = mc.generate_text_calendar(year)

    def test_locale(self):
        mc.generate_text_calendar_with_locale(2026, self.test_root)
    
if __name__ == '__main__':
    unittest.main()

    
