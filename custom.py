# list1 = [(1, 3), (1, 4), (2, 3), (2, 4)]
# list2 = [1, 2, 3, 4, 5]
# -------
# print the following:
#
# from List1: only when sum is even number:
#
# 1 + 3 = 4
# 2 + 4 = 6
#
# from list 2: print only even numbers:
# 2 is even number
# 4 is even number
list1 = [(1, 3), (1, 4), (2, 3), (2, 4)]
list2 = [1, 2, 3, 4, 5]
[print(f"{m} + {n} = {m+n}") for m,n in list1 if (m+n)%2==0]
[print(f"{i} is even number") for i in list2 if i%2==0]