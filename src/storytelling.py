# Import necessary libraries
from google.cloud import bigquery
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set up Google BigQuery connection
project_id = "capstone-project-2025-449217"
dataset_id = "jdc_data"
table_name = f"{project_id}.{dataset_id}.sales"

# Initialize BigQuery client
client = bigquery.Client(project=project_id)

# SQL Query to get revenue breakdown
query = f"""
SELECT 
    category,
    SUM(sale_total) AS total_revenue
FROM (
    SELECT 
        sale_total,
        CASE 
            WHEN trans_type IN ('Sale', 'Lay-PkUp', 'SO-PkUp') 
                 AND inv_type IN ('Stock', 'Special Order', 'Memo', 'Assembled', 'Built', 'Joined') THEN 'Retail Sales'
            WHEN trans_type IN ('Rep-PkUp', 'Quick Rep.') THEN 'Repairs'
            WHEN trans_type IN ('Custm-PkUp', 'Quick Custom', 'Custm-PostAdj')
                 OR inv_type = 'Custom' THEN 'Custom Orders'
            ELSE 'Other'
        END AS category
    FROM `{table_name}`
) grouped_data
WHERE category != 'Other'  -- Exclude 'Other' category
GROUP BY category
ORDER BY total_revenue DESC
"""

# Run the query
df = client.query(query).to_dataframe()

# Normalize revenue percentage
df["revenue_percentage"] = (df["total_revenue"] / df["total_revenue"].sum()) * 100

# Define colors
colors = ["#3498db", "#e74c3c", "#f1c40f"]  # Blue (Retail), Red (Repairs), Yellow (Custom)

# Create the pie chart
plt.figure(figsize=(8, 6))
plt.pie(
    df["revenue_percentage"],
    labels=df["category"],
    autopct="%1.1f%%",
    startangle=140,
    colors=colors,
    wedgeprops={"edgecolor": "black"}
)

# Add title
plt.title("Revenue Breakdown: Retail Sales vs. Repairs vs. Custom Orders", fontsize=14, fontweight="bold")

# Show the plot
plt.show()



# Run the query
df = client.query(query).to_dataframe()

# Normalize revenue percentage
df["revenue_percentage"] = (df["total_revenue"] / df["total_revenue"].sum()) * 100

# Create the bar chart
plt.figure(figsize=(8, 6))
sns.barplot(
    x=df["category"], 
    y=df["revenue_percentage"], 
    palette=colors
)

# Add labels and title
plt.ylabel("Revenue Percentage", fontsize=12)
plt.xlabel("Category", fontsize=12)
plt.title("Revenue Breakdown: Retail Sales vs. Repairs vs. Custom Orders", fontsize=14, fontweight="bold")

# Display percentage values on bars
for index, value in enumerate(df["revenue_percentage"]):
    plt.text(index, value + 1, f"{value:.1f}%", ha="center", fontsize=12)

# Show the plot
plt.ylim(0, max(df["revenue_percentage"]) + 5)
plt.show()



# SQL Query to get revenue breakdown for Retail Sales (Excluding Repairs & Custom)
query = f"""
SELECT 
    CASE 
        WHEN category_num = '190' THEN 'Loose Natural Diamonds'
        WHEN category_num = '195' THEN 'Lab Diamonds'
        ELSE 'Other Retail Sales'
    END AS category_group,
    SUM(sale_total) AS total_revenue
FROM `{table_name}`
WHERE trans_type IN ('Sale', 'Lay-PkUp', 'SO-PkUp')  -- Ensure only Retail Sales transactions
GROUP BY category_group
ORDER BY total_revenue DESC
"""

# Run the query
df = client.query(query).to_dataframe()

# Normalize revenue percentage
df["revenue_percentage"] = (df["total_revenue"] / df["total_revenue"].sum()) * 100

# Define colors
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]  # Blue (Other Retail), Orange (Loose Natural), Green (Lab Diamonds)

# Create the bar chart
plt.figure(figsize=(8, 6))
sns.barplot(
    x=df["category_group"], 
    y=df["revenue_percentage"], 
    palette=colors
)

# Add labels and title
plt.ylabel("Revenue Percentage", fontsize=12)
plt.xlabel("Category", fontsize=12)
plt.title("Retail Sales Breakdown: Loose Natural vs. Lab Diamonds vs. Other Retail", fontsize=14, fontweight="bold")

# Display percentage values on bars
for index, value in enumerate(df["revenue_percentage"]):
    plt.text(index, value + 1, f"{value:.1f}%", ha="center", fontsize=12)

# Show the plot
plt.ylim(0, max(df["revenue_percentage"]) + 5)
plt.show()