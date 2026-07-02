import pandas as pd
import os

# Load transformed dataset
df = pd.read_csv("transformed_data.csv")

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# 1. Save cleaned dataset
df.to_csv("output/cleaned_data.csv", index=False)

# 2. Save toppers (students with Grade 'A')
toppers = df[df["Grade"] == "A"]
toppers.to_csv("output/toppers.csv", index=False)

# 3. Save failed students (students with Result 'Fail')
failed_students = df[df["Result"] == "Fail"]
failed_students.to_csv("output/failed_students.csv", index=False)

# 4. Generate report
report = {
    "Total Students": len(df),
    "Passed Students": (df["Result"] == "Pass").sum(),
    "Failed Students": (df["Result"] == "Fail").sum(),
    "Highest Marks": df["Marks"].max(),
    "Lowest Marks": df["Marks"].min(),
    "Average Marks": df["Marks"].mean(),
    "Average Attendance": df["Attendance"].mean(),
    "Grade Distribution": df["Grade"].value_counts().to_dict()
}

report_df = pd.DataFrame(list(report.items()), columns=["Metric", "Value"])
report_df.to_csv("output/report.csv", index=False)

print("All files have been generated and stored inside the 'output' folder.")
