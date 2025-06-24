import calendar
from datetime import datetime

date_input = input().strip()
month, day, year = map(int, date_input.split())

date_obj = datetime(year, month, day)
day_name = calendar.day_name[date_obj.weekday()]

print(day_name.upper())