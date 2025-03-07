import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('AB_NYC_2019/AB_NYC_2019.csv') #load dataset

#data cleaning
#display basic info
print("Dataset info:\n")
print(df.info())
print("\nFirst five rows:\n")
print(df.head())

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

#correlation matrix
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

#price vs neighbourhood group
neighbourhood_prices = df.groupby('neighbourhood_group')['price'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=neighbourhood_prices, x='neighbourhood_group', y='price', hue='neighbourhood_group', palette='viridis', legend=False)
plt.title('Average price per neighbourhood group')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Prices')
plt.show()

# Availability distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['availability_365'], bins=30, kde=True)
plt.title('Availability Distribution')
plt.xlabel('No of days available')
plt.ylabel('Frequency')
plt.show()

#Reviews per month vs no of reviews
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='number_of_reviews', y='reviews_per_month', alpha=0.5)
plt.title('Reviews per month VS No of reviews')
plt.xlabel('Number_of_reviews')
plt.ylabel('Reviews per month')
plt.show()

# Boxplot of price by neighborhood group
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='neighbourhood_group', y='price')
plt.ylim(0, 500)
plt.title('Price Distribution by Neighborhood Group')
plt.xlabel('Neighborhood Group')
plt.ylabel('Price')
plt.show()

# Average availability per neighborhood group
neighborhood_availability = df.groupby('neighbourhood_group')['availability_365'].mean().reset_index()
# Bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=neighborhood_availability, x='neighbourhood_group', y='availability_365', palette='magma')
plt.title('Average Availability per Neighborhood Group')
plt.xlabel('Neighborhood Group')
plt.ylabel('Average Availability (days)')
plt.show()

# Advanced Analysis
# Reviews over time
df.set_index('last_review', inplace=True)
monthly_reviews = df['reviews_per_month'].resample('ME').sum()

plt.figure(figsize=(12, 6))
monthly_reviews.plot(color='purple')
plt.title('Total Reviews per Month Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Reviews')
plt.show()

# Price distribution by room type
plt.figure(figsize=(10, 6))
sns.boxplot(data=df.reset_index(), x='room_type', y='price')
plt.ylim(0, 500)
plt.title('Price Distribution by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Price')
plt.show()

print("\nKey Insights:")
print("1. Most listings are concentrated in Manhattan and Brooklyn.")
print("2. Prices tend to be higher in Manhattan, with a wider spread in luxury listings.")
print("3. Review activity has seasonal trends — consider these patterns for pricing strategies.")
print("4. Private rooms and shared rooms are generally more affordable than entire homes/apartments.")

print("\nAnalysis Completed!!")