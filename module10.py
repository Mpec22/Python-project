import pandas as pd

# Load transformed dataset
df = pd.read_csv("transformed_data.csv")

# 1. Total Students
total_students = len(df)

# 2. Number of Passed Students
passed_students = (df["Result"] == "Pass").sum()

# 3. Number of Failed Students
failed_students = (df["Result"] == "Fail").sum()

# 4. Highest Marks
highest_marks = df["Marks"].max()

# 5. Lowest Marks
lowest_marks = df["Marks"].min()

# 6. Average Marks
average_marks = df["Marks"].mean()

# 7. Average Attendance
average_attendance = df["Attendance"].mean()

# 8. Grade-wise Distribution
grade_distribution = df["Grade"].value_counts().to_dict()

# Create report dictionary
report = {
    "Total Students": total_students,
    "Passed Students": passed_students,
    "Failed Students": failed_students,
    "Highest Marks": highest_marks,
    "Lowest Marks": lowest_marks,
    "Average Marks": average_marks,
    "Average Attendance": average_attendance,
    "Grade Distribution": grade_distribution
}

# Convert to DataFrame for saving
report_df = pd.DataFrame(list(report.items()), columns=["Metric", "Value"])

# Save report
report_df.to_csv("report.csv", index=False)
print("Final report saved as report.csv")
