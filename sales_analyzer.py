import csv

#reader data
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    content = [row for row in reader] # list comprehension
    print(content)

