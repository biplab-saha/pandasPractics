import pandas as pd
file = pd.read_csv('sales_data.csv')
df=pd.DataFrame(file)

# which payment meythod most use
payment=df['Payment Method'].value_counts().head(1) 
print(payment)