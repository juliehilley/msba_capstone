# Initialize BigQuery
from google.cloud import bigquery
from google.oauth2 import service_account
import matplotlib.pyplot as plt
import pandas as pd
import textwrap
import seaborn as sns
import numpy as np
from tabulate import tabulate

# Set your project ID
project_id = "capstone-project-2025-449217"

# Path to service account key file
key_path = "/Users/juliehilley/Desktop/__Capstone & Prep/capstone-project-2025-449217-f9f34f80492d.json"

# Initialize the BigQuery client
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project=project_id)

# Confirm the connection by listing tables in the jdc_data dataset
dataset_id = "jdc_data"
tables = client.list_tables(dataset_id)
print(f"Tables in dataset '{dataset_id}':")
for table in tables:
    print(f" - {table.table_id}")

# Run the query and load into a DataFrame
query = """
    SELECT 
        SUM(cost) AS total_inventory_value,
        COUNT(sku) AS total_units_on_hand
    FROM `capstone-project-2025-449217.jdc_data.filtered_inventory`
    WHERE sold_status = 0;
"""
df_inventory = client.query(query).to_dataframe()

# Print summary statistics
print(df_inventory)

# Bar Chart for Total Inventory Value & Units on Hand
plt.figure(figsize=(8, 5))
plt.bar(["Total Inventory Value ($)", "Total Units On Hand"], 
        [df_inventory.loc[0, "total_inventory_value"], df_inventory.loc[0, "total_units_on_hand"]])
plt.ylabel("Value / Count")
plt.title("Total Inventory Overview")
plt.xticks(rotation=30)
plt.show()
