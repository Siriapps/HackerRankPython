# https://www.hackerrank.com/challenges/py-set-mutations/problem

numA = int(input())
A = set(map(int,input().split()))
for _ in range((int(input()))):
    func,numElements = input().split()
    elements = set(map(int,input().split()))
    if func == "update":
        A.update(elements)
    elif func == "intersection_update":
        A.intersection_update(elements)
    elif func == "symmetric_difference_update":
        A.symmetric_difference_update(elements)
    elif func == "difference_update":
        A.difference_update(elements)

print(sum(A))