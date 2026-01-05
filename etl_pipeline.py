import pandas as pd
import mysql.connector
from datetime import datetime

# ------------------ DATABASE CONNECTION ------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="fleximart"
)
cursor = conn.cursor()

# ------------------ HELPERS ------------------
def clean_date(date_val):
    try:
        return pd.to_datetime(date_val, dayfirst=True).date()
    except:
        return None

def clean_phone(phone):
    if pd.isna(phone):
        return None
    digits = ''.join(filter(str.isdigit, str(phone)))
    if len(digits) == 10:
        return "+91-" + digits
    if len(digits) == 12 and digits.startswith("91"):
        return "+91-" + digits[2:]
    return None

# ------------------ DATA QUALITY COUNTERS ------------------
report = {
    "customers_processed": 0,
    "customers_duplicates": 0,
    "customers_loaded": 0,
    "products_processed": 0,
    "products_loaded": 0,
    "sales_processed": 0,
    "sales_loaded": 0
}

# ------------------ EXTRACT ------------------
customers = pd.read_csv("customers_raw.csv")
products = pd.read_csv("products_raw.csv")
sales = pd.read_csv("sales_raw.csv")

report["customers_processed"] = len(customers)
report["products_processed"] = len(products)
report["sales_processed"] = len(sales)

# ------------------ TRANSFORM CUSTOMERS ------------------
customers.drop_duplicates(subset="customer_id", inplace=True)
report["customers_duplicates"] = report["customers_processed"] - len(customers)

customers.dropna(subset=["email"], inplace=True)
customers["phone"] = customers["phone"].apply(clean_phone)
customers["registration_date"] = customers["registration_date"].apply(clean_date)

# ------------------ LOAD CUSTOMERS ------------------
for _, row in customers.iterrows():

    cursor.execute(
        "SELECT COUNT(*) FROM customers WHERE email=%s",
        (row["email"],)
    )
    exists = cursor.fetchone()[0]

    if exists == 0:
        cursor.execute("""
            INSERT INTO customers (first_name, last_name, email, phone, city, registration_date)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            row["first_name"].strip(),
            row["last_name"].strip(),
            row["email"],
            row["phone"],
            row["city"],
            row["registration_date"]
        ))
        report["customers_loaded"] += 1
conn.commit()

# ------------------ TRANSFORM PRODUCTS ------------------
products.dropna(subset=["price"], inplace=True)
products["category"] = products["category"].str.capitalize()
products["stock_quantity"] = products["stock_quantity"].fillna(0)
# ------------------ LOAD PRODUCTS ------------------
for _, row in products.iterrows():
    cursor.execute("""
        INSERT INTO products (product_name, category, price, stock_quantity)
        VALUES (%s,%s,%s,%s)
    """, (
        row["product_name"],
        row["category"],
        row["price"],
        int(row["stock_quantity"])
    ))
    report["products_loaded"] += 1

conn.commit()

# ------------------ SALES → ORDERS & ORDER_ITEMS ------------------
sales.drop_duplicates(subset="transaction_id", inplace=True)
sales.dropna(subset=["customer_id", "product_id"], inplace=True)
sales["transaction_date"] = sales["transaction_date"].apply(clean_date)

for _, row in sales.iterrows():
    cursor.execute(
        "SELECT customer_id FROM customers WHERE email IS NOT NULL LIMIT 1"
    )
    cust = cursor.fetchone()
    if not cust:
        continue

    total = row["quantity"] * row["unit_price"]

    cursor.execute("""
        INSERT INTO orders (customer_id, order_date, total_amount, status)
        VALUES (%s,%s,%s,%s)
    """, (
        cust[0],
        row["transaction_date"],
        total,
        row["status"]
    ))
    order_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal)
        VALUES (%s,%s,%s,%s,%s)
    """, (
        order_id,
        1,
        row["quantity"],
        row["unit_price"],
        total
    ))

    report["sales_loaded"] += 1

conn.commit()

# ------------------ DATA QUALITY REPORT ------------------
with open("data_quality_report.txt", "w") as f:
    for k, v in report.items():
        f.write(f"{k}: {v}\n")

print("ETL PIPELINE COMPLETED SUCCESSFULLY")

cursor.close()
conn.close()

