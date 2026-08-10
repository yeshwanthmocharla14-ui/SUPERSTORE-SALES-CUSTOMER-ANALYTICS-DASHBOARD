-- ================================================================
-- Superstore Sales & Customer Analytics - SQL Business Analysis
-- Database: MySQL
-- Table: superstore (created from superstore_clean.csv)
-- ================================================================

CREATE TABLE IF NOT EXISTS superstore (
    Order_ID        VARCHAR(20),
    Order_Date      DATE,
    Ship_Date       DATE,
    Customer_ID     VARCHAR(20),
    Segment         VARCHAR(30),
    Region          VARCHAR(20),
    State           VARCHAR(30),
    Category        VARCHAR(30),
    Sub_Category    VARCHAR(30),
    Sales           DECIMAL(10,2),
    Quantity        INT,
    Discount        DECIMAL(4,2),
    Profit          DECIMAL(10,2)
);

-- 1. Total sales & profit overview
SELECT
    COUNT(*)              AS total_orders,
    ROUND(SUM(Sales), 2)  AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS overall_margin_pct
FROM superstore;

-- 2. Revenue and % share by region (identifies South as top region)
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS region_sales,
    ROUND(SUM(Sales) * 100.0 / SUM(SUM(Sales)) OVER (), 1) AS pct_of_total_sales
FROM superstore
GROUP BY Region
ORDER BY region_sales DESC;

-- 3. Profit by category
SELECT
    Category,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(AVG(Profit), 2) AS avg_profit_per_order
FROM superstore
GROUP BY Category
ORDER BY total_profit DESC;

-- 4. Discount vs profitability (window function: running average discount by month)
SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS order_month,
    ROUND(AVG(Discount), 2) AS avg_discount,
    ROUND(AVG(Profit), 2) AS avg_profit,
    ROUND(
        AVG(AVG(Discount)) OVER (ORDER BY DATE_FORMAT(Order_Date, '%Y-%m')
                                  ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2
    ) AS rolling_3mo_avg_discount
FROM superstore
GROUP BY order_month
ORDER BY order_month;

-- 5. Top 10 customers by revenue
SELECT
    Customer_ID,
    ROUND(SUM(Sales), 2) AS total_spend,
    COUNT(DISTINCT Order_ID) AS total_orders
FROM superstore
GROUP BY Customer_ID
ORDER BY total_spend DESC
LIMIT 10;

-- 6. Loss-making sub-categories (high discount driving negative margin)
SELECT
    Sub_Category,
    ROUND(AVG(Discount), 2) AS avg_discount,
    ROUND(SUM(Profit), 2)   AS total_profit,
    COUNT(*)                AS orders_at_loss
FROM superstore
WHERE Profit < 0
GROUP BY Sub_Category
ORDER BY total_profit ASC;

-- 7. Monthly sales trend with month-over-month growth (window function: LAG)
SELECT
    order_month,
    monthly_sales,
    ROUND(
        (monthly_sales - LAG(monthly_sales) OVER (ORDER BY order_month))
        / LAG(monthly_sales) OVER (ORDER BY order_month) * 100, 1
    ) AS mom_growth_pct
FROM (
    SELECT DATE_FORMAT(Order_Date, '%Y-%m') AS order_month,
           SUM(Sales) AS monthly_sales
    FROM superstore
    GROUP BY order_month
) monthly
ORDER BY order_month;

-- 8. Segment-wise performance (joins-style comparison using CTE)
WITH segment_summary AS (
    SELECT Segment,
           SUM(Sales)   AS segment_sales,
           SUM(Profit)  AS segment_profit
    FROM superstore
    GROUP BY Segment
)
SELECT
    Segment,
    segment_sales,
    segment_profit,
    ROUND(segment_profit / segment_sales * 100, 2) AS margin_pct
FROM segment_summary
ORDER BY segment_sales DESC;
