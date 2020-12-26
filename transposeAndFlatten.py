# hackerrank.com/challenges/np-transpose-and-flatten/problem
import numpy
n,m = map(int,input().split())
array = numpy.array([input().split() for _ in range(n)],dtype=int)
print(numpy.transpose(array))
print(array.flatten())
