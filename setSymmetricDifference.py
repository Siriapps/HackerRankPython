#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
numEng = int(input())
eng = set(map(int,input().split()))

numFrench = int(input())
french = set(map(int,input().split()))

print(len(eng.symmetric_difference(french)))
