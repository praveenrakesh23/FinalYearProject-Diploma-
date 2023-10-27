import matplotlib.pyplot as plt
import sqlite3

custom_colors = ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45"]

# Define the number of rows and columns
num_rows = 5
num_cols = 1

# Define the width ratios for columns
width_ratios = [1]

# Define the height ratios for rows (one subplot per row)
height_ratios = [1] * num_rows

# Create a Matplotlib figure with specified column and row ratios
fig, axs = plt.subplots(num_rows, num_cols, figsize=(8, 16), gridspec_kw={'width_ratios': width_ratios, 'height_ratios': height_ratios})
plt.subplots_adjust(top=1, left=0.13, bottom=0.1, hspace=0.302)

# FOR TOP SELLING PRODUCTS
with sqlite3.connect("sqlite.db") as db:
    cur = db.cursor()
    query = "SELECT product_name, amount FROM anal"
    cur.execute(query)
    data = cur.fetchall()

    product_names = [item[0] for item in data]
    amounts = [item[1] for item in data]

    sorted_data = sorted(zip(product_names, amounts), key=lambda x: x[1], reverse=True)
    x_top_7 = [item[0] for item in sorted_data[:7]]
    y_top_7 = [item[1] for item in sorted_data[:7]]

# TOP SELLING PRODUCTS BAR CHART
axs[0].barh(x_top_7, y_top_7, color=custom_colors)
axs[0].set_xlabel('Sales Amount', fontsize=16)
axs[0].set_ylabel('Product Name', fontsize=16)

axs[0].tick_params(axis='y', labelsize=8)  # Adjust the labelsize to your preference
axs[0].tick_params(axis='x', labelsize=8)

# WEEKLY BILLS GRAPH
date_list = {"Sunday": 0, "Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0}

# retrieving data from database and counting
with sqlite3.connect("sqlite.db") as db:
    cur = db.cursor()
    query2 = "SELECT Day FROM bill"
    cur.execute(query2)
    dates = cur.fetchall()

    for date in dates:
        day = date[0]
        if day in date_list:
            date_list[day] += 1

days = list(date_list.keys())
counts = list(date_list.values())

# Bills Bar Chart
axs[1].scatter(days, counts, color=custom_colors)
axs[1].plot(days, counts)
axs[1].set_xlabel('Days of the week', fontsize=14)
axs[1].set_ylabel('Bills Generated', fontsize=14)

# for inventory occupancy graph
cur.execute("SELECT  product_cat FROM raw_inventory")

categories = cur.fetchall()

# main dictionary for above purpose
category_dict = {category[0].strip(): 0 for category in categories}
csat_dict = category_dict

# For category selling analysis
cur.execute("SELECT category,quantity FROM anal")

cat_anal = cur.fetchall()
# Main dictionary for above purpose
cat_anal_dict = {cat[0]: 0 for cat in cat_anal}

for cat in cat_anal:
    cats_anal = cat[0].strip()  # for category
    quat_anal = cat[1]  # for quantity
    if cats_anal in cat_anal_dict:
        cat_anal_dict[cats_anal] += quat_anal
print('Sold quantity:')
print(cat_anal_dict)

for cat in categories:
    cats = cat[0].strip()
    if cats in category_dict:
        category_dict[cats] += 1

print('no.of products in a category:')
print(category_dict)

cur.execute("SELECT  product_cat,stock FROM raw_inventory")

cate_stock = cur.fetchall()

cate_stock_dict = {cat[0]: 0 for cat in cate_stock}

for cat in cate_stock:
    cats = cat[0]
    stc = cat[1]
    if cats.strip() in cate_stock_dict:
        cate_stock_dict[cats] += stc

print('stocks per category:')
print(cate_stock_dict)

category_sold = list(cat_anal_dict.keys())
quantity_sold = list(cat_anal_dict.values())
axs[2].bar(category_sold, quantity_sold, color= custom_colors)

category_ = list(cate_stock_dict.keys())
stock_ = list(cate_stock_dict.values())
axs[3].bar(category_, stock_, color=custom_colors)

plt.tight_layout()

# Show the grid of subplots
plt.show()












import matplotlib.pyplot as plt
import sqlite3

custom_colors = ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45"]

with sqlite3.connect("sqlite.db") as db:
    cur = db.cursor()
    cur.execute("SELECT category, quantity FROM anal")
    cat_anal = cur.fetchall()

# Create lists to store category names and quantities
categories = []
quantities = []

# Extract data from the fetched rows
for cat in cat_anal:
    categories.append(cat[0].strip())  # for category
    quantities.append(cat[1])  # for quantity

plt.figure(figsize=(12, 6))
plt.barh(categories, quantities, color=custom_colors)
plt.xlabel('Category')
plt.ylabel('Sold Stock')
plt.title('Top Selling Categories (In terms of stock sold)')
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
