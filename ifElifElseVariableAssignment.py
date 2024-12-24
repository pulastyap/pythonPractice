# For learning if conditional statement

grade_A_marks = 90
grade_B_marks = 75

student_marks = int(input("Enter your marks: "))

grade = "Grade A" if student_marks >= grade_A_marks else "Grade B" if student_marks >= grade_B_marks else "Grade C"

print(grade)