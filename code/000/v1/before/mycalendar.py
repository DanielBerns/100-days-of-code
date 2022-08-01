# calendar_yeardays2calendar.py
import calendar
import sys

class CustomHTMLCalendar(calendar.LocaleHTMLCalendar):
    cssclasses = [style + " text-nowrap" for style in
                  calendar.HTMLCalendar.cssclasses]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-italic lead"
    
    def __init__(self):
        super().__init__(firstweekday=calendar.SUNDAY, locale='es_AR')
        
try:    
    year = int(sys.argv[-1])
except ValueError:
    year = 2020

c = CustomHTMLCalendar()

with open(f'calendar-{year:d}.html', 'w') as target:
    target.write('<html>')
    target.write('<head>')
    target.write('<link rel="stylesheet" href="calendar.css">')
    target.write('</head>')
    target.write('<body>')
    target.write(c.formatyear(year))
    target.write('</body>')    
    target.write('</html>')
