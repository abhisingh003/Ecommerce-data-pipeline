import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute("SELECT SUM(total_price) FROM orders")
print("Total Revenue:", cursor.fetchone())

cursor.execute("""
SELECT product, SUM(quantity)
FROM orders
GROUP BY product
ORDER BY 2 DESC
""")
print("Top Products:", cursor.fetchall())

conn.close()