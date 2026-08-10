# 📊 Sales & Customer Analytics Project

## 📌 Project Overview

An end-to-end Data Analytics project analyzing retail sales and customer behavior using SQL, Python, and Power BI. The project identifies business insights from historical sales data — sales performance, customer purchasing behavior, profitability trends, regional performance, and the impact of discounts on profit margins — and turns them into actionable recommendations.

## 🎯 Project Objectives

- Analyze sales and profit trends across regions and categories
- Identify top-performing customers and products
- Understand the relationship between discounts and profitability
- Build an interactive dashboard for business stakeholders
- Generate actionable business insights from data

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| 🗄️ SQL (MySQL) | Data querying and business analysis |
| 🐍 Python | Data cleaning and exploratory data analysis |
| 🐼 Pandas / NumPy | Data manipulation and numerical computation |
| 📈 Matplotlib / Seaborn | Data visualization |
| 📊 Power BI | Interactive dashboard |
| 📑 Jupyter Notebook | Interactive analysis environment |

## 📂 Dataset Information

**Source:** Synthetic dataset generated to mirror the structure and scale of the public Superstore retail dataset (52,347 transaction records), since the original working files were lost. Generation logic is in [`python/generate_data.py`](python/generate_data.py) — fully reproducible.

Columns: Order ID, Order/Ship Date, Customer ID, Segment, Region, State, Category, Sub-Category, Sales, Quantity, Discount, Profit.

## 📌 Project Workflow

### 1. Data Collection
Synthetic dataset generated with `python/generate_data.py`, saved to `data/superstore_raw.csv`.

### 2. Data Cleaning & Preprocessing
- Checked missing/null values (~7.5% of records had missing or inconsistent fields)
- Standardized inconsistent region text (casing/whitespace)
- Parsed date columns to datetime, dropped unrecoverable rows, removed duplicates
- Full code: [`python/eda_analysis.py`](python/eda_analysis.py) / [`python/superstore_eda.ipynb`](python/superstore_eda.ipynb)

### 3. SQL Business Analysis
Full query set in [`sql/superstore_analysis.sql`](sql/superstore_analysis.sql), including:
- Revenue & profit by region (window functions for % share)
- Profit by category, loss-making sub-categories
- Monthly sales trend with month-over-month growth (`LAG`)
- Top 10 customers by revenue
- Segment-wise performance (CTEs)

### 4. Python EDA
Full notebook: [`python/superstore_eda.ipynb`](python/superstore_eda.ipynb)
- Region revenue share
- Discount vs profit correlation
- Monthly sales trend
- Profit by category

### 5. Power BI Dashboard
Interactive dashboard (`SUPERSTORE SALES & CUSTOMER ANALYTICS DASHBOARD.pbix`) with KPI cards (Total Sales, Profit, Orders, Customers), regional/category charts, and slicers for Region, Category, Segment, and Ship Mode.

## 📈 Dashboard Preview

![Dashboard](SUPERSTORE%20SALES%20%26%20CUSTOMER%20ANALYTICS%20DASHBOARD.png)

## 📊 Key Business Insights

**Sales**
- South region drives the largest share of total revenue (~36%)
- Technology is the highest-profit category

![Region Revenue Share](screenshots/region_revenue_share.png)

**Profitability**
- Discount and profit are negatively correlated (r ≈ -0.48); orders discounted 30%+ run at a loss on average

![Discount vs Profit](screenshots/discount_vs_profit.png)

**Trend**
![Monthly Sales Trend](screenshots/monthly_sales_trend.png)

**Recommendation:** Reducing deep discounting (30%+) on low-margin sub-categories is the clearest lever to recover profit margin.

## 📁 Project Structure

```
proj1_superstore/
├── data/
│   ├── superstore_raw.csv
│   └── superstore_clean.csv
├── sql/
│   └── superstore_analysis.sql
├── python/
│   ├── generate_data.py
│   ├── eda_analysis.py
│   └── superstore_eda.ipynb
├── screenshots/
├── requirements.txt
└── README.md
```

## 🚀 Skills Demonstrated

SQL querying (joins, window functions, CTEs) · data cleaning · exploratory data analysis · dashboard development · data visualization · business storytelling

## 🔮 Future Improvements

- Sales forecasting model
- ML-based customer segmentation
- Online-hosted dashboard, real-time data integration

## 👨‍💻 Author

**Yeshwanth Mocherla** — Aspiring Data Analyst | SQL | Python | Power BI
