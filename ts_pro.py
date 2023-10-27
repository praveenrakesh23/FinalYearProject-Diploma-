import matplotlib.pyplot as plt
import sqlite3

custom_colors = ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45"]

with sqlite3.connect("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db") as db:
    cur = db.cursor()
cur.execute("SELECT product_name,quantity FROM anal")

cat_anal = cur.fetchall()
# Main dictionary for above purpose
cat_anal_dict = {cat[0]: 0 for cat in cat_anal}

for cat in cat_anal:
    cats_anal = cat[0].strip()  # for category
    quat_anal = cat[1]  # for quantity
    if cats_anal in cat_anal_dict:
        cat_anal_dict[cats_anal] += quat_anal


plt.figure(figsize=(12, 6))
plt.bar(cat_anal_dict.keys(),cat_anal_dict.values(), color = custom_colors)
plt.xlabel('Product')
plt.ylabel('Sold Stock')
plt.title('Top Selling Products (In terms of stock sold)')
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()