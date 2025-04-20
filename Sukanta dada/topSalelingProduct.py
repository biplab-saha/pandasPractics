import pandas as pd
file=pd.read_csv('sales_data.csv')
df=pd.DataFrame(file)


#top selling product
topProduct=df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(1)
print(topProduct)