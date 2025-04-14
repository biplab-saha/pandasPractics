import pandas as pd
checkIndex=pd.read_csv("sales_data_500.csv")
df=pd.DataFrame(checkIndex)
# Row by index
print("Row by index")
print(df.iloc[[1,]])
# row by label
print("row by label")
print(df.loc[[1,3,6,95,3]])