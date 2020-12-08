#https://www.hackerrank.com/challenges/validating-the-phone-number/problem
import re
for _ in range(int(input())):
    print("YES" if re.match(r'^[7-9]\d{9}$',input()) else "NO")
