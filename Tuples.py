n = int(input("enter n:"))
integer_list = map(int, input("enter: ").split())
t = tuple(integer_list)
print(hash(t))
