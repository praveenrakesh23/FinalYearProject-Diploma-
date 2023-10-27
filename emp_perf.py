import matplotlib.pyplot as plt
import sqlite3

custom_colors = ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45"]

with sqlite3.connect("C:\\Users\\prave\\OneDrive\\Desktop\\PRAVEENPROJECT\\praveen\\sqlite.db") as db:
    cur = db.cursor()
cur.execute("SELECT Employee FROM bill")

cat_anal = cur.fetchall()
# Main dictionary for above purpose
cat_anal_dict = {cat[0]: 0 for cat in cat_anal}

for date in cat_anal:
    day = date[0]  # Extract the day from the fetched data
    if day in cat_anal_dict:
        cat_anal_dict[day] += 1

plt.figure(figsize=(12, 6))
plt.bar(cat_anal_dict.keys(),cat_anal_dict.values(), color = custom_colors)
plt.xlabel('Employee ID')
plt.ylabel('Sales')
plt.title('Top performing employee (In terms of Bill generated)')
plt.tight_layout()

plt.show()