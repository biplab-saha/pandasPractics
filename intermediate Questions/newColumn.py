import pandas as pd
file=pd.read_csv("sales_data.csv")
df=pd.DataFrame(file)
# topProduct=df.groupby('Product')['Total Sales'].sum().nlargest()
# print(topProduct)
# print(df.columns)
print(df['Total Sales'].sum())

# df['profit']=