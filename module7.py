import pandas as pd

# Load transformed dataset
df = pd.read_csv("transformed_data.csv")

# 1. Students sorted by Marks (descending order: highest first)
print("\nStudents sorted by Marks:")
print(df.sort_values(by="Marks", ascending=False).head(10))  # top 10

# 2. Students sorted by Attendance (descending order)
print("\nStudents sorted by Attendance:")
print(df.sort_values(by="Attendance", ascending=False).head(10))  # top 10

# 3. Students sorted by Study Hours (descending order)
print("\nStudents sorted by Study Hours:")
print(df.sort_values(by="StudyHours", ascending=False).head(10))  # top 10
