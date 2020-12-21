# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
bools = list()
setA = set(map(int, input().split()))
for _ in range(int(input())):
    setN = set(map(int, input().split()))
    bools.append(setA.issuperset(setN))

    # loop for checking superset without using built-in function
    # for i in setN:
    #     bools.append(i in setA)
print(all(bools))
