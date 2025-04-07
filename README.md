Monthly Sales Analyser

This project generates and analyzes simulated sales data for a month. It includes data generation, summary statistics, and visualizations to provide insights into daily and product-wise performance.

Features

Generate realistic sales data for multiple products over a month

Analyze total units sold, average prices, and revenue per product

Identify top-performing days and products

Visualize:

Daily total revenue (bar chart)

Product-wise revenue share (pie chart)


Export analysis charts as PNG files


File Structure

1. monthly_sales_summary.py

Generates the sales data and provides basic summaries.

Key Functions:

create_csv(): Creates a CSV file (sales_summary.csv) with random sales data for 30 days.

read_data(): Reads the CSV, calculates and prints:

Total units sold per product

Average unit price

Total revenue per product

Best selling product and highest revenue generator



2. sales_analyzer.py

Performs deeper analysis and creates visualizations.

Key Functions:

read_csv(): Reads the sales data, calculates daily and product-wise revenue, identifies:

Day with highest revenue

Product with least revenue


visualise():

Plots a bar chart of daily total revenue

Plots a pie chart of product-wise revenue share

Saves both charts as images



Requirements

Install the required libraries with:

pip install pandas matplotlib

How to Run

Run the main analysis script:

python sales_analyzer.py

This will:

Generate a fresh sales_summary.csv

Perform data analysis

Display and save visualizations


Output Files

sales_summary.csv: Simulated sales data

daily_revenue_bar_chart.png: Bar chart of daily revenues

product_wise_revenue_pie_chart.png: Pie chart of product-wise revenue share.