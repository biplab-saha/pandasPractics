import pandas as pd
file=pd.read_csv('sales_data.csv')
df=pd.DataFrame(file)
# print(df.columns)
total=df.groupby('Category')['Total Sales'].sum()
print(total)