#https://www.hackerrank.com/challenges/np-eye-and-identity/problem
import numpy
numpy.set_printoptions(legacy='1.13')# It enables 1.13 legacy printing mode. This approximates numpy 1.13 print output
                                    # by including a space in the sign position
# 'n' denotes the rows.
# 'm' denotes the columns.
n,m = map(int,input().split())
print(numpy.eye(n,m))
