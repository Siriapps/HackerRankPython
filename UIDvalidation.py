#https://www.hackerrank.com/challenges/validating-uid/problem
import re
for _ in range(int(input())):
    uid = input()
    print("Valid" if all([re.search(r,uid)for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']])
                     and not re.search(r'.*(.).*\1',uid) else "Invalid")
