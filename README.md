# JDC Sales & Inventory Forecasting – MSBA Capstone Project

## **Project Overview**
This capstone project for the University of Montana's Master of Science in Business Analytics (MSBA) program focuses on **sales and inventory forecasting** for **Jewelry Design Center (JDC)**. JDC operates multiple locations and specializes in custom jewelry design, retail sales, and repair services. 

The goal of this project is to develop **data-driven insights and predictive models** that support inventory planning and sales forecasting, helping JDC optimize inventory management and strategic decision-making.

**Status**: Finalized for submission – May 2025

---

## **Repository Structure**
```
msba_capstone/
│── data/           # Placeholder for raw and processed data (not included)
│── docs/           # Supporting documentation (e.g., final written report, requirements, methodology)
│── images/         # Visuals used in notebooks and reports
│── notebooks/      # Jupyter notebooks for analysis and modeling
│── src/            # Python scripts for data processing and forecasting
│── .gitignore      # Ensures sensitive files are excluded
│── README.md       # Project overview and setup guide
```

---

## **Objectives**
- Clean, organize, and analyze **sales and inventory data from 2020–2024**
- Focus exclusively on **retail sales**, excluding custom orders and repairs
- Use **Google BigQuery (GBQ)** for data storage and querying
- Use **Python** (in VS Code) for forecasting, analysis, and visualization
- Build and compare **time series forecasting models** to predict future inventory needs
- Deliver **strategic insights and recommendations** to reduce stock-outs and overstocking

---

## **Data Sources**
### **1. Sales Data (2020–2024)**
- Transaction-level retail sales across all JDC locations
- Provided as CSV files; cleaned for consistency in Excel
- Uploaded to Google BigQuery for structured querying

### **2. Inventory Data**
- Extracted from JDC’s POS system (**The Edge**)
- Includes product details, stock levels, entry dates, and categories
- Used to calculate inventory turnover, aging, and margin metrics

---

## **Methodology & Data Processing**
### **1. Data Cleaning & Preparation**
- Ensured consistent **unique identifiers** for merging datasets
- Standardized **date formats, labels, and measurement units**
- Cleaned preliminary data in **Excel**, then imported into **BigQuery**

### **2. Google BigQuery for Data Storage & SQL Analysis**
- Created datasets and tables in the `capstone-project-2025.jdc_data` namespace
- Used SQL to conduct **Exploratory Data Analysis (EDA)**:
  - Sales and profit trends by time and category
  - Inventory movement and product aging
  - Retail revenue concentration (e.g., 80/20 rule)

### **3. Filtering for Core Retail Focus**
- Excluded **non-retail transactions** such as repairs and custom jobs
- Retained categories that align with **core retail inventory**
- Worked closely with JDC stakeholders to ensure business relevance

### **4. Python Forecasting & Visualization**
- Connected BigQuery to Python for model development
- Created visualizations using **Matplotlib** and **Seaborn**
- Applied two different forecasting techniques:
  - **ARIMA**
  - **Prophet**
- Forecasts were generated at both **aggregate** and **category levels**

---

## **Model Evaluation**
- Evaluated models using **MAPE** and **RMSE**
- **Prophet** delivered the best performance for most both single category and aggregated top 12 categories compared to **SARIMA** 
- Model selection was based on **accuracy, interpretability, and alignment with JDC's planning needs**

---

## **Strategic Recommendations**
- Focus inventory planning around the **top 12 categories**, which account for ~80% of retail revenue
- Prepare for **seasonal surges** (especially in Q4) with targeted inventory boosts
- **Reduce aged stock** by identifying slow-moving SKUs
- Continue to **leverage forecasting tools** to adjust purchase timing and quantities

---

## **Final Deliverables**
- Final written report and presentation (see `reports/` folder)
- Forecasts for 2025–2026 retail inventory needs by top 12 categories
- Visual analysis of historical sales and inventory patterns
- Jupyter notebooks detailing full modeling workflow
- Strategic insights for JDC’s executive and operations teams
- *(Interactive Looker Studio dashboard available upon request)*

---

## **Setup Instructions (optional)**

To run the notebooks or scripts locally:
1. Clone the repository
2. Install dependencies with `pip install -r requirements.txt`
3. ### Python Version
This project was developed using **Python 3.11.8**. It is recommended to use this version (or higher within the 3.11.x series) for full compatibility.
4. Set up Google Cloud authentication if accessing BigQuery


> *Note: Raw data files are not included in this repo due to privacy/confidentiality agreements.*
