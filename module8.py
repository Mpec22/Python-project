import pandas as pd

# Load transformed dataset
df = pd.read_csv("transformed_data.csv")

# 1. Average marks by grade
avg_marks_by_grade = df.groupby("Grade")["Marks"].mean()
print("\nAverage Marks by Grade:")
print(avg_marks_by_grade)

# 2. Number of students in each grade
students_per_grade = df.groupby("Grade")["ID"].count()
print("\nNumber of Students in Each Grade:")
print(students_per_grade)

# 3. Average attendance by grade
avg_attendance_by_grade = df.groupby("Grade")["Attendance"].mean()
print("\nAverage Attendance by Grade:")
print(avg_attendance_by_grade)
