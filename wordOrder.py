# https://www.hackerrank.com/challenges/word-order/problem
from collections import Counter
words = []
for i in range(int(input())):
    word = input()
    words.append(word)
print(len(set(words)))
print(*(Counter(words).values()))

