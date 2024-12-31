import pandas as pd

# Load the CSV File
file_name = "c:\\Users\\user\\Downloads\\organizations-100000.csv"
try:
    data = pd.read_csv(file_name)
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"File '{file_name}' not found. Please ensure it is in the same directory.")

# Display the first few rows of the data 
print("\nDataset Information:")
print(data.info())

# Display summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Check for missing values 
print("\nMissing Values:")
print(data.isnull().sum())

# Example: Count rows based on a specific column (replace 'column_name' with an actual column)
print("\nCount by Column:")
print(data['Name'].value_counts())

# Filter rows where the 'Founded' column is 2005
filtered_data = data[data['Founded'] == 2005]
print("\nFiltered data:")
print(filtered_data)
