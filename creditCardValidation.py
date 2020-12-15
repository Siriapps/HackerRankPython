#https://www.hackerrank.com/challenges/validating-credit-card-number/problem
import re
for _ in range(int(input())):
    card = input()
    if re.match(r'^[456]\d{3}(-?\d{4}){3}$',card) \
            and not re.search(r"(\d)\1\1\1",card.replace("-","")):
        print("Valid")
    else:
        print("Invalid")