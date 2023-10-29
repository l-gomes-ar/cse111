import tkinter as tk
import math

from tkinter import Frame, Label, Button
from number_entry import FloatEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of Circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Radius:"
    lbl_radius = Label(frm_main, text="Radius:")

    # Create a float entry box where the user will enter the radius of circle.
    ent_radius = FloatEntry(frm_main, width=16)

    # Create a label that displays "Area:"
    lbl_area = Label(frm_main, text="Area:")

    # Create labels that will display the results.
    lbl_result = Label(frm_main, width=16)

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Create status bar in case the user types invalid input
    lbl_incorrect = Label(frm_main, text="")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(      row=0, column=0, padx=20, pady=0)
    ent_radius.grid(      row=0, column=1, padx=20, pady=0)

    lbl_area.grid(        row=1, column=0, padx=20, pady=0)
    lbl_result.grid(      row=1, column=1, padx=20, pady=0, columnspan=2)

    btn_clear.grid(       row=2, column=1, padx=20, pady=10, sticky="w")
    lbl_incorrect.grid(   row=3, column=0, padx=0, pady=0, columnspan=4)


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the area of a circle
        by taking the user's radius input and calculating the formula
        """
        try:
            # Get the user's input 'radius'.
            radius = ent_radius.get()

            # Compute the area
            area = math.pi * (radius ** 2)

            # Display the area for the user to see.
            lbl_result.config(text=f"{area:.2f}")

            # Update status bar for user to see.
            if radius <= 0:
                lbl_result.config(text="")
                lbl_incorrect.config(text=f"Invalid input: '{radius:.2f}'. Enter a positive number!")
            else:
                lbl_incorrect.config(text="")


        except ValueError:
            # When the user deletes all the digits in the radius
            # input box, delete content in the result and the status_bar
            lbl_result.config(text="")
            lbl_incorrect.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_radius.clear()
        lbl_result.config(text="")
        ent_radius.focus()

    # Bind the calculate function to the radius entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_radius.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_radius.focus()


# If this file is executed like this:
# > python gui.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
