# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
import numpy
n,m = map(int,input().split())
array = numpy.array([input().split() for _ in range(n)],dtype=int)
print(numpy.mean(array,axis=1))
print(numpy.var(array,axis=0))
print(round(numpy.std(array),11))