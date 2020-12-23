# https://www.hackerrank.com/challenges/polar-coordinates/problem
import cmath

complexNum = input()
print(abs(complex(complexNum)))# r value
print(cmath.phase(complex(complexNum)))# phi value

# We can use polar() instead of abs() and phase()
# print(cmath.polar(complex(complexNum)))
