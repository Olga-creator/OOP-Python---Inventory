# Import libraries
from tabulate import tabulate
import os


# ========The beginning of the class==========
class Shoe:

    # The constructor should initialise country, code, product, cost, quantity
    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # This method will return the cost of the shoes
    def get_cost(self):
        return self.cost

    # This method will return the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # This method will return the code of the shoes
    def get_code(self):
        return self.code

    # This method will return the product
    def get_product(self):
        return self.product

    # This method will return the country of the shoes
    def get_country(self):
        return self.country

    # This method will be used to change the value of the quantity
    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    # This method will return a string representation of a class
    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, " \
               f"Quantity: {self.quantity}"


# The list will be used to store a list of objects of shoes.
shoe_list = []


# ==========Functions outside the class==============
# This function will open the file "inventory.txt" and read the data from the file, then create a shoes object
# and append this object into the shoes list. One line in the file represents data to create one object of shoes.
def read_shoes_data(my_list):

    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()[1:]
            for shoe in lines:
                my_shoe_list = shoe.replace("\n", "").split(",")
                obj = Shoe(my_shoe_list[0], my_shoe_list[1], my_shoe_list[2], my_shoe_list[3], my_shoe_list[4])
                my_list.append(obj)
            return my_shoe_list
    except FileNotFoundError as error:
        print("File doesn't exist.")
        print(error)


# This function called when the user selects 'a' to add new shoe to "inventory.txt" file as well as
# append this object inside the shoe list
def capture_shoes(my_list):

    # Prompt a user for inputs with relevant checks
    while True:
        country_user = input("Enter country: ").capitalize()
        if country_user == "" or country_user.isdigit():
            print("Please enter valid country.\n")
            continue
        else:
            break

    while True:
        code_user = input("Enter code: ")
        if code_user == "" or not code_user.startswith("SKU"):
            print("Please enter valid code.\n")
            continue
        else:
            break

    while True:
        product_user = input("Enter product: ")
        if product_user == "":
            print("Please enter valid product.\n")
            continue
        else:
            break

    while True:
        try:
            cost_user = int(input("Enter cost: "))
            break
        except ValueError:
            print("Incorrect cost. Try again!\n")
            continue

    while True:
        try:
            quantity_user = int(input("Enter quantity: "))
            break
        except ValueError:
            print("Incorrect quantity. Try again!\n")
            continue

    obj_user = Shoe(country_user, code_user, product_user, cost_user, quantity_user)
    my_list.append(obj_user)

    with open("inventory.txt", "a+") as file:
        file.write(f"\n{country_user},{code_user},{product_user},{cost_user},{quantity_user}")

    print("\nThe product had been added to the inventory list.\n")


# This function called when the user selects 'va' to read all the shoes listed in 'inventory.txt' and
# print to the console in a table format by using Python’s tabulate module
def view_all(my_list):

    table = []

    for shoe in my_list:
        table.append([shoe.get_country(), shoe.get_code(), shoe.get_product(), shoe.get_cost(), shoe.get_quantity()])
    print(tabulate(table, headers=('Country', 'Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid'))
    print()


# This function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked.
# The user will be asked if they want to add this quantity of shoes and then update it.
def re_stock(my_list):

    table = []
    min_shoe = None

    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()[1:]
            for line in lines:
                val = int(line.split(",")[4])
                if min_shoe is None or val < min_shoe:
                    min_shoe = val

            print("\t\tTHIS SHOE HAS THE LOWEST QUANTITY:")
            for item in my_list:
                if min_shoe == int(item.get_quantity()):
                    table.append([item.get_country(), item.get_code(), item.get_product(), item.get_cost(),
                                  item.get_quantity()])
                    print(tabulate(table, headers=('Country', 'Code', 'Product', 'Cost', 'Quantity', 'Value'),
                                   tablefmt='fancy_grid'))

                    # Prompt the user if they want to add this quantity of shoes and then update it
                    question = input("\nWould you like to add this quantity of shoes? (Yes / No) ").lower()
                    if question == 'y' or question == 'Yes':
                        while True:
                            try:
                                re_stocked = int(input("Enter new quantity: "))
                                item.set_quantity(re_stocked)
                                print("\nThe quantity has been successfully updated!\n")
                                break
                            except ValueError:
                                print("Invalid quantity. Try again!\n")
                                continue
                    else:
                        print()
                        pass

        # Update quantity in the "inventory.txt" file
        with open("inventory.txt", "w") as file1:
            file1.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in my_list:
                file1.write(f"{shoe.get_country()},{shoe.get_code()},{shoe.get_product()},"
                            f"{shoe.get_cost()},{shoe.get_quantity()}\n")

    except FileNotFoundError:
        print("")


# This function will search for a shoe from the list using the shoe code
# and return this object so that it will be printed
def search_shoe(my_list):

    table = []

    user_code = input("\nEnter code: ")
    for shoe in my_list:
        if user_code == shoe.get_code():
            table.append([shoe.get_country(), shoe.get_code(), shoe.get_product(), shoe.get_cost(),
                          shoe.get_quantity()])
            print(tabulate(table, headers=('Country', 'Code', 'Product', 'Cost', 'Quantity', 'Value'),
                           tablefmt='fancy_grid'))
    print()


# This function will calculate the total value for each item and display this on the console for all the shoes
def value_per_item():

    table1 = []
    table2 = []

    for shoe in shoe_list:
        value = int(shoe.get_cost()) * int(shoe.get_quantity())
        table1.append([shoe.get_country(), shoe.get_code(), shoe.get_product(), shoe.get_cost(), shoe.get_quantity()])
        table2.append(value)

    # Ref: Append to a List in Python – Nested Lists
    # https://www.askpython.com/python/list/append-to-a-list-in-python
    for row, item in enumerate(table1):
        item.append(table2[row])

    print(tabulate(table1, headers=('Country', 'Code', 'Product', 'Cost', 'Quantity', 'Value'), tablefmt='fancy_grid'))
    print()


# This function will determine the product with the highest quantity and display this shoe as being for sale
def highest_qty(my_list):

    table = []
    max_num = 0

    with open('inventory.txt', 'r') as data:
        lines = data.readlines()[1:]
        for shoe in lines:
            val = int(shoe.split(",")[4])
            if val > max_num:
                max_num = val

    print("\t\t\t\tTHIS SHOE IS FOR SALE:")
    for item in my_list:
        if max_num == int(item.get_quantity()):
            table.append([item.get_country(), item.get_code(), item.get_product(), item.get_cost(),
                          item.get_quantity()])
            print(tabulate(table, headers=('Country', 'Code', 'Product', 'Cost', 'Quantity', 'Value'),
                           tablefmt='fancy_grid'))
    print()


# ==========Main Menu=============
# Create a menu that executes each function above

read_shoes_data(shoe_list)

while True:
    # Menu will only be displayed if text file "inventory.txt" exists, otherwise only error message will be shown
    if os.path.isfile("inventory.txt"):

        menu = input("""Select one of the following options below:
a -  Add new shoes
va - View all shoes
r -  Re-stock 
s -  Search shoes by code
vv - View Items value
h -  View items for sale
e -  Exit
: """).lower()

        if menu == "a":
            capture_shoes(shoe_list)
            continue

        elif menu == "va":
            view_all(shoe_list)
            continue

        elif menu == "r":
            re_stock(shoe_list)
            continue

        elif menu == "s":
            search_shoe(shoe_list)
            continue

        elif menu == "vv":
            value_per_item()
            continue

        elif menu == "h":
            highest_qty(shoe_list)
            continue

        elif menu == "e":
            print("Goodbye!!!")
            exit()

        else:
            print("\nThis option is not valid. Try again.\n")
            continue
