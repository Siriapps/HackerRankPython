n = int(input())
lst = map(int, input().split())
compare = []
palindrome = []
for i in lst:
    compare.append(i>0)
    palindrome.append(str(i) == str(i)[::-1])
print(all(compare) and any(palindrome))

