#https://www.hackerrank.com/challenges/ginorts/problem
s = input()
lower,upper,even,odd = [],[],[],[]
for i in s:
    if i.isalpha():
        if i.islower(): lower.append(i)
        if i.isupper(): upper.append(i)
    if i.isdigit():
        if int(i)%2 == 0: even.append(i)
        else:
            odd.append(i)
print("".join((*sorted(lower),*sorted(upper),*sorted(odd),*sorted(even))))
