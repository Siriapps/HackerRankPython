# https://www.hackerrank.com/challenges/np-arrays/problem
import numpy

def arrays(arr):
    return numpy.array(list(reversed(arr)),dtype=float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)