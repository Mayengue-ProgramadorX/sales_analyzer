import csv

total_revenue = 0
#reader data
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        #print(row)
        quantity = int(row['quantity']) # convert to int()
        price = float(row['price']) #convert to float()
        
        #calculate 
        total_row = price * quantity
        total_revenue += total_row