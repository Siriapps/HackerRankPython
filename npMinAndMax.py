# https://www.hackerrank.com/challenges/np-min-and-max/problem
import numpy
n,m = map(int,input().split())
array = numpy.array([input().split() for _ in range(n)],dtype=int)
print(numpy.max(numpy.min(array,axis=1)))
