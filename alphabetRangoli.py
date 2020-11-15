# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
from string import ascii_lowercase


def print_rangoli(size):
    alpha = ascii_lowercase
    for i in range(size-1,-1,-1):
        print('-'.join(alpha[i:size][::-1]+alpha[i+1:size]).center((4*size)-3,'-'))

    for i in range(1,size):
        print('-'.join(alpha[i:size][::-1]+alpha[i+1:size]).center((4*size)-3,'-'))


if __name__ == '__main__':
    n = int(input("Size: "))
    print_rangoli(n)
