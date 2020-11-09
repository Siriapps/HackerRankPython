n = int(input("Enter no.of students:"))
student_marks = {} 
for _ in range(n):
    name, *line = input("enter name:").split() # here we are taking
                                               # the name and the scores all
                                               # in the same line
    scores = list(map(float, line))
    student_marks[name] = scores #storing the names and scores in student_marks dictionary
query_name = input("enter query_name:")

avg = sum(student_marks[query_name])/3# finding the average

print("%.2f" % avg)#this line helps to print only two decimal places

    
