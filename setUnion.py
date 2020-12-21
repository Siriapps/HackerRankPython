#https://www.hackerrank.com/challenges/py-set-union/problem
numEng = int(input())
eng = set(map(int,input().split()))

numFrench = int(input())
french = set(map(int,input().split()))

print(len(eng.union(french)))
