#https://www.hackerrank.com/challenges/calendar-module/problem
import calendar
from datetime import datetime
print(calendar.day_name[datetime.strptime(input(),"%m %d %Y").weekday()].upper())