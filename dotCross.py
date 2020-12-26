# https://www.hackerrank.com/challenges/np-dot-and-cross/problem
import numpy
n = int(input())
arrayA = numpy.array([input().split() for _ in range(n)],dtype=int)
arrayB = numpy.array([input().split() for _ in range(n)],dtype=int)
print(numpy.dot(arrayA,arrayB)) # Matrix Multiplication