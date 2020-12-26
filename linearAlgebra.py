#https://www.hackerrank.com/challenges/np-linear-algebra/problem
from numpy import linalg
matrix = list()
for _ in range(int(input())):
    matrix.append(list(map(float,input().split())))
print(round(linalg.det(matrix),2))