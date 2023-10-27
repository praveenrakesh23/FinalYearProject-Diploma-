import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Define the SQLite database file path
db_path = 'sqlite.db'

# Create a connection to the SQLite database
conn = sqlite3.connect(db_path)

# Query the raw_inventory and anal tables from the database
raw_inventory_query = "SELECT product_id, stock, cost_price, mrp, product_cat AS category, product_subcat AS subcategory FROM raw_inventory"
anal_query = "SELECT product_id, quantity, amount FROM anal"

# Read data from the database tables into pandas DataFrames
raw_inventory_df = pd.read_sql_query(raw_inventory_query, conn)
anal_df = pd.read_sql_query(anal_query, conn)

# Merge the two DataFrames based on 'product_id'
merged_df = pd.merge(raw_inventory_df, anal_df, on='product_id', how='outer')

# Calculate the profit for each product
merged_df['Profit'] = (merged_df['amount'] - merged_df['cost_price'] * merged_df['quantity'])

# Group by 'product_id' and sum the profits
profit_summary = merged_df.groupby('product_id')['Profit'].sum().reset_index()

# Sort the DataFrame by profit in descending order and select the top 10 products
top_10_products = profit_summary.sort_values(by='Profit', ascending=False).head(10)

# Query the product names, categories, and subcategories from the database
product_info_query = "SELECT product_id, product_name, product_cat AS category, product_subcat AS subcategory FROM raw_inventory"
product_info_df = pd.read_sql_query(product_info_query, conn)

# Merge the top 10 products with their names, categories, and subcategories
top_10_products = pd.merge(top_10_products, product_info_df, on='product_id', how='left')

# Group by category and sum the profits
category_profit = merged_df.groupby('category')['Profit'].sum().reset_index()

# Group by subcategory and sum the profits
subcategory_profit = merged_df.groupby('subcategory')['Profit'].sum().reset_index()

# Close the database connection
conn.close()

# Create a bar chart for the top 10 products with product names and categories
plt.figure(figsize=(18, 6))
plt.subplot(131)
plt.bar(top_10_products['product_name'], top_10_products['Profit'])
plt.xlabel('Product Name')
plt.ylabel('Profit')
plt.title('Top 10 Selling Products by Profit')
plt.xticks(rotation=90)

# Create a bar chart for category-wise profit
plt.subplot(132)
plt.bar(category_profit['category'], category_profit['Profit'], alpha=0.7)
plt.xlabel('Category')
plt.ylabel('Profit')
plt.title('Category Wise Profit')
plt.xticks(rotation=90)

# Create a bar chart for subcategory-wise profit
plt.subplot(133)
plt.bar(subcategory_profit['subcategory'], subcategory_profit['Profit'], alpha=0.7)
plt.xlabel('Subcategory')
plt.ylabel('Profit')
plt.title('Subcategory Wise Profit')
plt.xticks(rotation=90)

# Adjust layout for multiple subplots
plt.tight_layout()

# Display the plots
plt.show()
