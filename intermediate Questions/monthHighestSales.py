import pandas as pd
file=pd.read_csv('sales_data.csv')
df=pd.DataFrame(file)


# print(df.groupby(pd.to_datetime(df['Date']).dt.month_name())['Total Sales'].sum().idxmax())
