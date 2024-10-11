import pandas as pd

# 1-Load the dataset into a DataFrame
data = pd.read_csv('walmart_sales_dataset_of_45stores.csv')
print("Data Info: ")
print(data.info())
print('#########################################')
print('The 1st five rows')
print(data.head())
print('##########################################')

# 2-cleaning
print("Check null values :")
print(data.isnull().sum())
print('##########################################')
#if there are na values -> drop
cleaned_data = data.dropna()
print('Dublicated rows:')
print(cleaned_data.duplicated().sum())
#if there are duplicated -> remove
cleaned_data = cleaned_data.drop_duplicates()
print('##########################################')
print("Cleaned data\'Zero Null values and zero duplicated\'")
print(cleaned_data.info())
print('##########################################')

#######################################################

                #a-Find the store with maximum sales
# Calculate total sales for each store
store_sales = cleaned_data.groupby('Store')['Weekly_Sales'].sum()
max_sales_store = store_sales.idxmax()
max_sales_value = store_sales[max_sales_store]
print(f"The store with maximum sales is Store {max_sales_store} with total sales of ${max_sales_value:.2f}")
print('##########################################')
                #b-Calculate standard deviation of sales for each store
store_std = cleaned_data.groupby('Store')['Weekly_Sales'].std()
# the store with maximum standard deviation
max_std_store = store_std.idxmax()
max_std_value = store_std[max_std_store]
print(f"The store with maximum standard deviation is Store {max_std_store} with a standard deviation of ${max_std_value:.2f}")

                #C- the mean sales for non-holiday weeks
mean_non_holiday_sales = cleaned_data[cleaned_data['Holiday_Flag'] == 0]['Weekly_Sales'].mean()
# holidays with sales higher than mean non-holiday sales
higher_sales_holidays = cleaned_data[(cleaned_data['Holiday_Flag'] == 1) & (cleaned_data['Weekly_Sales'] > mean_non_holiday_sales)]
print('Mean of non holiday sales ',mean_non_holiday_sales)
print("Holidays with higher sales than mean non-holiday sales:")
print(higher_sales_holidays[['Date', 'Weekly_Sales']])
print('##########################################')

                #D-a monthly and semester view of sales in units and give insights.
# Set the float format to display numbers in millions with commas
pd.options.display.float_format = '{:,.0f}'.format

# Convert Date column to datetime format if it's not already in datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

# Filter data for the specific date range
start_date = '2010-02-05'
end_date = '2012-10-26'
filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

# Extract year, month, and semester information
filtered_data['Year'] = filtered_data['Date'].dt.year
filtered_data['Month'] = filtered_data['Date'].dt.month
filtered_data['Semester'] = filtered_data['Month'].apply(lambda x: 'First' if x <= 6 else 'Second')

# Calculate monthly sales for each year
monthly_sales_by_year = filtered_data.groupby(['Year', 'Month'])['Weekly_Sales'].sum()

# Calculate semester sales for each year
semester_sales_by_year = filtered_data.groupby(['Year', 'Semester'])['Weekly_Sales'].sum()

# Print insights
print("Monthly Sales by Year:")
print(monthly_sales_by_year)
print(" ")
print("In 2010, sales were highest in December (288,760,533) and were generally high throughout the year.")
print("In 2011, sales were highest in December (288,078,102)")
print("In 2012, sales were highest in June ( 240,610,329)")
print('##########################################')
print("\nSemester Sales by Year:")
print(semester_sales_by_year)
print(" ")
print("In 2010, the first semester (First) had lower sales (982,622,260) compared to the second semester (Second) which had significantly higher sales (1,306,263,860).")
print("In 2011, both semesters had similar high sales figures, with the second (1,320,860,210)semester slightly higher than the first(1,127,339,797).")
print("In 2012, the first semester had higher sales (1,210,765,416) compared to the second semester (789,367,443).")

