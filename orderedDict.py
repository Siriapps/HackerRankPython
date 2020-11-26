# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item,space,price = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(price)#We are setting the value of the item as the sum of its previous value and its price
for item, quantity in d.items():
    print(item, quantity)
