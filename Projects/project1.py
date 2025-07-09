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
print(df)


# # change weekly study hours column
# changeWeeklyStudyHours = df['WklyStudyHours'] = df['WklyStudyHours'].str.replace('< 5 ' , '5 - 10')
# print(df.head())



# gender distribution
ax = sns.countplot(data = df , x= 'Gender' )
plt.title('Gender Distribution')
ax.bar_label (ax.containers[0])
plt.figure(figsize=(6,4))
# plt.show()


# form the above chat we have analysed that the number of females of the data is more then the number of male 

gp=df.groupby('ParentEduc').agg({"MathScore":'mean','ReadingScore':'mean','WritingScore':'mean'})
print(gp)

# plt.figure(figsize=(5,5))
sns.heatmap(gp, annot=True)
plt.title("Relations Between Parent's Education and Student's score")
plt.show()
# form the above chart we have concluded that the education of the parents have a good impact  on their student 



ParentMaritalStatusCheck = df.groupby('ParentMaritalStatus').agg({"MathScore":'mean','ReadingScore':'mean','WritingScore':'mean'})
print(ParentMaritalStatusCheck )
sns.heatmap(ParentMaritalStatusCheck,annot=True)
plt.title("Relations Between Parent's Marital Status and Student's score")
plt.figure(figsize=(5,5))
plt.show()


# boxplot check for outliers
sns.boxplot(data=df , x= "MathScore")
plt.show()


print(df['EthnicGroup'].unique())
# Distribution of EthniGroup
groupA=df.loc[(df['EthnicGroup'] == "group A")].count()
groupB=df.loc[(df['EthnicGroup'] == "group B")].count()
groupC=df.loc[(df['EthnicGroup'] == "group C")].count()
groupD=df.loc[(df['EthnicGroup'] == "group D")].count()
groupE=df.loc[(df['EthnicGroup'] == "group E")].count()

myList = [groupA['EthnicGroup'],groupB['EthnicGroup'],groupC['EthnicGroup'],groupD['EthnicGroup'],groupE['EthnicGroup']]
l = ["group A","group B","group C","group D","group E"]
plt.title('Distributions Of Ethnic Groups')
plt.pie(myList, labels = l, autopct="%1.2f%%")
plt.show()

#  check value eg. group label thake aschilo....
ax = sns.countplot(data=df, x= 'EthnicGroup')
ax.bar_label(ax.containers[0])
plt.show()

