#https://www.hackerrank.com/challenges/zipped/problem
col,row = map(int,input().split())
subjects = []
for _ in range(row):
    subjects.append(list(map(float,input().split())))
total = [zip(*subjects)]
for i in total:
    for j in i:
        print((sum(list(j)))/row)
