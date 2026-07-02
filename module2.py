import pandas as pd

# Load dataset
df = pd.read_csv("student_dataset_v2.csv")

# 1. Find missing values
print("Missing values per column:")
print(df.isnull().sum())

# 2. Find duplicate records
print("\nDuplicate records count:", df.duplicated().sum())

# 3. Display descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())

# 4. Check memory usage
print("\nMemory usage:")
print(df.memory_usage(deep=True))

# 5. Display summary information
print("\nSummary info:")
print(df.info())
