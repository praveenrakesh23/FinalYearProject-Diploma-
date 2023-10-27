import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

custom_colors = ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45", "#27aeef", "#b33dc6"]
# Define the SQLite database file path
db_path = 'C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db'

# Create a connection to the SQLite database
conn = sqlite3.connect(db_path)

# Query the raw_inventory and anal tables from the database
raw_inventory_query = "SELECT product_id, stock, cost_price, mrp, product_name FROM raw_inventory"
anal_query = "SELECT product_id, quantity, amount FROM anal"

# Read data from the database tables into pandas DataFrames
raw_inventory_df = pd.read_sql_query(raw_inventory_query, conn)
anal_df = pd.read_sql_query(anal_query, conn)

# Merge the two DataFrames based on 'product_id'
merged_df = pd.merge(raw_inventory_df, anal_df, on='product_id', how='outer')

# Calculate the profit for each product
merged_df['Profit'] = (merged_df['amount'] - merged_df['cost_price'] * merged_df['quantity'])

# Calculate profit margin (profit as a percentage of cost price)
merged_df['ProfitMargin'] = (merged_df['Profit'] / (merged_df['cost_price'] * merged_df['quantity'])) * 100

# Group by 'product_id' and calculate the mean profit margin
profit_margin_summary = merged_df.groupby('product_id')['ProfitMargin'].mean().reset_index()

# Sort the DataFrame by profit margin in descending order
profit_margin_summary = profit_margin_summary.sort_values(by='ProfitMargin', ascending=False)

# Query the product names from the database
product_names_query = "SELECT product_id, product_name FROM raw_inventory"
product_names_df = pd.read_sql_query(product_names_query, conn)

# Merge the profit margin summary with product names
profit_margin_summary = pd.merge(profit_margin_summary, product_names_df, on='product_id', how='left')

profit_margin_summary['product_name'] = profit_margin_summary['product_name'].astype(str)
# Close the database connection
conn.close()

# Create a bar chart for product-wise profit margin with product names on the x-axis
plt.figure(figsize=(12, 6))
plt.bar(profit_margin_summary['product_name'], profit_margin_summary['ProfitMargin'], color = custom_colors)
plt.xlabel('Product Name')
plt.ylabel('Profit Margin (%)')
plt.title('Product-wise Profit Margin')
plt.xticks(rotation=90)
plt.tight_layout()

# Display the bar chart
plt.show()
