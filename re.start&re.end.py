#https://www.hackerrank.com/challenges/re-start-re-end/problem
import re
s = input()
k = input()
index = 0
if re.search(k,s):
    while len(k) < len(s):
        m = re.search(k,s[index:])
        if m!= None:
            print((index+m.start(), index+m.end()-1))
        else:
            break
        index += m.start()+1
else:
    print((-1, -1))
