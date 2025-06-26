# top 10 country with the highest number in shows using pie chat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('netflix_titles.csv')

topCountry=df['country'].value_counts().head(10)
print(topCountry)
plt.figure(figsize=(10,6))
plt.title('')
plt.xlabel('')
plt.ylabel('')

