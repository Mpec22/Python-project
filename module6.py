import pandas as pd

# Load transformed dataset
df = pd.read_csv("transformed_data.csv")

# 1. Average Marks
avg_marks = df["Marks"].mean()
print("Average Marks:", avg_marks)

# 2. Highest Marks
highest_marks = df["Marks"].max()
print("Highest Marks:", highest_marks)

# 3. Lowest Marks
lowest_marks = df["Marks"].min()
print("Lowest Marks:", lowest_marks)

# 4. Average Attendance
avg_attendance = df["Attendance"].mean()
print("Average Attendance:", avg_attendance)

# 5. Average Study Hours
avg_study_hours = df["StudyHours"].mean()
print("Average Study Hours:", avg_study_hours)

# 6. Pass Percentage
pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()
total = len(df)
pass_percentage = (pass_count / total) * 100
fail_percentage = (fail_count / total) * 100
print("Pass Percentage:", pass_percentage)
print("Fail Percentage:", fail_percentage)

# 7. Grade Distribution
grade_distribution = df["Grade"].value_counts()
print("\nGrade Distribution:")
print(grade_distribution)
