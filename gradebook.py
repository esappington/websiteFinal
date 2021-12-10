# gradebook.py
import random

# Display the average of each student's grade.
# Display tthe average for each assignment.

gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64],
             [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72],
             [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96],
             [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94],
             [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78],
             [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89],
             [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67],
             [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92],
             [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80],
             [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72]]



#create a list with 10 numbers
numbers = []
for number in range(10):
    numbers.append(random.randint(1,100))

print(numbers)

#basic structure of list comprehension
#[(expression) (for loop) (optional condition(s)))
lc_numbers = [random.randint(1,100) for number in range(10)]
print(lc_numbers)

#perform element-wise operations on lc_numbers
squared_list = [number ** 2 for number in lc_numbers]
print(squared_list)

#gradebook example withe nested lists
#creates the student list
print("\n Gradebook example")
gradebook = []
for student in range(10):
    record = []
    for grade in range(15):
        record.append(random.randint(1,100))

    gradebook.append(record)


for student in gradebook:
    print(student)

#list comprehensions Gradebook example nested lists
#this uses one line of code and does the same thing as the gradebook example with nested loops
#works for the assignment scores
print("\nList comprehension gradebook example")
lc_gradebook = [[random.randint(1,100) for grade in range(15)] for student in range(10)]

for student in lc_gradebook:
    print(student)



#get assignment scores
print("\nAssignment Scores")
assignment_scores = []
for assignment in range(len(lc_gradebook[0])):
    scores = []
    for student in lc_gradebook:
        scores.append(student[assignment])

    assignment_scores.append(scores)

for assignment in assignment_scores:
    print(assignment)





#list comprehensions Gradebook example nested lists
#this works for the Student scores
print("\nList comprehension gradebook example")
lc_gradebook = [[random.randint(1,100) for grade in range(10)] for assignment in range(15)]

for assignment in lc_gradebook:
    print(assignment)

#get student scores
print("\nStudent scores")
student_scores = []
for student in range(len(lc_gradebook[0])):
    scores = []
    for assignment in lc_gradebook:
        scores.append(assignment[student])

    student_scores.append(scores)

for student in student_scores:
    print(student)




