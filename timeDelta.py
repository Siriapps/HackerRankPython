#https://www.hackerrank.com/challenges/python-time-delta/problem
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    timezoneT1 = datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    timezoneT2 = datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return int(abs(timezoneT1-timezoneT2).total_seconds())
for iter in range(int(input())):
    t1 = input()
    t2 = input()
    print(time_delta(t1,t2))
