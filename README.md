## 📊 Project Overview

This project is part of my **Data Science Internship with SyntecxHub**.  
It focuses on **Time Series Analysis** and **Category Chart Visualization** using Python.

I created a synthetic dataset of 100 sales records and analyzed it using **Pandas**, **Matplotlib**, and **Seaborn**.

The goal of this project is to:
- Analyze sales trends over time (monthly and quarterly)
- Compare category-wise performance
- Create visual reports for business insights

## 📈 Visualizations Generated
1. **Monthly Sales (Line Chart)** — shows overall sales trend over time  
2. **Quarterly Sales (Bar Chart)** — compares performance by quarter  
3. **Sales by Category (Bar Chart)** — highlights top-performing product categories  
4. **Category Sales Share (Pie Chart)** — visualizes percentage contribution of each category  

## 🧰 Technologies Used
- Python  
- Pandas  
- Matplotlib  
- Seaborn  

## 📁 Files in the Repository
- `generate_data.py` → generates a synthetic dataset (100 rows)
- `analysis.py` → analyzes and visualizes data
- `sales_data.csv` → dataset file
- `monthly_sales.png`, `quarterly_sales.png`, `category_sales.png`, `category_sales_share.png` → visualization charts
- `project_summary.txt` → summary report
- `requirements.txt` → dependencies

## 🧠 Key Learnings
- Data handling with Pandas  
- Creating and customizing visualizations  
- Understanding time-based and categorical data trends  


## How to Run
1. Open VS Code terminal (`Ctrl + ~`)
2. Create virtual environment:
   - `python -m venv venv`
3. Activate it:
   - Windows → `venv\Scripts\activate`
   - Mac/Linux → `source venv/bin/activate`
4. Install dependencies:
   - `pip install -r requirements.txt`
5. Generate data:
   - `python generate_data.py`
6. Run analysis:
   - `python analysis.py`
7. Open the PNG and TXT files in VS Code to view results.


