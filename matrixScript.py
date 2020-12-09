#https://www.hackerrank.com/challenges/matrix-script/problem
import re
n,m = map(int,input().split())
matrix = []
for _ in range(n):
    matrix_item = list(input())
    matrix.append(matrix_item)

zipped = list(zip(*matrix))
string = "".join(["".join(x) for x in zipped])
text = re.sub('([\w])[\W]+([\w])', r'\1 \2', string)
print(re.sub('  ', ' ', text))