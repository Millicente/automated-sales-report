import random
import sqlite3
from datetime import datetime

conn = sqlite3.connect('data/sales.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        customer_name TEXT,
        product TEXT,
        category TEXT,
        quantity INTEGER,
        unit_price REAL,
        total_amount REAL,
        region TEXT,
        payment_method TEXT
    )
''')


products = [
    "Laptop",
    "Smartphone",
    "Tablet",
    "Wireless Headphones",
    "Smart Watch",
    "Office Chair",
    "Desk",
    "External Hard Drive",
    "Gaming Console",
    "Monitor"
]
categories = [
    "Electronics",
    "Accessories",
    "Furniture",
    "Gaming",
    "Office Equipment"
]
regions = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]
payment_methods = [
    "Credit Card",
    "Debit Card",
    "Bank Transfer",
    "Cash",
    "Mobile Payment"
]                         
customer_names = [
    "Tristiano Accardi",
    "Mary Johnson",
    "David Brown",
    "Sophia Williams",
    "Michael Davis",
    "Emma Wilson",
    "Daniel Martinez",
    "Olivia Anderson",
    "James Taylor",
    "Ava Thomas",
    "BrightTech Solutions",
    "Ferguson Corporations",
    "NextGen Enterprises",
    "Prime Retail Group",
    "Summit Holdings",
    "UrbanEdge Stores",
    "Vertex Consulting",
    "Skyline Innovations",
    "Elite Corporate Services",
    "GreenField Industries"
]

sales_data = []

for i in range(1000):
    customer = random.choice(customer_names)
    product = random.choice(products)
    category = random.choice(categories)
    region = random.choice(regions)
    payment = random.choice(payment_methods)
    date = f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
    quantity = random.randint(1, 20)
    unit_price = round(random.uniform(10.0, 1500.0), 2)
    total_amount = round(quantity * unit_price, 2)

    sales_data.append((date, customer, product, category, quantity, unit_price, total_amount, region, payment))

cursor.executemany('''
    INSERT INTO sales (date, customer_name, product, category, quantity, unit_price, total_amount, region, payment_method)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', sales_data)

conn.commit()
conn.close()

print("Database created and populated with 1000 sales records!")