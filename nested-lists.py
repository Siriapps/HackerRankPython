# https://www.hackerrank.com/challenges/nested-list/problem
myList = []
for n in range(int(input())):
    myList.append([input(), float(input())]) #Ex- mylist=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

secondLowest = sorted(list(set(score for (name, score) in myList)))[1]# this sorts the unique scores in descending order
                                                                      # and grabs the first number which is the second lowest score

# to check the condition if two or more people got the second lowest
# if so then it prints the sorted names
print("\n".join(sorted(list(name for (name, score) in myList if score == secondLowest))))
