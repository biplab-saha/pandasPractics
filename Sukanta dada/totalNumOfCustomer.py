import pandas as pd
file=pd.read_csv('sales_data.csv')
df=pd.DataFrame(file)


# total number of customer
totalCustomer=df['Customer Name'].count()
print(totalCustomer)

