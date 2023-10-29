# Exceeding Requirements: Added code to discount products prices by 10% if the current day is
# Tuesday or Wednesday or the current time of day is before 11:00 a.m, and display the discount 
# and reason for it.

import csv
import sys

from datetime import datetime


def main():
    PRODUCT_NUM_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2

    QUANTITY_INDEX = 1

    # Call read_dictionary and store the compound 
    # dictionary in a variable
    products_list = read_dictionary("products.csv", PRODUCT_NUM_INDEX)

    # Get current date and time
    current_date_time = datetime.now()
    
    # Print the store name
    print("Inkom Emporium")
    print()
    
    # Open "request.csv" for reading and printing info for all requested items
    try:
        with open("request.csv", "rt") as file:
            # Get reader object to read file
            reader = csv.reader(file)

            # Skip headings
            next(reader)

            # Create variable to store number of items,
            # subtotal price, sales tax rate, sales tax,
            # discount_day and discount_time
            n_items = 0
            subtotal = 0

            for row in reader:
                # Use product number to find the corresponding item in dict
                item = products_list[row[PRODUCT_NUM_INDEX]]

                # Retrieve and print the product name, requested quantity, and price
                product_name = item[NAME_INDEX]
                quantity = int(row[QUANTITY_INDEX])
                price = float(item[PRICE_INDEX])

                # Add quantity to the number of items
                n_items += quantity
                
                # Multiply price by quantity and add to the subtotal
                subtotal += price * quantity

                print(f"{product_name}: {quantity} @ {price}")

    except FileNotFoundError as f_err:
        print("Error: missing file")
        print(f_err)
        sys.exit(1)

    except PermissionError as p_err:
        print("Error: you do not have permission to access this file")
        print(p_err)
        sys.exit(1)
    
    except KeyError as k_err:
        print("Error: unknown product ID in the request.csv file")
        print(k_err)
        sys.exit(1)

    # Print new line
    print()

    # Create variable to store sales tax rate and discount
    TAX_RATE = .06
    discount = 0

    # If the current day is Tuesday (1) or Wednesday (2)
    # or if current time of day is before 11:00 am
    # discount 10% from subtotal
    if current_date_time.weekday() in [1, 2] or int(f"{current_date_time:%H}") < 11:
        discount = subtotal * .1
        subtotal -= discount

    # Compute sales tax amount
    sales_tax = subtotal * TAX_RATE

    # Print number of items
    print(f"Number of Items: {n_items}")

    # Print subtotal
    print(f"Subtotal: {subtotal:.2f}")

    # Print Sales Tax
    print(f"Sales Tax: {sales_tax:.2f}")

    # Print Total
    print(f"Total: {(subtotal + sales_tax):.2f}")

    print()

    # Check if there is any discount because of the current weekday
    if discount:
        print("Because today is either Tuesday or Wednesday,")
        print("or because the current time of day is before 11:00 a.m,")
        print("your product prices were discounted by 10%")
        print()

        print(f"Total Products Savings: {discount:.2f}")
        print()

    # Print gratitute message and date and time of purchase
    # using the ctime method
    print("Thank you for shopping at the Inkom Emporium.")
    print(current_date_time.ctime())


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    # Read contents of a CSV file
    try:
        with open(filename, "rt") as file:
            # Use csv reader for accessing the CSV file as a list
            reader = csv.reader(file)

            # Skip the headings line
            next(reader)

            # Iterate through rows in the reader object
            for row in reader:

                # Check row isn't empty
                if len(row):
                    # Set key for each row in dictionary
                    # and add this row list as its value
                    dictionary[row[key_column_index]] = row

    except FileNotFoundError as f_err:
        print("Error: missing file")
        print(f_err)
        sys.exit(1)

    except PermissionError as p_err:
        print("Error: you do not have permission to access this file")
        print(p_err)
        sys.exit(1)

    # Return dictionary
    return dictionary


# Call main
if __name__ == "__main__":
    main()
