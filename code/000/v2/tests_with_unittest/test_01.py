import unittest
from pathlib import Path 
import calendar

from context import my_calendar as mc


class MyCalendarTest(unittest.TestCase):
    def setUp(self):
        self.html_calendar = mc.CustomHTMLCalendar()
        p = Path('~', 'Data', '100-days-of-code', '000', 'v2').expanduser()
        p.mkdir(mode=0o700, parents=True, exist_ok=True)
        self.test_root = p
    
    def test_html_calendar(self):
        year = 2020
        calendar_html = Path(self.test_root, f'calendar-{year:d}.html')
        with open(calendar_html, 'w') as target:
            target.write('<html>')
            target.write('<head>')
            target.write('<link rel="stylesheet" href="calendar.css">')
            target.write('</head>')
            target.write('<body>')
            target.write(self.html_calendar.formatyear(year))
            target.write('</body>')    
            target.write('</html>')
        
    def test_calendar_filesystem(self):
        year = 2020
        year_path = Path(self.test_root, str(year))
        mc.build_filesystem(year_path, year)
        mc.generate_year(year_path, year, calendar.MONDAY, 'es_AR')


if __name__ == '__main__':
    unittest.main()

    
