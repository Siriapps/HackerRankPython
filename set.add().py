# https://www.hackerrank.com/challenges/py-set-add/problem

# about .add() function in sets
# >>> s = set('HackerRank')
# >>> s.add('H')
# >>> print s
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# >>> print s.add('HackerRank')
# None
# >>> print s
# set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])

n = int(input())
stamps = set()
for i in range(n):
    country = input()
    stamps.add(country)

print(len(stamps))


