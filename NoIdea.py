# https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
array = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

print(sum((i in setA) - (i in setB) for i in array))
# True = 1 and False = 0
