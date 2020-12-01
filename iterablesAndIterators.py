# https://www.hackerrank.com/challenges/iterables-and-iterators/problem
from itertools import combinations
n = int(input())  # denoting the length of the list
lst = input().split()  # space-separated lowercase English letters, denoting the elements of the list.
k = int(input())  # denoting the number of indices to be selected.
combinations = list(combinations(lst, k))
count = 0
for i in combinations:
    if 'a' in i:
        count += 1
print("{:.4f}".format(count/len(combinations)))
