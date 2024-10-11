import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


data = pd.read_csv('walmart_sales_dataset_of_45stores.csv')
# Visualize distribution of Weekly_Sales
plt.figure(figsize=(10, 6))
sns.histplot(data['Weekly_Sales'], bins=30, kde=True)
plt.title('Distribution of Weekly Sales')
plt.xlabel('Weekly Sales')
plt.ylabel('Frequency')

#1-Visualize relationship between Temperature and Weekly_Sales
lowess = sm.nonparametric.lowess#estimating relationships between variables in a dataset
smoothed = lowess(data['Weekly_Sales'], data['Temperature'], frac=0.3)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Temperature', y='Weekly_Sales', data=data)
plt.plot(smoothed[:, 0], smoothed[:, 1], color='red', label='Loess Curve')
plt.title('Relationship between Temperature and Weekly Sales with Loess Curve')
plt.xlabel('Temperature')
plt.ylabel('Weekly Sales')
plt.legend()
#2-Visualize relationship between CPI and Weekly_Sales
lowess = sm.nonparametric.lowess
smoothed = lowess(data['Weekly_Sales'], data['CPI'], frac=0.3)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='CPI', y='Weekly_Sales', data=data)
plt.plot(smoothed[:, 0], smoothed[:, 1], color='red', label='Loess Curve')
plt.title('Relationship between CPI and Weekly Sales with Loess Curve')
plt.xlabel('CPI')
plt.ylabel('Weekly Sales')
plt.legend()
#3-Visualize relationship between Fuel_Price and Weekly_Sales
lowess = sm.nonparametric.lowess
smoothed = lowess(data['Weekly_Sales'], data['Fuel_Price'], frac=0.3)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Fuel_Price', y='Weekly_Sales', data=data)
plt.plot(smoothed[:, 0], smoothed[:, 1], color='red', label='Loess Curve')
plt.title('Relationship between Fuel_Price and Weekly Sales with Loess Curve')
plt.xlabel('Fuel_Price')
plt.ylabel('Weekly Sales')
plt.legend()
#4-Visualize relationship between Unemployment and Weekly_Sales
lowess = sm.nonparametric.lowess
smoothed = lowess(data['Weekly_Sales'], data['Unemployment'], frac=0.3)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Unemployment', y='Weekly_Sales', data=data)
plt.plot(smoothed[:, 0], smoothed[:, 1], color='red', label='Loess Curve')
plt.title('Relationship between Unemployment and Weekly Sales with Loess Curve')
plt.xlabel('Unemployment')
plt.ylabel('Weekly Sales')
plt.legend()

#5-Analyze the impact of holiday weeks on Weekly_Sales
holiday_sales = data[data['Holiday_Flag'] == 1]['Weekly_Sales']
non_holiday_sales = data[data['Holiday_Flag'] == 0]['Weekly_Sales']
# Compare sales during holiday weeks vs. non-holiday weeks
plt.figure(figsize=(10, 6))
sns.boxplot(x='Holiday_Flag', y='Weekly_Sales', data=data)
plt.title('Comparison of Weekly Sales during Holiday and Non-Holiday Weeks')
plt.xlabel('Holiday Flag')
plt.ylabel('Weekly Sales')
plt.xticks([0, 1], ['Non-Holiday', 'Holiday'])

#6-Create a pie plot
# Count the number of holiday weeks and non-holiday weeks
holiday_count = data['Holiday_Flag'].sum()
non_holiday_count = len(data) - holiday_count
labels = ['Holiday', 'Non-Holiday']
sizes = [holiday_count, non_holiday_count]
colors = ['#ff9999', '#66b3ff']  # Red for holiday, blue for non-holiday
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Comparison of Holiday Weeks and Non-Holiday Weeks')
plt.axis('equal')

plt.show()
print('##########################################')



