from pathlib import Path
import sys

if len(sys.argv) != 2:
    print('What year?')
    sys.exit(1)
    
year = int(sys.argv[1])

home = Path('~').expanduser()
calendar = Path(home, 'Documents', 'Calendar', str(year))

months = [f'{m:02d}' for m in range(1, 13)]

if year % 100:
    days_per_month = [31, 28 if year % 4 else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
elif year % 400:
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    days_per_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print('Year', year, str(calendar))
print('    ', 'months', months, 'days', days_per_month)

calendar.mkdir(mode=0o700, parents=True, exist_ok=False)
for this_month_label, this_month_days in zip(months, days_per_month):
    print(year, this_month_label)
    this_month = Path(calendar, this_month_label)
    this_month.mkdir(mode=0o700, parents=True, exist_ok=False)
    for this_day_number in range(1, this_month_days + 1):
        this_day_label = f'{this_day_number:02d}'
        # print('    ', this_day_label)
        this_day = Path(this_month, this_day_label)
        this_day.mkdir(mode=0o700, parents=True, exist_ok=False)
