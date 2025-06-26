import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('netflix_titles.csv')

tvShows=df[df['type']=='TV Show']
tvShows['release_year'].value_counts().plot(kind='line',color='red',marker='*')
plt.figure(figsize=(10,6))
plt.title("Duration between release date date and no of shows")
plt.xlabel('release date')
plt.ylabel('tv shows')
plt.tight_layout()
plt.show()
