#https://www.hackerrank.com/challenges/py-check-subset/problem
bools = list()
for _ in range(int(input())):
    numA = int(input())
    setA = set(map(int,input().split()))
    numB = int(input())
    setB = set(map(int,input().split()))

    print(setA.issubset(setB))

# loop for solving this problem instead of using built in function "issubset"
    # for a in setA:
    #     bools.append(a in setB)
    # print(all(bools)==True)



