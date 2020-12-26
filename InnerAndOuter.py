#https://www.hackerrank.com/challenges/np-inner-and-outer/problem
import numpy
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(numpy.inner(A, B))
print(numpy.outer(A, B))