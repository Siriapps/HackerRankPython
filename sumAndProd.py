# https://www.hackerrank.com/challenges/np-sum-and-prod/problem
import numpy
n,m = map(int,input().split())
array = numpy.array([input().split() for _ in range(n)],dtype=int)
print(numpy.prod(numpy.sum(array,axis=0)))
