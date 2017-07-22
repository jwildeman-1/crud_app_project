import pandas as pd
import getpass

user_name = getpass.getuser()

print("----------------------")
print("PRODUCTS APPLICATION")
print("----------------------")
print("Welcome to the products app, " + (user_name) + "!")
print("")

import csv
import os

products = []

csv_file_path = r"C:\Users\Jason\Desktop\python-practice\crud\data\products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = list(csv.DictReader(csv_file, delimiter=','))
    for row in reader:
        products.append(row)

# other_path = "C:\Users\Jason\Desktop\python-practice\crud\data\other_products.csv"
#
# with open(other_path), "w") as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
#     writer.writeheader() # uses fieldnames set above
#     for product in products:
#         writer.writerow(product)

print("There are {0} products in the database.".format(len(products))) # .format(len(products)) " + str(len(products)) + " this should return a dynamic count of the products in the database

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
new_operation = new_operation.title()

d = {}
d["List"] = 1
d["Show"] = 2
d["Create"] = 3
d["Update"] = 4
d["Destroy"] = 5

def list_products():
    print("")
    print("---- LISTING PRODUCTS:")
    print("")
    for product in products:
        print(" + Product #" + str(product["id"]) + ": " + product["name"])

def show_product():
    print("")
    product_number = input("What is the Product #? ")
    product = [n for n in products if n["id"] == product_number][0]
    if product:
        print("The product you identified is: ", product)
    else:
        print("That Product # was not found", product)

def create_product():
    print("")
    print("---- CREATING A PRODUCT:")
    print("")

def update_product():
    print("")
    print("---- UPDATING A PRODUCT:")
    print("")

def destroy_product():
    print("")
    print("---- DESTROYING A PRODUCT:")
    print("")

if new_operation == "1": list_products()
elif new_operation == "2": show_product()
elif new_operation == "3": create_product()
elif new_operation == "4": update_product()
elif new_operation == "5": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

# if new_operation == "1": # this is where my code originally started
#    print("")
#    print(" + LISTING PRODUCTS")
# elif new_operation == "2":
#    print("")
#    print(" + SHOWING A PRODUCT")
# elif new_operation == "3":
#    print("")
#    print(" + CREATING A PRODUCT")
# elif new_operation == "4":
#    print("")
#    print(" + UPDATING A PRODUCT")
# elif new_operation == "5":
#    print("")
#    print(" + DESTROYING A PRODUCT")
# else:
#    print("")
#    print(" + OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED COMMANDS.") # this is where my original code ended

print("")

















#command = []

#while True:
#    command = input("Please select a command: ")
#    if new_operation.title == "Quit":
#        break
#    else:
#        new_operation.append(int(csv_file_path))

#def lookup_product_by_id(product_id):
#    matching_products = [product for product in products if product["id"] == product_id]
#    return matching_products[0] # because the line above gives us a list and we want to return a single item.
