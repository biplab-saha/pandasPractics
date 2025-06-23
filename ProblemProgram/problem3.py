import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('netflix_titles.csv')

# what is the distribution of movie durations in the dataset
movie=df[df['type']=='Movie'].copy()
movie['duration']=movie['duration'].str.replace('min', "").astype(float)

plt.figure(figsize=(10,6))
plt.hist(movie['duration'],bins=30,color='lightblue',edgecolor='black')
plt.title("Destribution of Movie Duration")
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.tight_layout()
plt.show()