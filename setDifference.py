#https://www.hackerrank.com/challenges/py-set-difference-operation/problem
numEng = int(input())
eng = set(map(int,input().split()))

numFrench = int(input())
french = set(map(int,input().split()))

print(len(eng.difference(french)))
