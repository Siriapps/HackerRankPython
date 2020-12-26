#https://www.hackerrank.com/challenges/np-array-mathematics/problem
import numpy
n,m = map(int,input().split())

a = numpy.array([input().split() for _ in range(n)], dtype=int)
b = numpy.array([input().split() for _ in range(n)], dtype=int)
print(f"{a+b}\n{a-b}\n{a*b}\n{a//b}\n{a%b}\n{a**b}")
