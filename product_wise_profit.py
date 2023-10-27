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

# Group by 'product_id' and calculate the total profit
profit_summary = merged_df.groupby('product_id')['Profit'].sum().reset_index()

# Sort the DataFrame by total profit in descending order
profit_summary = profit_summary.sort_values(by='Profit', ascending=False)

# Query the product names from the database
product_names_query = "SELECT product_id, product_name FROM raw_inventory"
product_names_df = pd.read_sql_query(product_names_query, conn)

# Merge the top 10 products with their names
top_10_profitable = pd.merge(profit_summary.head(10), product_names_df, on='product_id', how='left')

# Close the database connection
conn.close()

print(top_10_profitable)
# Create a bar chart for top 10 profitable products with product names
plt.figure(figsize=(12, 6))
plt.barh(top_10_profitable['product_name'], top_10_profitable['Profit'], color=custom_colors)
plt.ylabel('Product Name')
plt.xlabel('Profit Amount'+'u(\u20B9)')
plt.title('Top 10 Profitable Products by Profit Amount')

plt.tight_layout()

# Display the bar chart
plt.show()
