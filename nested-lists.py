l = []
second_lowest_names = []
scores = set()

for _ in range(int(input("Enter How many students: "))):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    l.append([name, score])
    scores.add(score)# adding the scores to the scores in which set function helps us only take
                     # unique values and it also sorts the values helping us to find the second_lowest score

        
second_lowest = sorted(scores)[1] #this sorts the scores in descending order
                                  # and grabs the first number which is the second lowest score

# to check the condition if two or more people got the second lowest
# if so then it prints the sorted names
for name, score in l:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name, end='\n')
