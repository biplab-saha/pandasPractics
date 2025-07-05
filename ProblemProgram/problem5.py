# top 10 country with the highest number in shows using pie chat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('netflix_titles.csv')

top_con=df['country'].value_counts().head(10)
top_con.plot(kind='bar',color='orange',edgecolor='black')
plt.figure(figsize=(20,10))
plt.title('top 10 countries')
plt.xlabel('shows')
plt.ylabel('countries')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

