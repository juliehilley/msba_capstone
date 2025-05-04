"""
JDC Sales Analysis Script

This script connects to Google BigQuery to extract sales and inventory data
from Jewelry Design Center (2020–2024) and generates visualizations to support
trend analysis, forecasting, and category-level performance insights.
"""

# Standard libraries
import os

# Third-party libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Google Cloud
from google.cloud import bigquery
from google.oauth2 import service_account

# --------------------------
# Setup BigQuery Connection
# --------------------------
project_id = "capstone-project-2025-449217"
key_path = (
    "/Users/juliehilley/Desktop/__Capstone & Prep/"
    "capstone-project-2025-449217-f9f34f80492d.json"
)
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project=project_id)

# Confirm connection
dataset_id = "jdc_data"
tables = client.list_tables(dataset_id)
print(f"Tables in dataset '{dataset_id}':")
for table in tables:
    print(f" - {table.table_id}")

# ----------------------------
# Helper Functions
# ----------------------------
def run_query(query: str) -> pd.DataFrame:
    """Execute a BigQuery SQL query and return the result as a DataFrame."""
    return client.query(query).to_dataframe()

def plot_line(df, x_col, y_col, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    plt.plot(df[x_col], df[y_col], marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_barh(df, x_col, y_col, title, xlabel):
    plt.figure(figsize=(10, 6))
    plt.barh(df[x_col], df[y_col], color="royalblue")
    plt.xlabel(xlabel)
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

# --------------------------
# Monthly Sales Trend
# --------------------------
table_name = f"{project_id}.{dataset_id}.filtered_retail_sales"
query = f"""
SELECT 
    FORMAT_DATE('%Y-%m', sold_date) AS year_month,
    ROUND(SUM(sale_total), 2) AS total_sales
FROM `{table_name}`
WHERE sold_date IS NOT NULL
GROUP BY year_month
ORDER BY year_month
"""
df = run_query(query)
if not df.empty:
    plot_line(df, 'year_month', 'total_sales', 'Monthly Sales Trends', 'Month', 'Total Sales (USD)')
else:
    print("No data found for the query.")

# --------------------------
# Average Sales by Weekday
# --------------------------
query = f"""
SELECT 
    dayofweek,  
    ROUND(AVG(sale_total), 2) AS average_sales
FROM `{table_name}`
WHERE EXTRACT(YEAR FROM sold_date) BETWEEN 2018 AND 2022
    AND dayofweek != 'Sunday'
GROUP BY dayofweek
ORDER BY 
    CASE 
        WHEN dayofweek = 'Monday' THEN 1
        WHEN dayofweek = 'Tuesday' THEN 2
        WHEN dayofweek = 'Wednesday' THEN 3
        WHEN dayofweek = 'Thursday' THEN 4
        WHEN dayofweek = 'Friday' THEN 5
        WHEN dayofweek = 'Saturday' THEN 6
    END;
"""
df_weekday = run_query(query)
plot_barh(df_weekday, "dayofweek", "average_sales", "Avg Sales by Day (Excl. Sunday)", "Avg Sales (USD)")

# --------------------------
# Average Monthly Sales
# --------------------------
query = f"""
SELECT 
    EXTRACT(MONTH FROM sold_date) AS month,
    ROUND(AVG(sale_total), 2) AS avg_monthly_sales
FROM `{table_name}`
WHERE EXTRACT(YEAR FROM sold_date) BETWEEN 2020 AND 2024
GROUP BY month
ORDER BY month;
"""
df_monthly_sales = run_query(query)
month_labels = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
plt.figure(figsize=(12, 6))
plt.plot(df_monthly_sales["month"], df_monthly_sales["avg_monthly_sales"], marker="o", linestyle="-", color="royalblue")
plt.xticks(ticks=df_monthly_sales["month"], labels=month_labels, rotation=45)
plt.title("Average Monthly Sales (2020–2024)")
plt.xlabel("Month")
plt.ylabel("Avg Sales (USD)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

