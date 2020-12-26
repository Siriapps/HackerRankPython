#https://www.hackerrank.com/challenges/np-concatenate/problem
import numpy
n,m,p = map(int,input().split())

arrayN = numpy.array([input().split() for _ in range(n)],dtype=int)
arrayM = numpy.array([input().split() for _ in range(m)],dtype=int)
print(numpy.concatenate((arrayN,arrayM),axis=0))