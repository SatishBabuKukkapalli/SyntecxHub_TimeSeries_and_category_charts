import csv
from datetime import datetime, timedelta
import random

random.seed(42)

categories = ["Electronics", "Furniture", "Clothing", "Toys", "Grocery"]
start_date = datetime(2023, 1, 1)
num_rows = 100

rows = []
for i in range(num_rows):
    date = start_date + timedelta(days=i)
    category = categories[i % len(categories)]
    base_sales = {
        "Electronics": 1200,
        "Furniture": 800,
        "Clothing": 400,
        "Toys": 300,
        "Grocery": 600
    }[category]
    noise = random.randint(-100, 200)
    sales = max(0, base_sales + noise + int(20 * (i % 12)))
    rows.append([date.strftime("%Y-%m-%d"), category, sales])

with open("sales_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Category", "Sales"])
    writer.writerows(rows)

print("✅ sales_data.csv created successfully with 100 rows.")
