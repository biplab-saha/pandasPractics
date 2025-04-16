import pandas as pd

# Reading an Excel file
hello = pd.read_csv('short_sales_data.csv')

# Display the first few rows
print("*******View the top rows*******")
print(hello.head())

print("*******View the bottom rows*******")
print(hello.tail())

print("*******Get information about the DataFrame*******")
print(hello.info())


print("*******Get summary statistics*******")
print(hello.describe())
