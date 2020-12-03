# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
cube = lambda x: x ** 3
def fibonacci(n):
    if n == 1:return [0]
    elif n == 0:return []
    else:
        series = [0,1]
        for _ in range(2,n):
            series.append(series[-1]+series[-2])
        return series


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
