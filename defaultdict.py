# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
from collections import defaultdict
listA = defaultdict(list)
listB=[]
n, m = map(int,input().split())
for i in range(0,n):
    # taking the inputs as keys and appending their index value of each occurance as the value into the defalutdict(i.e listA)
    listA[input()].append(i+1) # listA = defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3, 5]}) this is according to 1st test case

for i in range(0,m):
    listB.append(input())#appending the inputs into the list of B.

# checking if elements in listB are also in listA.
# If True it would print out all the values(indexes) of the particular key from the listA else it would just give -1 as the output
for i in listB:
    if i in listA:
        print(" ".join( map(str,listA[i]) ))
    else:
        print(-1)

