import pandas as pd
df=pd.read_csv('sales_data.csv')
print(df.to_string())
print(pd.__version__)