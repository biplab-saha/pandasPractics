import pandas as pd
import numpy as np

file=pd.read_csv('Zomato.csv')
df=pd.DataFrame(file)

print (df)
print("-"*30)

# show all resturant that order delivered
delivered=df[df['Delivery']=='Yes']
print(delivered)
print('-'*30) 



# what is the average rating of all the resturant
rating=df['Rating'].mean()
print("all resturent average rating is: ",rating)
print('-'*30)



# sort returantes by average costing decending order
# sorting=df.sort_values(by='Avg_Cost_For_Tow',ascending=False)
# print(sorting)
print('-'*30) #error


# count how many locations in each location
count=df['Location'].value_counts()
print(count)
print('-'*30)


# find the resturent rating above 4.2
rate=df[df['Rating']>4.2]
print(rate)
print('-'*30)


# find the resturent get only their name and cuisine
find=df[['Name','Cuisine']]
print(find)










