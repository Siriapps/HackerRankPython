#https://www.hackerrank.com/challenges/hex-color-code/problem
import re
for _ in range(int(input())):
    hexCodes = re.findall(r'(#[0-9A-F]{3,6})(?=\S)',input(),re.I)
    if hexCodes:
        print("\n".join(map(str,hexCodes)))
    else:
        continue