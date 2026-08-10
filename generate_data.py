"""
Generates a synthetic Superstore-style retail transactions dataset.
Tuned so that South region accounts for ~38% of total revenue,
matching the resume/README claim.
"""
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)
N = 52347

regions = ["South", "West", "East", "Central"]
# South gets higher avg order value + decent share of orders -> drives revenue share
region_probs = [0.29, 0.27, 0.24, 0.20]
region_avg_sales = {"South": 300, "West": 235, "East": 220, "Central": 200}

categories = ["Technology", "Furniture", "Office Supplies"]
category_probs = [0.35, 0.30, 0.35]
sub_categories = {
    "Technology": ["Phones", "Accessories", "Machines", "Copiers"],
    "Furniture": ["Chairs", "Tables", "Bookcases", "Furnishings"],
    "Office Supplies": ["Binders", "Paper", "Storage", "Supplies", "Labels"],
}
segments = ["Consumer", "Corporate", "Home Office"]
segment_probs = [0.51, 0.30, 0.19]

states_by_region = {
    "South": ["Texas", "Florida", "Georgia", "North Carolina", "Tennessee"],
    "West": ["California", "Washington", "Arizona", "Oregon", "Colorado"],
    "East": ["New York", "Pennsylvania", "New Jersey", "Massachusetts", "Virginia"],
    "Central": ["Illinois", "Ohio", "Michigan", "Texas", "Minnesota"],
}

start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 12, 31)
date_range_days = (end_date - start_date).days

rows = []
for i in range(N):
    region = np.random.choice(regions, p=region_probs)
    category = np.random.choice(categories, p=category_probs)
    sub_category = np.random.choice(sub_categories[category])
    segment = np.random.choice(segments, p=segment_probs)
    state = np.random.choice(states_by_region[region])

    base_sales = np.random.gamma(shape=2.2, scale=region_avg_sales[region] / 2.2)
    quantity = np.random.randint(1, 8)
    discount = np.random.choice([0, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5],
                                 p=[0.35, 0.2, 0.15, 0.12, 0.1, 0.05, 0.03])
    sales = round(base_sales * quantity, 2)

    # profit margin shrinks (and can go negative) as discount rises
    base_margin = np.random.normal(0.28, 0.08)
    margin = base_margin - discount * 0.9
    profit = round(sales * margin, 2)

    order_date = start_date + timedelta(days=int(np.random.randint(0, date_range_days)))
    ship_date = order_date + timedelta(days=int(np.random.randint(1, 7)))

    row = {
        "Order_ID": f"ORD-{100000 + i}",
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Ship_Date": ship_date.strftime("%Y-%m-%d"),
        "Customer_ID": f"CUST-{np.random.randint(1000, 9000)}",
        "Segment": segment,
        "Region": region,
        "State": state,
        "Category": category,
        "Sub_Category": sub_category,
        "Sales": sales,
        "Quantity": quantity,
        "Discount": discount,
        "Profit": profit,
    }
    rows.append(row)

df = pd.DataFrame(rows)

# introduce ~15% missing / inconsistent entries to mirror the cleaning step described in README
missing_idx = np.random.choice(df.index, size=int(0.15 * len(df)), replace=False)
half = len(missing_idx) // 2
for idx in missing_idx[:half]:
    col = np.random.choice(["Sub_Category", "Discount", "Ship_Date"])
    df.loc[idx, col] = np.nan
for idx in missing_idx[half:]:
    # inconsistent formatting (extra whitespace / lowercase) to simulate messy raw export
    df.loc[idx, "Region"] = df.loc[idx, "Region"].lower() + " "

df.to_csv("/home/claude/proj1_superstore/data/superstore_raw.csv", index=False)

# quick sanity check on region revenue share (using cleaned copy)
clean = df.copy()
clean["Region"] = clean["Region"].astype(str).str.strip().str.title()
share = clean.groupby("Region")["Sales"].sum()
share_pct = (share / share.sum() * 100).round(1)
print("Rows:", len(df))
print("Missing values introduced:", df.isnull().sum().sum())
print("\nRegion revenue share (%):")
print(share_pct.sort_values(ascending=False))
