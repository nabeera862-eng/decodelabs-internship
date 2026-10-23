# Project 2: Exploratory Data Analysis (EDA)

## Project Overview

This project performs Exploratory Data Analysis (EDA) on an e-commerce orders dataset containing 1200 rows and 14 columns. The analysis explores order values, sales trends, outliers, order statuses, and relationships between numerical variables.

## Objectives

- Understand the distribution of order values.
- Identify outliers using the IQR method.
- Analyze order status and monthly sales trends.
- Explore relationships between numerical variables.
- Extract useful business insights from the data.

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- Seaborn

## Key Findings

- The median order value was lower than the mean, indicating that a few large orders increased the average.
- Only 8 outliers were identified, and they appeared to be genuine high-value orders.
- Approximately 41.4% of orders were cancelled or returned.
- Monthly sales showed considerable variation, with 2023 having the highest average monthly sales.
- UnitPrice and Quantity had the strongest relationships with TotalPrice.

## Recommendations

- Investigate the reasons behind cancelled and returned orders.
- Use median order value alongside the mean for better reporting.
- Monitor high-value orders and monthly sales fluctuations.

## Project Files

- `DECODE_LABS_PROJECT2.py` — Python code for Exploratory Data Analysis.
- `EDA_Executive_Summary_Project2.pdf` — Detailed analysis, findings, recommendations, and     visualizations.
- `Cleaned_Dataset1.csv` — Cleaned dataset used for analysis.

## Conclusion

This project helped identify important patterns in e-commerce orders and provided insights into sales performance, order status, and customer purchasing behavior.