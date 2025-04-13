import pandas as pd
data=pd.read_csv("short_sales_data.csv")
df=pd.DataFrame(data)
# print(df['Quantity'])


# df=pd.DataFrame(data)
print(df[['Date','Price']])