# calendar_formatyear.py
# https://pymotw.com/3/calendar/index.html#module-calendar
import calendar
import locale
import sys

original_loc = locale.getlocale()
modified_loc = 'es_AR'

print('original_loc', original_loc)
print('modified_loc', modified_loc)

year = int(sys.argv[1])

locale.setlocale(locale.LC_ALL, modified_loc)
cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatyear(year, 2, 1, 1, 3))
locale.setlocale(locale.LC_ALL, original_loc)
