'''
The newly appointed Vice-Chancellor of Anna University wanted to create an automated grading system for the students to check their grade. When a student enters a mark, the grading system displays the corresponding grade.
Write a program to solve the given problem.
  Marks scored  
  Grade 
100
S
90 - 99
A
80 - 89
B
70 - 79
C
60 - 69
D
50 - 59
E
<50
F
Input format:
The input consists of one integer which corresponds to the marks scored by the student
'''
# Get the marks scored by the student
marks = int(input("Enter the marks scored by the student: "))

# Determine the grade based on the marks
if marks == 100:
    grade = "S"
elif 90 <= marks <= 99:
    grade = "A"
elif 80 <= marks <= 89:
    grade = "B"
elif 70 <= marks <= 79:
    grade = "C"
elif 60 <= marks <= 69:
    grade = "D"
elif 50 <= marks <= 59:
    grade = "E"
elif marks < 50:
    grade = "F"
else:
    grade = "Invalid marks"

# Display the grade
print(f"The grade is: {grade}")
'''
Enter the marks scored by the student: 95
The grade is: A

