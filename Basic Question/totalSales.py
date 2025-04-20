import pandas as pd
file=pd.read_csv('sales_data.csv')
df=pd.DataFrame(file)

totalSales=df['Total Sales'].sum()
print("Total Sales: ",totalSales)
# print(df)