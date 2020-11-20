# https://www.hackerrank.com/challenges/piling-up/problem
# importing deque
from collections import deque
for _ in range(int(input())):
    n = int(input())
    sideLength = deque(map(int,input().split())) #space separated integers, denoting the sideLengths of each cube.
    for slst in reversed(sorted(sideLength)):
        if sideLength[0] == slst:
            sideLength.popleft()
        elif sideLength[-1] == slst:
            sideLength.pop()
        else:
            print("No")
            break
    else:
        print("Yes")
