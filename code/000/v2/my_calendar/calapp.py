import calendar
from pathlib import Path
import sys

EXIST_OK = True

def build_filesystem(root, year):
    months = [f'{m:02d}' for m in range(1, 13)]
    
    if year % 100:
        days_per_month = [31, 28 if year % 4 else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    elif year % 400:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_per_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    root.mkdir(mode=0o700, parents=True, exist_ok=EXIST_OK)
    for this_month_label, this_month_days in zip(months, days_per_month):
        print(year, this_month_label)
        this_month = Path(root, this_month_label)
        this_month.mkdir(mode=0o700, parents=True, exist_ok=EXIST_OK)
        for this_day_number in range(1, this_month_days + 1):
            this_day_label = f'{this_day_number:02d}'
            this_day = Path(this_month, this_day_label)
            this_day.mkdir(mode=0o700, parents=True, exist_ok=EXIST_OK)

def generate_year(root, year, this_firstweekday, this_locale):
    this_calendar = calendar.LocaleTextCalendar(firstweekday=this_firstweekday, locale=this_locale)
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
        

if __name__ == "__main__":

    try:    
        year = int(sys.argv[1])
    except (IndexError, ValueError):
        year = 2020
    
    home = Path('~').expanduser()
    root = Path(home, 'Documents', 'Calendar', str(year))
    
    # build_filesystem(root, year)
    generate_year(root, year, calendar.MONDAY, 'es_AR')

 
