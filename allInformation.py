import pandas as pd
newDict={
    'name':['Biplab','nayan','mrinmoy','rinki','sandhya','bhanumati','dinesh','papiya','bibhuti'],
    'cityName':['Majdia','Majdia','Majdia','Majdia','Majdia','Majdia','Majdia','Majdia','Majdia'],
    'age':[20,23,26,20,40,45,50,60,50]
}

df=pd.DataFrame(newDict)

# print(df) #show all list

print(df.head(2))# top thake dakhabe braket vator ja value daba satuku e daba..
print(df.tail(3))#buttom thake dakhaba ata tao tumi ja value daba sathai dakha ba...

