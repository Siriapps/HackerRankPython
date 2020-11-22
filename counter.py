# https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter

n = int(input())  # Number of shoes
shoes = Counter(map(int, input().split()))  # Number of shoes in stock
customers = int(input())  # number of customers
total = []
for i in range(customers):
    size, price = map(int, input().split())
    # checking if the shoe size is present in the shoes
    if shoes[size] > 0:
        total.append(price)  # then,appending the price of that shoe size
        shoes.subtract(Counter([size])) # removing the number of occurances of the particular shoe size
                                        # in the shoes in order to execute the condition i.e the no.of shoes
                                        # in stock and the number of times the customer has asked for that shoe
                                        # size should match and the prices of those shoe sizes would only be considered
                                        # while calculating the total.

print(sum(total)) # total income
