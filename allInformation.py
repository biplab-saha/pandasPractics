import pandas as pd
newDict={
    'name':['Biplab','nayan','mrinmoy','rinki','sandhya','bhanumati','dinesh','papiya','bibhuti'],
    'cityName':['Majdia','Majdia','Majdia','Majdia','Majdia','Majdia','Majdia','Majdia','Majdia'],
    'age':[20,23,26,20,40,45,50,60,50]
}

# df=pd.DataFrame(newDict)

# print(df) #show all list

# print(df.head(2))# top thake dakhabe braket vator ja value daba satuku e daba..
# print(df.tail(3))#buttom thake dakhaba ata tao tumi ja value daba sathai dakha ba...

#print (df.describe())#numarical value analysiecs korba..
# df.to_csv('biplab.csv') #convert csv file

# biplabFile=pd.read_csv("biplab.csv")
# df=pd.DataFrame(biplabFile)


#print(biplabFile['name'][0])#coulum diya file exces korche and index number diya amer dakta parchie..



# value change korete parbo...
# biplabFile['age'][0]=23
# print(biplabFile)




# create a new csv file
# biplabFile.to_csv('biplab2.csv')


biplabNewFile=pd.read_csv('biplab2.csv')
#change head name
biplabNewFile.index=['first','second','thrid','forth','five','six','seven','eight','ning']
print(biplabNewFile)
df=pd.DataFrame(biplabNewFile)
df.to_csv("newBiplabCsvFile.csv")













