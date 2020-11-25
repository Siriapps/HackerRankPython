# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

# from collections import namedtuple
# n = int(input()) # number of Students
# fields = input().split() #different types of fields like- ID,MARKS,CLASS,NAME
# Students = namedtuple('Students',fields)
# total = 0
# for i in range(n):
#     fields1, fields2, fields3, fields4 = input().split()
#     details = Students(fields1,fields2,fields3,fields4)
#
#     total+= int(details.MARKS) #summing up all the marks
#
# #average
# print('{:.2f}'.format(total/n)) #here,.2f helps print the value only till 2 decimals of the floating point numbers


#####################################
########### 4 Lines Of Code #########
#####################################
from collections import namedtuple
n,Students = int(input()),namedtuple('Students',input().split())
print('{:.2f}'.format(sum([int(Students(*input().split()).MARKS) for _ in range(n)])/n))
