import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('studentData.csv')
# print(df.head())
# print(df.info())
# print(df.describe())


# count a null Value
# print(df.isnull().sum())

# drop unmaned column
df = df.drop('Unnamed: 0',axis=1)
# print(df)


# # change weekly study hours column
# changeWeeklyStudyHours = df['WklyStudyHours'] = df['WklyStudyHours'].str.replace('< 5 ' , '5 - 10')
# print(df.head())



# gender distribution
ax = sns.countplot(data = df , x= 'Gender' )
ax.bar_label (ax.containers[0])
plt.figure(figsize=(6,4))
plt.show()