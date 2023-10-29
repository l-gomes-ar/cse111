import csv


def main():
    NAME_INDEX = 1
    
    # Call read_dictionary store dictionary in a variable
    students = read_dictionary("students.csv", 0)

    # Get I-Number from user
    i_number = input("I-Number (70-000-0000) or (700000000): ")

    i_number = i_number.replace("-", "")

    # Check for I-Number's length
    if len(i_number) < 9:
        print("Invalid I-Number: too few digits")
    elif len(i_number) > 9:
        print("Invalid I-Number: too many digits")
    else:
        # For character in I-Number
        for char in i_number:
            # Check if character is not a digit
            if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                 # Print message and break
                print("Invalid I-Number")

                break

        # Check if I-Number in dictionary
        if i_number in students:
            # Get student name from students dictionary
            # by using the key (I-Number) and the index 
            # for name (1)
            name = students[i_number][NAME_INDEX]

            print(name)
        else:
            print("No such student!")


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

    # Open students.csv
    with open(filename, "rt") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:            
            # Get key for the dictionary
            dictionary[row[key_column_index]] = row
        
    return dictionary


# Call main
if __name__ == "__main__":
    main()