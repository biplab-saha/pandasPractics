import pandas as pd
data=pd.read_csv('sales_data.csv')
df=pd.DataFrame(data)

# print(data.head())
# print(df.info())

# print(df.describe())

# check the null value in data sat
# print(df.isnull().sum())

#  find the number  row and column
print(df.shape)

# 




# Filter rows based on a condition