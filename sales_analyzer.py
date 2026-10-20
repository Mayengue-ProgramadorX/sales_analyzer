import csv

total_revenue = 0

revenue_by_product = {}
quantity_by_product = {}
revenue_by_day = {}

#reader data
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        #print(row)
        product = row['product']
        date = row['date']
        quantity = int(row['quantity']) # convert to int()
        price = float(row['price']) #convert to float()
        
        #calculate 
        revenue = price * quantity
        total_revenue += revenue

        # Accumulators: each line adds values into a dictionary.
        # If the key does not exist yet, .get(key, 0) returns 0.
        # This ensures the current value is incremented correctly,
        # creating the key on the first occurrence and summing on the next ones.
        revenue_by_product[product] = revenue_by_product.get(product, 0) + revenue  
        quantity_by_product[product] = quantity_by_product.get(product, 0) + quantity  
        revenue_by_day[date] = revenue_by_day.get(date, 0) + revenue

    # Finds the day with the highest total revenue by selecting the key whose value is the largest.
    best_day = max(revenue_by_day, key=revenue_by_day.get)



# Generates a sales summary in the file sales_report.txt using standard text formatting.
with open("sales_report.txt", "w") as file:
    file.write(f"Total Revenue: ${total_revenue:.2f}\n\n") 

    file.write("Revenue by Product:\n")
    for product, revenue in revenue_by_product.items():
        file.write(f"  - {product}: ${revenue:.2f}\n")

    file.write("\nQuantity Sold by Product:\n")
    for product, qty in quantity_by_product.items():
        file.write(f"  - {product}: {qty}\n")

    file.write(f"\nBest Day: {best_day}\n")



# Writes a CSV summary with one row per product, including total quantity and total revenue.
with open("product_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header row
    writer.writerow(["product", "total_quantity", "total_revenue"])

    # One row per product
    for product in revenue_by_product:
        writer.writerow([
            product,
            quantity_by_product[product],
            f"{revenue_by_product[product]:.2f}"   # format to 2 decimal place
        ])
