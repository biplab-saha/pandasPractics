import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('netflix_titles.csv')

# what is the percent of each content type(PG,R,TV-MA)in a dataset
contentTypeCounts=(df['rating'].value_counts()/len(df))*100
# print(contentTypeCounts)
plt.figure(figsize=(11,6))
contentTypeCounts.plot(kind='pie',color='skyblue')
plt.title('Content Type Distribution')
plt.xlabel('Content Type')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45)
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.legend(title='Content Type',loc='center left',bbox_to_anchor=(1,0.5))
plt.tight_layout()
plt.show()

