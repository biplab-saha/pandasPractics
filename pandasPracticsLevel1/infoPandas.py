import pandas as pd 
checkInfo=pd.read_csv("short_sales_data.csv")
print(checkInfo.info())