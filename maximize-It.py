# https://www.hackerrank.com/challenges/maximize-it/problem
from itertools import product
k, m = map(int, input().split())

# Slicing the 1st value and storing the rest of the given values in a nested listed because
# 1st value is about the no.of elements going to be in that line, which is not necessary in our further calculations
values = [list(map(int, input().split()))[1:] for _ in range(k)]

# Here,we get all the possible combinations of each element from each list through the product()
# and we can then perform the sum of their squares and modulus with the m value given
output = map(lambda x: sum(i**2 for i in x) % m, product(*values))

print(max(output))
