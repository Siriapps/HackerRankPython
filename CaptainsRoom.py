#https://www.hackerrank.com/challenges/py-the-captains-room/problem
from collections import Counter
K = int(input())
roomNum = list(map(int,input().split()))
count = Counter(roomNum)
for k,v in count.items():
    if v!=K :
        print(k)

