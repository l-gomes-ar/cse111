# Reads from the keyboard the three numbers for a tire, computes and outputs the volume of space inside that tire,
# shows approximate price range for tire, stores phone number of user if they wish to buy. Writes down all info in "volumes.txt"

from datetime import datetime
from math import pi


# Get valid input from user
while True:
    try:
        w = float(input("Enter the width of the tire in mm (ex 205): "))
        a = float(input("Enter the aspect ratio of the tire (ex 60): "))
        d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

        # If all values are valid, break
        break

    except ValueError:
        print("Ensure the values are numbers!")

print()

# Store the tire_size
tire_size = f"{w:.0f}/{a:.0f} R{d:.0f}"

# Create list of common tire sizes with the same price range
common_tire_sizes_1 = [
    "165/70 R14", "175/65 R15", "185/65 R15", "195/60 R15", "195/65 R15", "205/55 R16"
]

common_tire_sizes_2 = [
    "215/55 R17", "225/60 R18", "225/65 R17", "235/60 R18", "245/45 R19"
]

common_tire_sizes_3 = [
    "225/65 R17", "265/70 R17"
]

# Display the approximate price range for the tires
print("The approximate price range for these tires is:", end=" ")

if tire_size in common_tire_sizes_1:
    print("$62 - $250")
elif tire_size == "205/60 R15":
    print("$85 - $150")
elif tire_size == "215/55 R16":
    print("$70 - $220")
elif tire_size in common_tire_sizes_2:
    print("$62.99 - $239.93")
elif tire_size in common_tire_sizes_3:
    print("$100 - $200")
elif tire_size == "225/45 R17":
    print("$75 - $273")
elif tire_size == "225/40 R18":
    print("$86 - $285")
else:
    print("I am sorry. We do not have data for the approximate price range for these tires!")

# Calculate volume
volume = round((pi * w ** 2 * a * (w * a + 2540 * d)) / (10 ** 10), 2)

# Output the volume of space inside that tire
print(f"The approximate volume is {volume} liters")

# Ask user if they want to buy these tires
buy_tires = input(f"Do you want to buy tires with the dimensions ({tire_size}) entered [yes / no]? ")

if buy_tires == "yes":
    phone = input("Please enter your phone number: ")

current_date_time = datetime.now()

with open("volumes.txt", "at") as f:
    # Catch error if phone is not defined when writing to volumes.txt
    try:
        print(f"{current_date_time:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {volume}, Phone number: {phone}", file=f)

    except NameError:
        print(f"{current_date_time:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {volume}", file=f)
    