import pandas as pd
file=pd.read_csv('sales_data.csv')
df=pd.DataFrame(file)

print(df.head(5))