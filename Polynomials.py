#https://www.hackerrank.com/challenges/np-polynomials/problem
import numpy
coefficients = list(map(float,input().split()))
print(numpy.polyval(coefficients,int(input())))
