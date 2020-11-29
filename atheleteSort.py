# https://www.hackerrank.com/challenges/python-sort-sort/problem
if __name__ == '__main__':
    n,m = map(int,input().split())
    arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
    k = int(input())
    for row in sorted(arr,key=lambda row:int(row[k])):
        print(*row)
