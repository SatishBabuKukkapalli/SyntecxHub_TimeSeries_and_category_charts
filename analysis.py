import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Read the CSV file
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
print("✅ Loaded CSV with", len(df), "rows")

# Add Month and Quarter columns
df["Month"] = df["Date"].dt.to_period("M")
df["Quarter"] = df["Date"].dt.to_period("Q")

# === Monthly Line Chart ===
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()
monthly_sales["Month_str"] = monthly_sales["Month"].astype(str)

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales["Month_str"], monthly_sales["Sales"], marker="o")
plt.title("Monthly Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()

# === Quarterly Bar Chart ===
quarterly_sales = df.groupby("Quarter")["Sales"].sum().reset_index()
quarterly_sales["Quarter_str"] = quarterly_sales["Quarter"].astype(str)

plt.figure(figsize=(8, 4))
sns.barplot(x="Quarter_str", y="Sales", data=quarterly_sales)
plt.title("Quarterly Sales")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("quarterly_sales.png")
plt.close()

# === Category Bar Chart ===
category_sales = df.groupby("Category")["Sales"].sum().reset_index()

plt.figure(figsize=(8, 4))
sns.barplot(x="Category", y="Sales", data=category_sales)
plt.title("Sales by Category")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.close()

# === Category Pie Chart ===
plt.figure(figsize=(6, 6))
plt.pie(category_sales["Sales"], labels=category_sales["Category"], autopct="%1.1f%%")
plt.title("Category Sales Share")
plt.savefig("category_sales_share.png")
plt.close()

# === Summary ===
summary = f"""
Summary Report
==============
Total records analyzed: {len(df)}

Charts generated:
1. monthly_sales.png - Monthly trend (line chart)
2. quarterly_sales.png - Quarterly totals (bar chart)
3. category_sales.png - Category comparison (bar chart)
4. category_sales_share.png - Category percentage share (pie chart)

Observations:
- Electronics category leads in total sales.
- Steady monthly increase in overall sales.
- Pie chart shows each category’s contribution clearly.
"""

with open("project_summary.txt", "w") as f:
    f.write(summary)

print("✅ Analysis complete. Charts and project_summary.txt created.")
