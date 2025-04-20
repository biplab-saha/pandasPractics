import pandas as pd
file=pd.read_csv("sales_data.csv")
df=pd.DataFrame(file)

# print(df.shape[0]) #row indicate 0
# print(df.shape[1]) #column indicate 1
print(file)


# which payment meythod most use
payment=df['Payment Method'].value_counts().head(1) 
print(payment)



