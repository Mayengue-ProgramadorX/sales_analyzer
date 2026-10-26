# Title – # **Sales_Processor**

**This project processes sales data and generates two reports**:
a human‑readable text summary **(sales_report.txt)** and a structured CSV summary **(product_summary.csv).**
The program calculates total revenue, revenue per product, quantity sold per product, and identifies the day with the highest revenue.

It demonstrates accumulator patterns, dictionary aggregation, file writing, and basic reporting logic in Python.

**Features**
### **1. Line Revenue Calculation
Each sale row computes its revenue using:
 **revenue = quantity * price**


### **2. Accumulators (Dictionary Aggregation)
The program uses dictionaries to accumulate totals:

**revenue_by_product – total revenue per product**

**quantity_by_product – total quantity sold per product**

**revenue_by_day – total revenue per day**

Accumulator pattern used throughout:
# Accumulators: each line adds values into a dictionary.
# If the key does not exist yet, .get(key, 0) returns 0.
# This ensures the current value is incremented correctly,
# creating the key on the first occurrence and summing on the next ones.


### **3. Best Day Calculation
Finds the day with the highest revenue:
**best_day = max(revenue_by_day, key=revenue_by_day.get)**


### **4. Generates sales_report.txt
A formatted text file containing:

**Total revenue**

**Revenue by product**

**Quantity sold by product**

**Best day**

Example snippet:
Total Revenue: $1749.32

Revenue by Product:
  - Widget A: $779.61
  - Widget B: $719.76
  - Widget C: $249.95

Quantity Sold by Product:
  - Widget A: 39
  - Widget B: 24
  - Widget C: 5

Best Day (Highest Revenue): 2024-01-03


### **5. Generates product_summary.csv
A CSV file with columns:
**product,total_quantity,total_revenue**

### **How to Run
**python sales_processor.py**

After execution, two files will be created:

**sales_report.txt**

**product_summary.csv**

Both will appear in the same directory as the script.


### **Example Output
**sales_report.txt**
=== Sales Summary ===
Total Revenue: $1749.32
Highest Revenue Day: 2024-01-03


**product_summary.csv**
product,total_quantity,total_revenue
Widget A,39,779.61
Widget B,24,719.76
Widget C,5,249.95
