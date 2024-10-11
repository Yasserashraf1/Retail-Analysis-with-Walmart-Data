# Retail-Analysis-with-Walmart-Data
## Overview
This project analyzes sales data from Walmart, focusing on the impact of holidays, temperature, fuel prices, unemployment, and other factors on weekly sales. The dataset contains information from 45 Walmart stores, covering sales from 2010-02-05 to 2012-11-01. The goal of this project is to perform exploratory data analysis, answer key business questions, and create visualizations to provide insights into sales trends.

## Dataset Description
The dataset includes the following fields:
* Store: Store number.
* Date: Week of sales.
* Weekly_Sales: Sales for the given store.
* Holiday_Flag: Whether the week includes a holiday (1 = Holiday week, 0 = Non-holiday week).
* Temperature: Temperature on the day of sale.
* Fuel_Price: Cost of fuel in the region.
* CPI: Consumer Price Index.
* Unemployment: Unemployment rate.

## Project Tasks
* **Exploratory Data Analysis:**
  * Import and display data.
  * Visualize the distribution of quantitative variables.
  * Clean the data by handling missing and duplicated values.
* **Business Questions Answered:**
  * Identify the store with the highest total sales.
  * Find the store with the highest sales variability (standard deviation).
  * Determine holidays that result in higher sales compared to non-holiday periods.
  * Provide monthly and semester-level insights into sales trends.
  * Analyze the relationship between weekly sales and other numerical features (temperature, fuel price, CPI, unemployment).
* **Visualizations:**
  * Histograms of sales.
  * Loess curves for relationships between weekly sales and temperature, fuel price, CPI, and unemployment.
  * Boxplots comparing holiday vs non-holiday sales.
  * Pie chart showing the proportion of holiday vs non-holiday weeks.
* **Interactive Dashboard:**
  * Developed using Dash and Plotly.
  * Users can select variables for X and Y axes to explore relationships between features.

## Installation
* To run the project locally, you need the following Python libraries:
  * pandas
  * matplotlib
  * seaborn
  * statsmodels
  * dash
  * plotly
* You can install them using the following command:
_pip install pandas matplotlib seaborn statsmodels dash plotly_

## Usage
* Clone the repository:
_git clone https://github.com/your-username/walmart-retail-analysis.git_
* Navigate to the project directory:
_cd walmart-retail-analysis_
* Run the analysis script:
_python analysis.py_
* Start the Dash dashboard:
_python dashboard.py_

Author
Yasser Ashraf Mohammed Gaber
[LinkedIn]([https://www.linkedin.com/in/yasserashraf/]) | [GitHub]([url](https://www.linkedin.com/in/yasserashraf/))

