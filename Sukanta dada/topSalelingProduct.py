import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
file=pd.read_csv('sales_data.csv')
df=pd.DataFrame(file)


#top selling product
topProduct=df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(1)
# print(topProduct)
print(df)
plt.bar(df['Price'],df['Payment Method'])
plt.show()

