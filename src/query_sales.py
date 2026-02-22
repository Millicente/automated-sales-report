import sqlite3

conn = sqlite3.connect('data/sales.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT region, 
           COUNT(*) as total_transactions,
           ROUND(SUM(total_amount), 2) as total_revenue
    FROM sales
    GROUP BY region
    ORDER BY total_revenue DESC
''')

results = cursor.fetchall()

print("\n--- Total Sales by Region ---")
for row in results:
    print(f"Region: {row[0]} | Transactions: {row[1]} | Revenue: ${row[2]}")

cursor.execute('''
    SELECT product,
           COUNT(*) as total_transactions,
           ROUND(SUM(total_amount), 2) as total_revenue
    FROM sales
    GROUP BY product
    ORDER BY total_revenue DESC
''')

results = cursor.fetchall()

print("\n--- Total Sales by Product ---")
for row in results:
    print(f"Product: {row[0]} | Transactions: {row[1]} | Revenue: ${row[2]}")    

cursor.execute('''
    SELECT payment_method,
           COUNT(*) as total_transactions,
           ROUND(SUM(total_amount), 2) as total_revenue
    FROM sales
    GROUP BY payment_method
    ORDER BY total_revenue DESC
''')

results = cursor.fetchall()

print("\n--- Total Sales by Payment Method ---")
for row in results:
    print(f"Payment Method: {row[0]} | Transactions: {row[1]} | Revenue: ${row[2]}")    
    
conn.close()    