import pandas as pd
file=pd.read_csv("sales_data.csv")
df=pd.DataFrame(file)

# print(df.shape[0]) #row indicate 0
# print(df.shape[1]) #column indicate 1
print(file)


# which payment meythod most use
payment=df['Payment Method'].value_counts().head(1) 
print(payment)

# what is avarage revenue par order
# totalRevenue=df('Quantity')[''].sum()

# df['Revenue'] = df['Quantity'] * df['Unit_Price']

# order_revenue = df.groupby('Order_ID')['Revenue'].sum()

# average_revenue = order_revenue.mean()

# print(average_revenue)



# total number of customer
totalCustomer=df['Customer Name'].sum()
print(totalCustomer)

