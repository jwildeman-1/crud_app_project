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

menu = """

  There are 20 products in the database.

  Available opoerations are List, Show, Create, Update, and Destroy.

  Please select an operation: """

new_operation = input(menu)

if new_operation.title() == "List":
    print("LISTING PRODUCTS")
elif new_operation.title() == "Show":
    print("SHOWING A PRODUCT")
elif new_operation.title() == "Create":
    print("CREATING A PRODUCT")
elif new_operation.title() == "Update":
    print("UPDATING A PRODUCT")
elif new_operation.title() == "Destroy":
    print("DESTROYING A PRODUCT")
else:
    print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

#print("There are 20 products in the database.") # + str(len(csv_file_path)) +

#print("")

#print("    command | operation | description")
#print("    ------- | --------- | -----------------")
#print("       1    | 'List'    | Display a list of product identifiers and names")
#print("       2    | 'Show'    | Show information about a product")
#print("       3    | 'Create'  | Add a new product")
#print("       4    | 'Update'  | Edit an existing product")
#print("       5    | 'Destroy' | Delete an existing product")

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
