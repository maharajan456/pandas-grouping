# -------------------------------
# Task 1: Basic Grouping & Aggregations
# -------------------------------

import pandas as pd
import random

random.seed(42)

# Define data parameters
regions = ['North', 'South', 'East', 'West']
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books']
salespersons = ['Alice', 'Bob', 'Carol', 'David', 'Emma', 'Frank']

# Generate synthetic dataset (200 transactions)
data = {
    'transaction_id': range(1001, 1201),
    'region': [random.choice(regions) for _ in range(200)],
    'category': [random.choice(categories) for _ in range(200)],
    'salesperson': [random.choice(salespersons) for _ in range(200)],
    'sales_amount': [round(random.uniform(50, 5000), 2) for _ in range(200)],
    'customer_id': [random.randint(5000, 5100) for _ in range(200)]
}

df = pd.DataFrame(data)

# -------------------------------
# Task 1 Analyses
# -------------------------------

# 1. Total sales amount per region (sorted descending)
total_sales_region = (
    df.groupby('region')['sales_amount']
      .sum()
      .reset_index()
      .sort_values('sales_amount', ascending=False)
)

# 2. Count of transactions per category
count_transactions_category = (
    df.groupby('category')['transaction_id']
      .count()
      .reset_index()
)

# 3. Average sales amount per salesperson
avg_sales_salesperson = (
    df.groupby('salesperson')['sales_amount']
      .mean()
      .reset_index()
)

# Display results
print("\nTotal Sales by Region:")
print(total_sales_region)

print("\nTransaction Count by Category:")
print(count_transactions_category)

print("\nAverage Sales Amount per Salesperson:")
print(avg_sales_salesperson)

# ---------------------------------------
# Task 2: Multi-Column Grouping & Aggregations
# ---------------------------------------

# 1. Group by region & category → total sales
region_category_sales = (
    df.groupby(['region', 'category'])['sales_amount']
      .sum()
      .reset_index()
)

# 2. Salesperson metrics → sum, mean, count
salesperson_stats = (
    df.groupby('salesperson')['sales_amount']
      .agg(['sum', 'mean', 'count'])
      .reset_index()
)

# 3. Sort salespersons by total sales (sum) → top performer
salesperson_sorted = salesperson_stats.sort_values('sum', ascending=False)

# 4. Find category with maximum total revenue using idxmax()
category_sales = df.groupby('category')['sales_amount'].sum()
top_category = category_sales.idxmax()

# Display results
print("\nTotal Sales by Region & Category:")
print(region_category_sales)

print("\nSalesperson Stats (Sum, Mean, Count):")
print(salesperson_stats)
print(salesperson_sorted)

print("\nTop Revenue-Generating Category:")
print(top_category)

# ---------------------------------------
# Task 3: Custom Aggregation & Summary Report
# ---------------------------------------

# 1. Define sales range function
def sales_range(x):
    return x.max() - x.min()

# 2. Apply custom + standard aggregations by region
region_agg_custom = (
    df.groupby('region')['sales_amount']
      .agg(['sum', 'mean', 'min', 'max', sales_range])
      .reset_index()
)

print("\nCustom Aggregation by Region:")
print(region_agg_custom)

# 3. Final summary report with dictionary-based agg()
region_summary = (
    df.groupby('region')
      .agg({
          'sales_amount': ['sum', 'mean'],   # multiple stats on same column
          'customer_id': 'count'             # total number of transactions
      })
      .reset_index()
)

print("\nFinal Summary Report by Region:")
print(region_summary)
