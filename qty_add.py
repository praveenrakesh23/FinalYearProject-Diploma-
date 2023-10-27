import sqlite3

with sqlite3.connect('sqlite.db') as db:
    cur = db.cursor()

query = 'SELECT product_name FROM raw_inventory'
cur.execute(query)
raw_pro_names = cur.fetchall()

pro_name_list = []
for i in raw_pro_names:
    s = str(i)
    product_name = {"product_name": s}
    pro_name_list.append(product_name)

search = 'Dosa Rice(5 kg)'
