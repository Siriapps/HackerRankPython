# https://www.hackerrank.com/challenges/compress-the-string/problem
from itertools import groupby
output = []
for k,v in groupby(input()):
    output.append((len(list(v)),int(k)))
print(*output)

