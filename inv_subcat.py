import matplotlib.pyplot as plt
import sqlite3

custom_colors = ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45"]

with sqlite3.connect("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db") as db:
    cur = db.cursor()
cur.execute("SELECT  product_subcat,stock FROM raw_inventory")

cate_stock = cur.fetchall()

cate_stock_dict = {cat[0]: 0 for cat in cate_stock}

for cat in cate_stock:
    cats = cat[0]
    stc = cat[1]
    if cats.strip() in cate_stock_dict:
        cate_stock_dict[cats] += stc

plt.figure(figsize=(12, 6))
plt.bar(cate_stock_dict.keys(),cate_stock_dict.values(), color = custom_colors)
plt.xlabel('Sub-Category')
plt.ylabel('Stock (Units)')
plt.title('Inventory occupying stock (In Units)')
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
