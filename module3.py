import pandas as pd

# Load dataset
df = pd.read_csv("student_dataset_v2.csv")

# 1. Remove duplicate records
df = df.drop_duplicates()

# 2. Handle missing values
# Option A: Drop rows with missing Marks
df = df.dropna(subset=["Marks"])

# Option B (alternative): Fill missing Marks with mean
# df["Marks"].fillna(df["Marks"].mean(), inplace=True)

# 3. Remove invalid entries
# Example: Negative study hours or attendance outside 0–100
df = df[(df["StudyHours"] >= 0) & (df["Attendance"].between(0, 100)) & (df["Marks"].between(0, 100))]

# 4. Validate attendance values
# Ensure attendance is between 0 and 100
invalid_attendance = df[~df["Attendance"].between(0, 100)]
print("Invalid attendance records:", invalid_attendance)

# 5. Validate study hours
# Assuming study hours should be between 0 and 12
invalid_hours = df[~df["StudyHours"].between(0, 12)]
print("Invalid study hours records:", invalid_hours)

# 6. Validate marks
# Marks should be between 0 and 100
invalid_marks = df[~df["Marks"].between(0, 100)]
print("Invalid marks records:", invalid_marks)

# 7. Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)
print("Cleaned dataset saved as cleaned_data.csv")
