n = int(input("enter no.of scores:"))
arr = list(map(int,input("enter array of scores:").split()))
temp = []
for x in arr:
    if x not in temp:
        temp.append(x)
temp.sort(reverse=True)
print(temp[1])


