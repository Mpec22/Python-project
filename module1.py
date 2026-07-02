import pandas as pd

# 1. Read the CSV file
df = pd.read_csv("student_dataset_v2.csv")

# 2. Display the first five records
print("First 5 records:")
print(df.head())

# 3. Display the last five records
print("\nLast 5 records:")
print(df.tail())

# 4. Print the shape of the dataset (rows, columns)
print("\nShape of dataset:", df.shape)

# 5. Print column names
print("\nColumn names:", df.columns.tolist())

# 6. Display data types of each column
print("\nData types:")
print(df.dtypes)
