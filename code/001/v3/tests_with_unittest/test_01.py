import unittest
from pathlib import Path 
import calendar

from context import my_calendar as mc


class MyCalendarTest(unittest.TestCase):
    def setUp(self):
        self.html_calendar = mc.CustomHTMLCalendar()
        p = Path('~', 'Data', '100-days-of-code', '001', 'v3')
        self.test_root = p
    
    def test_html_calendar(self):
        year = 2020
        html_calendar_root = Path(self.test_root, f'html_calendar-{year:d}')
        mc.generate_html_calendar(year, html_calendar_root)
        
    def test_filesystem_calendar(self):
        year = 2022
        filesystem_calendar_root = Path(self.test_root, str(year))
        mc.generate_filesystem_calendar(year, filesystem_calendar_root)

    def test_text_calendar(self):
        year = 2020
        yd, ym, wd = mc.generate_text_calendar(year)


if __name__ == '__main__':
    unittest.main()

    
