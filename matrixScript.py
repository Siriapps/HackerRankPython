#https://www.hackerrank.com/challenges/matrix-script/problem
import re
n,m = map(int,input().split())
matrix = []
for _ in range(n):
    matrix_item = list(input())
    matrix.append(matrix_item)
string = "".join(map(str,list(sum(tuple(zip(*matrix)), ()))))
text = re.sub('([\w])[\W]+([\w])', r'\1 \2', string)
text = re.sub('  ', ' ', text)
print(text)