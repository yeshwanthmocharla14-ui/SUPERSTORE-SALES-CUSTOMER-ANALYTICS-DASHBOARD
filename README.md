# SUPERSTORE-SALES-CUSTOMER-ANALYTICS-DASHBOARD
# 📊 Sales & Customer Analytics Project

## 📌 Project Overview

This is an end-to-end Data Analytics project developed to analyze retail sales and customer behavior using SQL, Python, and Power BI. The project focuses on identifying meaningful business insights from historical sales data and transforming raw data into actionable recommendations through data analysis and visualization.

The project simulates a real-world business scenario where a company wants to understand its sales performance, customer purchasing behavior, profitability trends, regional performance, and the impact of discounts on profit margins.

Through this project, I performed data cleaning, SQL-based business analysis, exploratory data analysis (EDA) in Python, and created an interactive Power BI dashboard for business reporting and decision-making.

---

# 🎯 Project Objectives

The main objectives of this project are:

- Analyze sales and profit trends across different regions and categories
- Identify top-performing customers and products
- Understand the relationship between discounts and profitability
- Perform customer and sales analytics using SQL and Python
- Build an interactive dashboard for business stakeholders
- Generate actionable business insights from data

---

# 🛠️ Tool / Technology & 📌 Purpose |

🗄️ SQL (MySQL) - Data querying and business analysis 
🐍 Python - Data cleaning and exploratory data analysis
🐼 Pandas - Data manipulation and preprocessing 
🔢 NumPy - Numerical computations
📈 Matplotlib - Data visualization and chart creation 
🎨 Seaborn - Statistical data visualization
📊 Power BI - Interactive dashboard development
🌐 GitHub - Version control and project portfolio
💻 VS Code - Code editor for Python and SQL development
📑 Jupyter Notebook - Interactive Python analysis environment 

---

# 📂 Dataset Information

### Dataset Used: Superstore Sales Dataset

The dataset contains retail business transaction records including:

- Order details
- Customer information
- Product categories
- Sales and profit
- Discounts
- Shipping information
- Regional and state-level sales data

# 📌 Project Workflow

## 1️⃣ Data Collection

- Downloaded the Superstore retail dataset from Kaggle
- Imported the dataset into MySQL, Python, and Power BI

## 2️⃣ Data Cleaning & Preprocessing

Performed data cleaning operations to improve data quality:

- Checked missing/null values
- Removed duplicate records
- Verified column data types
- Converted date columns into proper datetime format
- Created Month-Year columns for trend analysis

### Python Operations Performed

python
df.isnull().sum()
df.duplicated().sum()
df['Order Date'] = pd.to_datetime(df['Order Date'])

📌 SQL Analysis

Performed SQL-based business analysis using MySQL.

Key SQL Operations
Aggregate functions
GROUP BY analysis
Sorting and filtering
Customer analysis
Profitability analysis
Trend analysis

🔍 Business Questions Solved Using SQL

Sales Analysis
What is the total sales revenue?
Which region generated the highest sales?
Which categories contributed the highest profit?
Customer Analysis
Who are the top 10 customers?
Which customers contribute the highest revenue?
Product Analysis
Which products are loss-making?
Which sub-categories are most profitable?
Trend Analysis
What are the monthly sales trends?
Which months recorded peak sales?

📌 Sample SQL Query

SELECT Category,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;

🐍 Python Exploratory Data Analysis (EDA)

Performed Exploratory Data Analysis using Python libraries such as Pandas, Matplotlib, and Seaborn.

📊 Analysis Performed

Sales Trend Analysis
Monthly sales growth
Seasonal sales patterns
Profitability Analysis
Profit by category
Profit vs Discount analysis
Customer Behavior Analysis
Top spending customers
Repeat customer trends
Correlation Analysis
Relationship between sales, profit, and discounts

📌 Sample Python Code
monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

📈 Power BI Dashboard

Developed a professional and interactive Power BI dashboard to visualize sales and customer analytics.

Dashboard Features
KPI Cards
Total Sales
Total Profit
Total Orders
Total Customers
Charts & Visualizations
Monthly Sales Trend
Sales by Region
Profit by Category
Top 10 Customers
Profit vs Discount Scatter Plot
Interactive Filters/Slicers
Region
Category
Segment
Ship Mode

📌 Dashboard Preview

Main Dashboard

(Add dashboard screenshot here)

📊 Key Business Insights

The following insights were identified through the analysis:

📌 Sales Insights

Technology category generated the highest sales revenue.
West region contributed the highest overall sales.

📌 Profitability Insights

High discounts significantly reduced profit margins.
Some products generated high sales but resulted in negative profits.

📌 Customer Insights

A small group of customers contributed a major portion of total revenue.
Corporate and Consumer segments generated the highest sales.
📌 Business Recommendations
Reduce excessive discounting on low-margin products.
Focus marketing efforts on high-value customers.
Improve profitability in underperforming regions.

📁 Project Structure

Sales_Customer_Analytics_Project/
│
├── data/
├── sql/
├── python/
├── dashboard/
├── reports/
├── screenshots/
└── README.md

🚀 Skills Demonstrated

This project demonstrates practical skills in:

SQL querying
Data cleaning
Exploratory Data Analysis
Business analytics
Dashboard development
Data visualization
Business storytelling
Problem-solving

📌 Learning Outcomes

Through this project, I gained hands-on experience in:

End-to-end Data Analytics workflow
SQL business analysis
Python-based EDA
Building Power BI dashboards
Generating business insights from raw data
Presenting analytical findings effectively
📷 Screenshots

(Add screenshots of:
Power BI Dashboard
SQL Queries
Python Charts)

🔮 Future Improvements

Possible future enhancements:

Add forecasting models
Build customer segmentation using machine learning
Deploy dashboard online
Integrate real-time sales data
Add predictive analytics features

📌 Conclusion

This project successfully demonstrates the complete lifecycle of a Data Analytics project starting from raw data processing to dashboard reporting and business insight generation.

The project helped strengthen technical and analytical skills in SQL, Python, and Power BI while also improving business understanding and storytelling abilities.
