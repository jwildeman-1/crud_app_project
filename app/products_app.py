#import pandas as pd
import getpass

user_name = getpass.getuser()

print("----------------------")
print("PRODUCTS APPLICATION")
print("----------------------")
print("Welcome to the products app, " + (user_name) + "!")
print("")

import csv
import operator

csv_file_path = "data\products.csv"

products = []

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

print("There are " + str(len(csv_file_path)) + " products in the database.") # this should return a dynamic count of the products in the database

menu = """

    command | operation | description
    ------- | --------- | -----------------
       1    | 'List'    | Display a list of product identifiers and names
       2    | 'Show'    | Show information about a product
       3    | 'Create'  | Add a new product
       4    | 'Update'  | Edit an existing product
       5    | 'Destroy' | Delete an existing product

Please select a command: """

new_operation = input(menu)

d = {}
d["List"] = 1
d["Show"] = 2
d["Create"] = 3
d["Update"] = 4
d["Destroy"] = 5

if new_operation.title() == "1":
    print("")
    print(" + LISTING PRODUCTS")
elif new_operation.title() == "2":
    print("")
    print(" + SHOWING A PRODUCT")
elif new_operation.title() == "3":
    print("")
    print(" + CREATING A PRODUCT")
elif new_operation.title() == "4":
    print("")
    print(" + UPDATING A PRODUCT")
elif new_operation.title() == "5":
    print("")
    print(" + DESTROYING A PRODUCT")
else:
    print("")
    print(" + OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED COMMANDS.")

#command = []

print("")

#while True:
#    command = input("Please select a command: ")
#    if product_id == "Quit":
#        break
#    else:
#        command.append(int(csv_file_path))

#def lookup_product_by_id(product_id):
#    matching_products = [product for product in products if product["id"] == product_id]
#    return matching_products[0] # because the line above gives us a list and we want to return a single item.
