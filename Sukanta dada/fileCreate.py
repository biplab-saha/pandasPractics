import pandas as pd
data={
    'Restaurant_ID':[101,102,103,104,105],
    'Name':['The Spice House','Sushi Central','Pizza Fiesta','Curry Kingdom','Burder Barn'],
    'Location':['Delhi','Mumbai','Bangalore','Hyderabad','Pune'],
    'Cuisine':['North India','Japanese','ltalian','South India','American'],
    'Rating':[4.3,4.6,4.0,3.8,4.1],
    'Avg_Cost_For_Two':[800,1500,600,700,500],
    'Delivery':['Yes','No','Yes','Yes','No']
}

df=pd.DataFrame(data)
df.to_csv('Zomato.csv')