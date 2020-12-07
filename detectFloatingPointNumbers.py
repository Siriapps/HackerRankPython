# https://www.hackerrank.com/challenges/introduction-to-regex/problem
# a nice video on regex metacharacters-https://www.youtube.com/watch?v=K8L6KVGG-7o
import re
for _ in range(int(input())):
    print(bool(re.match("^[+-]?[0-9]*\.[0-9]+$",input())))
