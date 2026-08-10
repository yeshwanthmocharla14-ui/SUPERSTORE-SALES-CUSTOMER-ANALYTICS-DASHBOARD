"""
Superstore Sales & Customer Analytics - Data Cleaning + EDA
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# ---------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------
df = pd.read_csv("../data/superstore_raw.csv")
print("Initial shape:", df.shape)
print("\nMissing values per column:\n", df.isnull().sum())

# ---------------------------------------------------------------
# 2. Data cleaning
# ---------------------------------------------------------------
df["Region"] = df["Region"].astype(str).str.strip().str.title()
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"], errors="coerce")

missing_pct = df.isnull().mean().mean() * 100
print(f"\nAvg missing % across columns before fix: {missing_pct:.1f}%")

df["Sub_Category"] = df["Sub_Category"].fillna("Unknown")
df["Discount"] = df["Discount"].fillna(df["Discount"].median())
df = df.dropna(subset=["Ship_Date"])
df = df.drop_duplicates()

df["Order_Month"] = df["Order_Date"].dt.to_period("M").astype(str)

df.to_csv("../data/superstore_clean.csv", index=False)
print("\nCleaned shape:", df.shape)

# ---------------------------------------------------------------
# 3. Region revenue share
# ---------------------------------------------------------------
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
region_share = (region_sales / region_sales.sum() * 100).round(1)
print("\nRevenue share by region (%):\n", region_share)

plt.figure(figsize=(7, 5))
colors = ["#1F3864" if r == region_share.idxmax() else "#9DB4CE" for r in region_share.index]
region_share.plot(kind="bar", color=colors)
plt.title("Revenue Share by Region (%)")
plt.ylabel("% of Total Sales")
plt.xlabel("Region")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../screenshots/region_revenue_share.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 4. Discount vs Profit
# ---------------------------------------------------------------
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df.sample(3000, random_state=1), x="Discount", y="Profit",
                 alpha=0.4, color="#1F3864")
plt.axhline(0, color="red", linestyle="--", linewidth=1)
plt.title("Discount vs Profit")
plt.tight_layout()
plt.savefig("../screenshots/discount_vs_profit.png", dpi=150)
plt.close()

corr = df[["Discount", "Profit"]].corr().iloc[0, 1]
print(f"\nCorrelation between Discount and Profit: {corr:.2f}")

# ---------------------------------------------------------------
# 5. Monthly sales trend
# ---------------------------------------------------------------
monthly_sales = df.groupby("Order_Month")["Sales"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(marker="o", color="#1F3864")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=60)
plt.tight_layout()
plt.savefig("../screenshots/monthly_sales_trend.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 6. Category profit
# ---------------------------------------------------------------
cat_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by category:\n", cat_profit)

plt.figure(figsize=(7, 5))
cat_profit.plot(kind="bar", color="#3B6EA5")
plt.title("Total Profit by Category")
plt.ylabel("Profit ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../screenshots/profit_by_category.png", dpi=150)
plt.close()

# ---------------------------------------------------------------
# 7. Discount impact on margin -> business recommendation check
# ---------------------------------------------------------------
high_discount = df[df["Discount"] >= 0.3]
low_discount = df[df["Discount"] < 0.3]
margin_high = high_discount["Profit"].sum() / high_discount["Sales"].sum() * 100
margin_low = low_discount["Profit"].sum() / low_discount["Sales"].sum() * 100
print(f"\nMargin at discount >=30%: {margin_high:.1f}%")
print(f"Margin at discount <30%:  {margin_low:.1f}%")
print(f"Potential margin recovery if high-discount orders reduced: {margin_low - margin_high:.1f} pts")

print("\nDone. Charts saved to ../screenshots/")
