import sqlite3

# Connect to the database
conn = sqlite3.connect("sqlite.db")
cur = conn.cursor()

# Retrieve product data from 'raw_inventory' table
cur.execute("SELECT product_name, mrp, stock FROM raw_inventory")
product_data = cur.fetchall()

# Retrieve profit data from 'anal' table
cur.execute("SELECT product_name, amount FROM anal")
profit_data = cur.fetchall()

# Create a dictionary to store the standard stock level (50 for all products)
standard_stock = {product_name: 50 for product_name, _, _ in product_data}

# Create a dictionary to store the profit for each product
profit_dict = {product_name: amount for product_name, amount in profit_data}

# Define ANSI escape codes for text color
GREEN = "\033[92m"
RED = "\033[91m"
END = "\033[0m"

# Compare profit to standard stock level and determine profitability
profitability_dict = {}
for product_name, mrp, stock in product_data:
    if product_name in profit_dict:
        profit = profit_dict[product_name]
        if stock >= standard_stock[product_name]:
            is_profitable = profit > 0
        else:
            is_profitable = profit / stock > 0
        profitability_dict[product_name] = is_profitable

# Close the connection
conn.close()

# Print the results with colored text
for product_name, is_profitable in profitability_dict.items():
    profitability_status = "Profitable" if is_profitable else "Not Profitable"
    color_code = GREEN if is_profitable else RED
    print(f"{product_name}: {color_code}{profitability_status}{END}")
