import sqlite3

conn = sqlite3.connect("sqlite.db")
cur = conn.cursor()

strr = "UPDATE anal SET amount=2580 WHERE product_id=327004"

cur.execute(strr)

conn.commit()