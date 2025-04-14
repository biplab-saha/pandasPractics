import pandas as pd 
buttomCheck=pd.read_csv("sales_data_500.csv")
print(buttomCheck.tail())
print("****check to the top****")
print(buttomCheck.head())

print(buttomCheck.info())

print(buttomCheck.describe())