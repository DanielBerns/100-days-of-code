import calendar
from pathlib import Path
import shutil
import sys
from typing import Optional


class CustomHTMLCalendar(calendar.LocaleHTMLCalendar):
    """
      Extracted from https://docs.python.org/3.8/library/calendar.html#calendar.HTMLCalendar
    """
    cssclasses = [style + " text-nowrap" for style in
                  calendar.HTMLCalendar.cssclasses]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-italic lead"
    
    def __init__(self, 
                 this_firstweekday=calendar.SUNDAY,
                 this_locale='es-AR'
                 ):
        super().__init__(firstweekday=this_firstweekday, locale=this_locale)


class CustomTextCalendar(calendar.LocaleTextCalendar):
    def __init__(self, 
                 this_firstweekday=calendar.SUNDAY,
                 this_locale='es-AR'
                 ):
        super().__init__(firstweekday=this_firstweekday, locale=this_locale)


def get_container(root: Path):
    root.expanduser()
    root.mkdir(mode=0o700, parents=True, exist_ok=True)
    return root


def generate_html_calendar(
    year: int, 
    root: Path, 
    this_calendar: Optional[calendar.LocaleHTMLCalendar]=None
    ):

    if this_calendar is None:
        this_calendar = CustomHTMLCalendar()

    calendar_root = get_container(root)
    calendar_html = Path(calendar_root, f'calendar-{year:d}.html')
    calendar_css = Path(calendar_root, 'calendar.css')
    with open(calendar_html, 'w') as target:
        target.write('<html>')
        target.write('<head>')
        target.write('<link rel="stylesheet" href="./calendar.css">')
        target.write('</head>')
        target.write('<body>')
        target.write(this_calendar.formatyear(year))
        target.write('</body>')    
        target.write('</html>')
    shutil.copy('./calendar.css', calendar_css)


def generate_text_calendar(
    year: int, 
    this_calendar: Optional[calendar.LocaleTextCalendar]=None
    ):
    
    if this_calendar is None:
        this_calendar = CustomTextCalendar()

    year_dates = this_calendar.yeardatescalendar(year, width=1)
    year_months = [this_calendar.formatmonthname(year, k + 1, 1) for k in range(12)]
    weekdays = [this_calendar.formatweekday(k, 3) for k in range(7)]
    
    for month in year_dates[0]:
        for week in month:
            for day in week:
                print(day, year_months[day.month-1] if day.year == year else '*')
        
    for m in year_months:
        print(m)
        
    for w in weekdays:
        print(w)
        
    return year_dates, year_months, weekdays


def generate_filesystem_calendar(year, root, exist_ok=True):
    months = [f'{m:02d}' for m in range(1, 13)]
    
    if year % 100:
        days_per_month = [31, 28 if year % 4 else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    elif year % 400:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_per_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    calendar_root = get_container(root)
    for this_month_label, this_month_days in zip(months, days_per_month):
        print(year, this_month_label)
        this_month = Path(calendar_root, this_month_label)
        this_month.mkdir(mode=0o700, parents=True, exist_ok=exist_ok)
        for this_day_number in range(1, this_month_days + 1):
            this_day_label = f'{this_day_number:02d}'
            this_day = Path(this_month, this_day_label)
            this_day.mkdir(mode=0o700, parents=True, exist_ok=exist_ok)


