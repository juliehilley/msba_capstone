# msba_capstone

# JDC Sales & Inventory Forecasting
Project ID = capstone-project-2025
Dataset Name = jdc_data
Table Names = sales, inventory, doorcount, filtered_retail_sales 
GCS Bucket Name = capstone-dataset-files
GBQ Key ID = f9f34f80492d1db0796c859cbcc4b6f1104e1cd7
Path to Key = /Users/juliehilley/Desktop/__Capstone & Prep/capstone-project-2025-449217-f9f34f80492d.json

# Project Overview:
This capstone project for the University of Montana's MSBA program focuses on sales and inventory forecasting for Jewelry Design Center (JDC). JDC operates multiple locations and specializes in custom jewelry design, retail sales, and repair services. This project aims to develop data-driven insights and predictive models that support inventory planning and sales forecasting.


# Objectives
 - Clean, organize, and analyze sales, inventory, and door count data from 2020-2024.
 - Focus on retail transactions and inventory that supports retail sales (excluding custom orders and repairs).
 - Use Google BigQuery (GBQ) for storage and querying, and Python (VS Code) for analysis and visualization.
 - Build a forecasting model to predict inventory needs based on sales trends.
 - Deliver insights to JDC to optimize inventory management and improve business decision-making.

#  Data Sources
1. Sales Data (2020-2024)
    - Includes transaction-level sales for all JDC locations.
    - Originally provided as CSV files, cleaned in Excel for consistency.
    - UPloaded to Google BigQuery for storage and querying.

2. Inventory Data
    - Complete inventory dataset from JDC's current POS system (The Edge).
    - Includes product details, categories, stock levels, and transaction history.
    
3. Door Count Data
    - Tracks customer foot traffic at each JDC location.
    - Helps correlate sales with store visits for better forecasting.


# Methodology & Data Processing
1. Data Cleaning & Preparation
    - Ensured unique identifiers for consistent joins between sales and inventory data.
    - Standardized measurement unites, date formats, and categorical labels for consistency.
    - Used Excel for initial cleaning before moving to GBQ.

2. Data Storage & Exploration in GBQ
    - Created a Googld Cloud Storage bucket to upload cleaned CSV files.
    - Established tables in GBQ under the project "Capstone Project 2025"
    - Conducted exploratory data analysis (EDA) sith SQL queries to understand:
        Sales trends over time.
        Inventory movement by category
        Fooot traffic correlations with sales.
        Profit margin for inventory categories.

3. Defining the Scope: Filtering Sales & Inventory Data
    - Excluded custom orders, reparis, and services to focus solely on retail sales.
    - Defined a subset of inventory categories that align with retail transactions.
    - Collaborated with JDC stakeholders to refine the project scope.

4. Data Visualization in Python (VS Code)
    - Connected to GBQ from Python to pull filtered retail sales data.
    - Created initial visualizations to identify patterns and trends.
    - Next steps: More advanced EDA and forecasting model developmenmt.
