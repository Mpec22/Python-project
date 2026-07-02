import pandas as pd

# Load transformed dataset
df = pd.read_csv("transformed_data.csv")

# 1. Mean
print("\nMean values:")
print(df[["Marks", "Attendance", "StudyHours"]].mean())

# 2. Median
print("\nMedian values:")
print(df[["Marks", "Attendance", "StudyHours"]].median())

# 3. Mode
print("\nMode values:")
print(df[["Marks", "Attendance", "StudyHours"]].mode().iloc[0])

# 4. Standard Deviation
print("\nStandard Deviation:")
print(df[["Marks", "Attendance", "StudyHours"]].std())

# 5. Variance
print("\nVariance:")
print(df[["Marks", "Attendance", "StudyHours"]].var())

# 6. Correlation Matrix
print("\nCorrelation Matrix:")
print(df[["Marks", "Attendance", "StudyHours"]].corr())
