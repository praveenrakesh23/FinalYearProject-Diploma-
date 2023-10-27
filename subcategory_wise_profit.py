import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

custom_colors = ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45", "#27aeef", "#b33dc6"]

# Define the SQLite database file path
db_path = 'C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db'

# Create a connection to the SQLite database
conn = sqlite3.connect(db_path)

# Query the raw_inventory and anal tables from the database
raw_inventory_query = "SELECT product_id, stock, cost_price, mrp, product_subcat AS subcategory FROM raw_inventory"
anal_query = "SELECT product_id, quantity, amount FROM anal"

# Read data from the database tables into pandas DataFrames
raw_inventory_df = pd.read_sql_query(raw_inventory_query, conn)
anal_df = pd.read_sql_query(anal_query, conn)

# Merge the two DataFrames based on 'product_id'
merged_df = pd.merge(raw_inventory_df, anal_df, on='product_id', how='outer')

# Calculate the profit for each product
merged_df['Profit'] = (merged_df['amount'] - merged_df['cost_price'] * merged_df['quantity'])

# Group by 'subcategory' and calculate the total profit
subcategory_profit = merged_df.groupby('subcategory')['Profit'].sum().reset_index()

# Sort the DataFrame by total profit in descending order
subcategory_profit = subcategory_profit.sort_values(by='Profit', ascending=False)

# Close the database connection
conn.close()

# Create a bar chart for subcategory-wise profit in amount
plt.figure(figsize=(12, 6))
plt.bar(subcategory_profit['subcategory'], subcategory_profit['Profit'], color=custom_colors)
plt.xlabel('Subcategory')
plt.ylabel('Profit Amount (₹)')
plt.title('Subcategory-wise Profit Amount')
plt.tight_layout()

# Display the bar chart
plt.show()
