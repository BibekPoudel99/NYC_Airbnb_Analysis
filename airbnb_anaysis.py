import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('AB_NYC_2019/AB_NYC_2019.csv') #load dataset

#data cleaning
#display basic info
# print("Dataset info:\n")
# print(df.info())
# print("\nFirst five rows:\n")
# print(df.head())

#handle missing value
print("Handling missing values....\n")
df.isnull().sum() #check for missing value and sum method sums these boolean vlaues for each coumn, effectively counting the numver of missing values in eaach column of the dataframe.

df.fillna({'reviews_per_month' : 0}, inplace=True) #fill missing value with 0.
df.dropna(subset=['host_name', 'name'], inplace=True) #drop rows with missing hostname

#convert data types
df['last_review'] = pd.to_datetime(df['last_review']) #convert last review to datetime

#exploratory data analysis(eda)
print("\nSummary Statistics")
df.describe() 

#price distribution
plt.figure(figsize= (10,6))
sns.histplot(df['price'], bins=100, kde=True) #histogram having 100 bins and adds kernel density estimate line to the plot which is smoothed version of histogram
plt.xlim(0, 500)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()