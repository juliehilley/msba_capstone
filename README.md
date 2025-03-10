# JDC Sales & Inventory Forecasting – MSBA Capstone Project

## **Project Overview**
This capstone project for the University of Montana's MSBA program focuses on **sales and inventory forecasting** for **Jewelry Design Center (JDC)**. JDC operates multiple locations and specializes in custom jewelry design, retail sales, and repair services. 

The goal of this project is to develop **data-driven insights and predictive models** that support inventory planning and sales forecasting, helping JDC optimize its inventory management and business decision-making.

---

## **Repository Structure**
📂 capstone-project-2025 │── 📂 data/ # Placeholder for data files (data not included in repo) │── 📂 notebooks/ # Jupyter notebooks for analysis and modeling │── 📂 src/ # Python scripts for data processing, modeling, and visualization │── 📂 reports/ # Project documentation and final report │── 📂 docs/ # Supporting documentation (e.g., methodology, data dictionary) │── .gitignore # Ensures sensitive files are excluded │── requirements.txt # Dependencies for running the project │── README.md # Project overview and setup guide

---

## **Objectives**
- Clean, organize, and analyze **sales, inventory, and door count data (2020-2024).**
- Focus on **retail transactions and inventory** that supports retail sales (**excluding custom orders and repairs**).
- Use **Google BigQuery (GBQ)** for storage and querying, and **Python (VS Code)** for analysis and visualization.
- Build a **forecasting model** to predict inventory needs based on **historical sales trends.**
- Deliver **insights and recommendations** to JDC to optimize inventory management and **reduce stock-outs or overstocking.**

---

## **Data Sources**
### **1. Sales Data (2020-2024)**
- **Transaction-level** sales for all JDC locations.
- Originally provided as **CSV files**, **cleaned in Excel** for consistency.
- **Uploaded to Google BigQuery** for structured analysis.

### **2. Inventory Data**
- Extracted from **JDC's current POS system (The Edge).**
- Includes **product details, categories, stock levels, and transaction history.**
- Used to track **inventory turnover rates** and **aging stock.**

### **3. Door Count Data**
- Tracks **customer foot traffic** at each JDC location.
- Helps **correlate foot traffic with sales trends** for better demand forecasting.

---

## **Methodology & Data Processing**
### **1. Data Cleaning & Preparation**
- Ensured **unique identifiers** for consistent joins between sales and inventory.
- Standardized **measurement units, date formats, and categorical labels.**
- Used **Excel** for preliminary cleaning before importing into **Google BigQuery.**

### **2. Data Storage & Exploration in Google BigQuery**
- Created a **Google Cloud Storage (GCS) bucket** for data uploads.
- Established **BigQuery tables** under the project `"capstone-project-2025.jdc_data"`.
- Conducted **Exploratory Data Analysis (EDA)** using SQL to analyze:
  - **Sales trends** over time.
  - **Inventory movement** by category.
  - **Foot traffic correlations** with sales.
  - **Profit margins** across different product types.

### **3. Data Filtering: Sales & Inventory Focus**
- **Excluded** non-retail transactions (**custom orders, repairs, services**).
- Defined a **subset of inventory categories** that align with retail sales.
- Worked with **JDC stakeholders** to refine the **scope of analysis.**

### **4. Data Visualization & Forecasting in Python**
- Connected **BigQuery to Python** for analysis and forecasting.
- Created **visualizations** in Matplotlib and Seaborn to identify trends.
- Built **time series models** to predict inventory needs, including:
  - **Autoregressive (AR) models**
  - **ARIMA forecasting**
  - **Prophet models**
  - **Machine Learning-based forecasting (e.g., XGBoost, Random Forest)**
- Next steps: Model evaluation and **final recommendations for JDC.**

---

## **Setup Instructions**
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/msba_capstone.git


## Setup Instructions
_To be added: Instructions for setting up Python environment and accessing Google BigQuery._

## License
_License details to be determined._
