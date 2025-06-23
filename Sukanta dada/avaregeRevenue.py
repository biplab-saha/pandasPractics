import pandas as pd
file=pd.read_csv('sales_data.csv')
df=pd.DataFrame(file)
print(file)
# what is avarage revenue par order
totalRevenue=df('Quantity')[''].sum()

df['Revenue'] = df['Quantity'] * df['Unit_Price']

order_revenue = df.groupby('Order_ID')['Revenue'].sum()

average_revenue = order_revenue.mean()

print(average_revenue)
