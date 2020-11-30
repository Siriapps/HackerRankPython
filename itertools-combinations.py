# https://www.hackerrank.com/challenges/itertools-combinations/problem
from itertools import combinations
s,n = input().split()
for i in range(1,int(n)+1):
    print(*[''.join(p) for p in combinations(sorted(s),i)],sep='\n')
