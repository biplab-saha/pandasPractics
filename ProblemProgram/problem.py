import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('netflix_titles.csv')

# i want to check if any missing value are present in the dataset
# print(df.isnull().sum())


# i want to find any duplicate values in the dataset
# print(df.duplicated().sum())


# i want to find the number of unique value in the 'type' column
# print(df['type'].unique())


# question in company
# how many movies vs tv shows are there in the dataset
typeCounts=df['type'].value_counts()
plt.figure(figsize=(8,5))
typeCounts.plot(kind='bar',color=['blue','cyan'])
plt.title('Number of Movies vs Tv shows')
plt.xlabel('Type')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.tight_layout()
plt.show()
