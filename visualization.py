import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV File
file_name = "c:\\Users\\user\\Downloads\\organizations-100000.csv"
try:
    data = pd.read_csv(file_name)
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"File '{file_name}' not found. Please ensure it is in the same directory.")


# Top 10 countries with the most organizations
top_countries = data['Country'].value_counts().head(10)

top_countries.plot(kind='bar', color='skyblue')
plt.title("Top 10 Countries by Number of Organizations")
plt.xlabel("Country")
plt.ylabel("Number of Organizations")
plt.show()

# Pie Chart
# Top 5 industries
top_industries = data['Industry'].value_counts().head(5)

top_industries.plot(kind='pie', autopct='%1.1f%%')
plt.title("Top 5 Industries by Percentage")
plt.ylabel("")  # Remove default y-axis label
plt.show()
