# https://www.hackerrank.com/challenges/designer-door-mat/problem

size = list(map(int,input().split()))
rows = size[0]
columns = size[1]

# printing the top half of the mat
for i in range(rows // 2):
    printString = ".|." * ((i * 2) + 1)
    print(printString.center(columns, "-"))

print('WELCOME'.center(columns, '-'))

# printing the bottom half of the mat
for i in reversed(range(rows // 2)):
    printString = ".|." * ((i * 2) + 1)
    print(printString.center(columns, "-"))



