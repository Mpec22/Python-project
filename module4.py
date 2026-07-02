import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# 1. Grade column
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 45:
        return "D"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(assign_grade)

# 2. Result column (Pass/Fail)
# Assuming pass mark is 40
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# 3. Performance Score
# Custom formula combining Marks, Attendance, and StudyHours
# Example: weighted average
df["PerformanceScore"] = (
    (df["Marks"] * 0.5) + 
    (df["Attendance"] * 0.3) + 
    (df["StudyHours"] * 2)   # scaled study hours
)

# Save transformed dataset
df.to_csv("transformed_data.csv", index=False)
print("Transformed dataset saved as transformed_data.csv")
