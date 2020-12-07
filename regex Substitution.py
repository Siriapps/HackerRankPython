#https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
import re
for _ in range(int(input())):
    line = input()
    print(re.sub(r'(?<= )(&&|\|\|)(?= )',lambda x: 'and' if x.group()=='&&' else 'or',line))

# lookbehind -
    # (?<=regex)
    # Meaning: preceded by the expression regex but without including it in the match
# lookahead -
    # (?=regex)
    # Meaning: followed by the expression regex but without including it in the match
