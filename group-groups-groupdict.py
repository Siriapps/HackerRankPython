#https://www.hackerrank.com/challenges/re-group-groups/problem
import re
# we are not using '\w' in the place of [a-zA-Z0-9] because by using that we accept character like '_' as '_'is not
# alphanumeric we can't use '\w'
pattern = re.search(r'([a-zA-Z0-9])\1+', input())
print(pattern.group(1) if pattern else -1)
