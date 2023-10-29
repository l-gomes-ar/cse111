# Uses tkinter's GUI to create an aviation toolkit program that performs common calculations
# in aviation and conversion between different units. 

import tkinter as tk
from functools import partial
from math import cos, pi, radians, sin
from numpy import arctan
from tkinter import ttk


def main():
    # Define the root window, and main frame
    root = tk.Tk()

    # Set width and height for the Tk root
    w = 300 
    h = 450 

    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    frm_main = ttk.Frame(root, padding=10)
    frm_main.master.title("Aviation Toolkit")

    # Specify the layout of the frame in the root window as pack
    frm_main.pack()

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main, root)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def populate_main_window(frm_main, root):
    """Populates the main window with buttons for various calculations and conversions.

    Parameters:
        frm_main (Frame): The main frame to populate.
        root (Tk): The root Tkinter object.

    Returns:
        None
    """
    # Create widgets, buttons for options
    lbl_title = ttk.Label(frm_main, text="Flight Calculator")

    btn_dead_reckoning = ttk.Button(frm_main, text="Dead Reckoning Calculation", command=lambda: create_toplevel_window("btn_dead_reckoning"))
    btn_true_airspeed = ttk.Button(frm_main, text="True Airspeed Calculation", command=lambda: create_toplevel_window("btn_true_airspeed"))
    btn_groundspeed = ttk.Button(frm_main, text="Groudspeed Calculation", command=lambda: create_toplevel_window("btn_groundspeed"))
    btn_off_course = ttk.Button(frm_main, text="Off Course Correction", command=lambda: create_toplevel_window("btn_off_course"))
    btn_fuel_consumption = ttk.Button(frm_main, text="Fuel Consumption Endurance", command=lambda: create_toplevel_window("btn_fuel_consumption"))
    btn_rate_descent = ttk.Button(frm_main, text="Rate of Descent Calculation", command=lambda: create_toplevel_window("btn_rate_descent"))
    btn_toa = ttk.Button(frm_main, text="Time of Arrival Calculation", command=lambda: create_toplevel_window("btn_toa"))
    btn_distance_traveled = ttk.Button(frm_main, text="Distance Traveled Calculation", command=lambda: create_toplevel_window("btn_distance_traveled"))
    btn_tod = ttk.Button(frm_main, text="Top of Descent Calculation", command=lambda: create_toplevel_window("btn_tod"))
    btn_convert = ttk.Button(frm_main, text="Unit Converter", command=lambda: create_toplevel_window("btn_convert"))

    btn_close = ttk.Button(frm_main, text="Close", command=root.destroy)

    # Position them in the window
    lbl_title.grid(row=0, pady=10)

    btn_dead_reckoning.grid(row=1)
    btn_true_airspeed.grid(row=2)
    btn_groundspeed.grid(row=3)
    btn_off_course.grid(row=4)
    btn_fuel_consumption.grid(row=5)
    btn_rate_descent.grid(row=6)
    btn_tod.grid(row=7)
    btn_distance_traveled.grid(row=8)
    btn_toa.grid(row=9)
    btn_convert.grid(row=10)

    btn_close.grid(row=12, pady=20)


def create_toplevel_window(button_clicked):
    """Creates a new top-level window and populates it based on the button clicked.

    Parameters:
        button_clicked (str): The name of the button that was clicked.

    Returns:
        None
    """
    # Define the top level window and geometry
    toplevel = tk.Toplevel()

    # Set width and height for the Tk toplevel window
    w = 300 
    h = 450 

    # get screen width and height
    ws = toplevel.winfo_screenwidth()
    hs = toplevel.winfo_screenheight()

    # calculate x and y coordinates for the Tk toplevel window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    toplevel.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Define a frame for this top level window 
    frm_toplevel = ttk.Frame(toplevel, padding=10)

    # Specify layout for the new frame
    frm_toplevel.pack()

    # Create mapping for calling a function depending 
    # on the button clicked.
    populate_functions = {
        "btn_dead_reckoning": populate_dead_rec_window,
        "btn_true_airspeed": populate_true_airspeed_window,
        "btn_groundspeed": populate_groundspeed_window,
        "btn_off_course": populate_off_course_correction_window,
        "btn_fuel_consumption": populate_fuel_consumption_window,
        "btn_rate_descent": populate_rate_descent_window,
        "btn_tod": populate_tod_window,
        "btn_toa": populate_toa_window,
        "btn_distance_traveled": populate_distance_traveled_window,
        "btn_convert": populate_convert_window,
        "btn_cels_fahr": populate_cels_fahr_window,
        "btn_nautical_stature": populate_nautical_mi_window,
        "btn_nautical_km": populate_nautical_km_window,
        "btn_gallons_l": populate_gallons_l_window,
        "btn_pounds_kg": populate_pounds_kg_window,
        "btn_ft_m": populate_ft_m_window,
        "btn_inhg_mb": populate_inhg_mb_window,
        "btn_h_m_s_decimal_h": populate_h_m_s_decimal_h_window,
    }

    # Populate the appropriate window according to the button clicked
    if button_clicked in populate_functions:
        populate_functions[button_clicked](frm_toplevel)


def populate_dead_rec_window(frame):
    """Populates a window for dead reckoning calculation.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and place on grid
    lbl_title = ttk.Label(frame, text="Dead Reckoning Calculation").grid(row=0, pady=10, columnspan=2)

    # Create variable labels to store the labels for the entry boxes on window
    labels = [
        "Course (in degrees)",
        "Last Known Latitude (in degrees)",
        "Last Known Longitude (in degrees)",
        "Speed (in knots)",
        "Time (in minutes)"
    ]

    # Call populate_window, and save the return dict in a variable called widgets
    widgets = populate_window(frame, 5, labels)
    
    def calculate():
        # Get all the values from widgets
        try:
            course = float(widgets['ent_0'].get())
            latitude = float(widgets['ent_1'].get())
            longitude = float(widgets['ent_2'].get())
            speed = float(widgets['ent_3'].get())
            time = float(widgets['ent_4'].get())
            
            # Calculate Dead Reckoning and show it to the user
            values = calculate_dead_reckoning(course, latitude, longitude, speed, time)
            latitude = values['latitude']
            longitude = values['longitude']

            widgets['lbl_result'].config(text=f"Latitude: {latitude:.6f}\nLongitude: {longitude:.6f}")         

        except ValueError:
            # Show user a message saying that values should be numbers
            widgets['lbl_result'].config(text="Only numbers allowed in the input boxes!")

            # Delete all entry boxes
            widgets['ent_0'].delete(0, tk.END)
            widgets['ent_1'].delete(0, tk.END)
            widgets['ent_2'].delete(0, tk.END)
            widgets['ent_3'].delete(0, tk.END)
            widgets['ent_4'].delete(0, tk.END)

    def clear():
        # Delete all entry boxes, and result label
        widgets['ent_0'].delete(0, tk.END)
        widgets['ent_1'].delete(0, tk.END)
        widgets['ent_2'].delete(0, tk.END)
        widgets['ent_3'].delete(0, tk.END)
        widgets['ent_4'].delete(0, tk.END)

        widgets['lbl_result'].config(text="")

    # Assign calculate and clean to their respective buttons
    widgets['btn_calculate'].config(command=calculate)
    widgets['btn_clear'].config(command=clear)


def populate_true_airspeed_window(frame):
    """Populates a window for true airspeed calculation.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and place on grid
    lbl_title = ttk.Label(frame, text="True Airspeed Calculation").grid(row=0, pady=10, columnspan=2)

    # Create variable labels to store the labels for the entry boxes on window
    labels = [
        "Altitude (in feet)",
        "Equivalent Airspeed (in knots)"
    ]

    # Call populate_window, and save the return dict in a variable called widgets
    widgets = populate_window(frame, 2, labels)

    def calculate():
        # Get all the values from widgets
        try:
            altitude = float(widgets['ent_0'].get())
            equivalent_airspeed = float(widgets['ent_1'].get())

            if altitude < 0 or equivalent_airspeed < 0:
                raise ValueError

            tas = calculate_true_airspeed(altitude, equivalent_airspeed)
                    
            # Calculate True Airspeed and show it to the user
            widgets['lbl_result'].config(text=f"Approx. True Airspeed: {tas:.2f} kt")         

        except ValueError:
            # Show user a message saying that values should be numbers
            widgets['lbl_result'].config(text="Only numbers allowed in the input boxes! (And only positive numbers allowed for Equivalent Airspeed!)")

            # Delete all entry boxes
            widgets['ent_0'].delete(0, tk.END)
            widgets['ent_1'].delete(0, tk.END)

    def clear():
        # Delete all entry boxes, and result label
        widgets['ent_0'].delete(0, tk.END)
        widgets['ent_1'].delete(0, tk.END)

        widgets['lbl_result'].config(text="")

    # Assign calculate and clean to their respective buttons
    widgets['btn_calculate'].config(command=calculate)
    widgets['btn_clear'].config(command=clear)


def populate_groundspeed_window(frame):
    """Populates a window for ground speed calculation.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and place on grid
    lbl_title = ttk.Label(frame, text="Groundspeed Calculation").grid(row=0, pady=10, columnspan=2)

    # Create variable labels to store the labels for the entry boxes on window
    labels = [
        "True Airspeed (in knots)",
        "Wind Speed (in knots)",
        "Wind Direction (in knots)",
        "Aircraft Direction (in degrees)"
    ]

    # Call populate_window, and save the return dict in a variable called widgets
    widgets = populate_window(frame, 4, labels)

    def calculate():
        # Get all the values from widgets
        try:
            tas = float(widgets['ent_0'].get())
            wind_speed = float(widgets['ent_1'].get())
            wind_direction = float(widgets['ent_2'].get())
            aircraft_direction = float(widgets['ent_3'].get())

            if wind_speed < 0 or tas < 0 or wind_direction < 0 or aircraft_direction < 0:
                raise ValueError
            
            groundspeed = calculate_ground_speed(tas, wind_speed, wind_direction, aircraft_direction)

            # Calculate Groundspeed and show it to the user
            widgets['lbl_result'].config(text=f"Ground Speed: {groundspeed:.2f} knots")         

        except ValueError:
            # Show user a message saying that values should be numbers
            widgets['lbl_result'].config(text="Only positive numbers allowed in the input boxes!")

            # Delete all entry boxes
            widgets['ent_0'].delete(0, tk.END)
            widgets['ent_1'].delete(0, tk.END)
            widgets['ent_2'].delete(0, tk.END)
            widgets['ent_3'].delete(0, tk.END)

    def clear():
        # Delete all entry boxes, and result label
        widgets['ent_0'].delete(0, tk.END)
        widgets['ent_1'].delete(0, tk.END)
        widgets['ent_2'].delete(0, tk.END)
        widgets['ent_3'].delete(0, tk.END)

        widgets['lbl_result'].config(text="")

    # Assign calculate and clean to their respective buttons
    widgets['btn_calculate'].config(command=calculate)
    widgets['btn_clear'].config(command=clear)


def populate_off_course_correction_window(frame):
    """Populates a window for off course correction calculation.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and position it
    lbl_title = ttk.Label(frame, text="Off Course Heading Correction").grid(row=0, pady=10, columnspan=2)

    # Create variable labels to store the labels for the entry boxes on window
    labels = [
        "Distance Off Course (in NM)",
        "Distance Flown (in NM)",
        "Distance Remaining (in NM)"
    ]

    # Call populate_window, and save the return dict in a variable called widgets
    widgets = populate_window(frame, 3, labels)

    def calculate():
        # Get all the values from widgets
        try:
            off_course = float(widgets['ent_0'].get())
            flown = float(widgets['ent_1'].get())
            remaining = float(widgets['ent_2'].get())

            if off_course < 0 or flown < 0 or remaining < 0:
                raise ValueError
            
            # Calculate Off Course Correction and show it to the user
            correction = calculate_off_course_correction(off_course, flown, remaining)

            widgets['lbl_result'].config(text=f"Total Heading Correction: {correction:.2f}°")         

        except ValueError:
            # Show user a message saying that values should be positive numbers
            widgets['lbl_result'].config(text="Only positive numbers allowed in the input boxes!")

            # Delete all entry boxes
            widgets['ent_0'].delete(0, tk.END)
            widgets['ent_1'].delete(0, tk.END)
            widgets['ent_2'].delete(0, tk.END)

    def clear():
        # Delete all entry boxes, and result label
        widgets['ent_0'].delete(0, tk.END)
        widgets['ent_1'].delete(0, tk.END)
        widgets['ent_2'].delete(0, tk.END)

        widgets['lbl_result'].config(text="")

    # Assign calculate and clean to their respective buttons
    widgets['btn_calculate'].config(command=calculate)
    widgets['btn_clear'].config(command=clear)


def populate_fuel_consumption_window(frame):
    """Populates a window for fuel consumption endurance calculation.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and position it
    lbl_title = ttk.Label(frame, text="Fuel Consumption Endurance Calculation").grid(row=0, pady=10, columnspan=2)

    # Create variable labels to store the labels for the entry boxes on window
    labels = [
        "Total Amount Fuel (in gallons)",
        "Average Fuel Burn Per Hour (in gallons/hr)"
    ]

    # Call populate_window, and save the return dict in a variable called widgets
    widgets = populate_window(frame, 2, labels)

    def calculate():
        # Get all the values from widgets
        try:
            amount_fuel = float(widgets['ent_0'].get())
            average = float(widgets['ent_1'].get())

            if amount_fuel < 0 or average < 0:
                raise ValueError
            

            # Calculate Fuel Consumption Endurance and show it to the user
            endurance = calculate_fuel_endurance(amount_fuel, average)

            widgets['lbl_result'].config(text=f"Aircraft Endurance: {endurance:.2f} hours")         

        except ValueError:
            # Show user a message saying that values should be positive numbers
            widgets['lbl_result'].config(text="Only positive numbers allowed in the input boxes!")

            # Delete all entry boxes
            widgets['ent_0'].delete(0, tk.END)
            widgets['ent_1'].delete(0, tk.END)

    def clear():
        # Delete all entry boxes, and result label
        widgets['ent_0'].delete(0, tk.END)
        widgets['ent_1'].delete(0, tk.END)

        widgets['lbl_result'].config(text="")

    # Assign calculate and clean to their respective buttons
    widgets['btn_calculate'].config(command=calculate)
    widgets['btn_clear'].config(command=clear)


def populate_rate_descent_window(frame):
    """Populates a window for rate descent calculation.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and position it
    lbl_title = ttk.Label(frame, text="Rate of Descent Calculation").grid(row=0, pady=10, columnspan=2)

    # Create variable labels to store the labels for the entry boxes on window
    labels = [
        "Ground Speed (in knots)"
    ]

    # Call populate_window, and save the return dict in a variable called widgets
    widgets = populate_window(frame, 1, labels)

    def calculate():
        # Get all the values from widgets
        try:
            groundspeed = float(widgets['ent_0'].get())

            if groundspeed < 0:
                raise ValueError
            

            # Calculate Rate of Descent and show it to the user
            rate_descent = calculate_rate_descent(groundspeed)

            widgets['lbl_result'].config(text=f"Rate of Descent: {rate_descent:.2f} ft/min for 3° descent angle")         

        except ValueError:
            # Show user a message saying that values should be positive numbers
            widgets['lbl_result'].config(text="Only positive numbers allowed in the input boxes!")

            # Delete all entry boxes
            widgets['ent_0'].delete(0, tk.END)

    def clear():
        # Delete all entry boxes, and result label
        widgets['ent_0'].delete(0, tk.END)

        widgets['lbl_result'].config(text="")

    # Assign calculate and clean to their respective buttons
    widgets['btn_calculate'].config(command=calculate)
    widgets['btn_clear'].config(command=clear)


def populate_tod_window(frame):
    """Populates a window for top of descent calculation.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and position it
    lbl_title = ttk.Label(frame, text="Top of Descent Calculation").grid(row=0, pady=10, columnspan=2)

    # Create variable labels to store the labels for the entry boxes on window
    labels = [
        "Current Altitude (in feet)",
        "Airfield Altitude (in feet)",
        "Rate of Descent (in ft/min)",
        "Ground Speed (in knots)"
    ]

    # Call populate_window, and save the return dict in a variable called widgets
    widgets = populate_window(frame, 4, labels)

    def calculate():
        # Get all the values from widgets
        try:
            current_altitude = float(widgets['ent_0'].get())
            altitude_airfield = float(widgets['ent_1'].get())
            rate_descent = float(widgets['ent_2'].get())
            groundspeed = float(widgets['ent_3'].get())

            if current_altitude < 0 or altitude_airfield < 0 or rate_descent < 0 or groundspeed < 0 or altitude_airfield > current_altitude:
                raise ValueError
            
            # Calculate Top of Descent and show it to the user
            tod = calculate_tod(current_altitude, altitude_airfield, rate_descent, groundspeed)

            widgets['lbl_result'].config(text=f"Distance to Start Descent: {tod:.2f} NM")         

        except ValueError:
            # Show user a message saying that values should be positive numbers
            widgets['lbl_result'].config(text="Only positive numbers allowed in the input boxes! Airfield Altitude should not be greater than current altitude!")

            # Delete all entry boxes
            widgets['ent_0'].delete(0, tk.END)
            widgets['ent_1'].delete(0, tk.END)
            widgets['ent_2'].delete(0, tk.END)
            widgets['ent_3'].delete(0, tk.END)

    def clear():
        # Delete all entry boxes, and result label
        widgets['ent_0'].delete(0, tk.END)
        widgets['ent_1'].delete(0, tk.END)
        widgets['ent_2'].delete(0, tk.END)
        widgets['ent_3'].delete(0, tk.END)

        widgets['lbl_result'].config(text="")

    # Assign calculate and clean to their respective buttons
    widgets['btn_calculate'].config(command=calculate)
    widgets['btn_clear'].config(command=clear)


def populate_distance_traveled_window(frame):
    """Populates a window for distance traveled calculation.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and position it
    lbl_title = ttk.Label(frame, text="Distance Traveled Calculation").grid(row=0, pady=10, columnspan=2)


    # Create variable labels to store the labels for the entry boxes on window
    labels = [
        "Speed (in knots)",
        "Time Flying (in min)"
    ]

    # Call populate_window, and save the return dict in a variable called widgets
    widgets = populate_window(frame, 2, labels)

    def calculate():
        # Get all the values from widgets
        try:
            speed = float(widgets['ent_0'].get())
            time = float(widgets['ent_1'].get())

            if speed < 0 or time < 0:
                raise ValueError
            
            # Calculate Distance Traveled and show it to the user
            distance = calculate_distance_traveled(speed, time)

            widgets['lbl_result'].config(text=f"Distance Traveled: {distance:.2f} NM")         

        except ValueError:
            # Show user a message saying that values should be positive numbers
            widgets['lbl_result'].config(text="Only positive numbers allowed in the input boxes! Airfield Altitude should not be greater than current altitude!")

            # Delete all entry boxes
            widgets['ent_0'].delete(0, tk.END)
            widgets['ent_1'].delete(0, tk.END)

    def clear():
        # Delete all entry boxes, and result label
        widgets['ent_0'].delete(0, tk.END)
        widgets['ent_1'].delete(0, tk.END)

        widgets['lbl_result'].config(text="")

    # Assign calculate and clean to their respective buttons
    widgets['btn_calculate'].config(command=calculate)
    widgets['btn_clear'].config(command=clear)


def populate_toa_window(frame):
    """Populates a window for estimated time of arrival calculation.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create labels and buttons
    lbl_title = ttk.Label(frame, text="Time of Arrival Calculation").grid(row=0, pady=10, columnspan=2)

    # Create variable labels to store the labels for the entry boxes on window
    labels = [
        "Remaining Distance (in NM)",
        "Ground Speed (in knots)"
    ]

    # Call populate_window, and save the return dict in a variable called widgets
    widgets = populate_window(frame, 2, labels)

    def calculate():
        # Get all the values from widgets
        try:
            distance = float(widgets['ent_0'].get())
            groundspeed = float(widgets['ent_1'].get())

            if distance < 0 or groundspeed < 0:
                raise ValueError
            
            # Calculate Time of Arrival and show it to the user
            toa = calculate_toa(distance, groundspeed)

            widgets['lbl_result'].config(text=f"Estimated Time of Arrival: {toa:.2f} min")         

        except ValueError:
            # Show user a message saying that values should be positive numbers
            widgets['lbl_result'].config(text="Only positive numbers allowed in the input boxes! Airfield Altitude should not be greater than current altitude!")

            # Delete all entry boxes
            widgets['ent_0'].delete(0, tk.END)
            widgets['ent_1'].delete(0, tk.END)

    def clear():
        # Delete all entry boxes, and result label
        widgets['ent_0'].delete(0, tk.END)
        widgets['ent_1'].delete(0, tk.END)

        widgets['lbl_result'].config(text="")

    # Assign calculate and clean to their respective buttons
    widgets['btn_calculate'].config(command=calculate)
    widgets['btn_clear'].config(command=clear)


def populate_convert_window(frame):
    """Populates the unit converter frame with
    the appropriate labels(lbl), buttons(btn),
    and entry boxes (ent) widgets.

    Parameter
        frame: The top level frame to populate
    Return: nothing
    """
    # Create labels and buttons
    lbl_title = ttk.Label(frame, text="Unit Converter")

    btn_cels_fahr = ttk.Button(frame, text="Celsius to Fahrenheit", command=lambda: create_toplevel_window("btn_cels_fahr"))
    btn_nautical_stature = ttk.Button(frame, text="Nautical Miles to Stature Miles", command=lambda: create_toplevel_window("btn_nautical_stature"))
    btn_nautical_km = ttk.Button(frame, text="Nautical Miles to Kilometers", command=lambda: create_toplevel_window("btn_nautical_km"))
    btn_gallons_l = ttk.Button(frame, text="Gallons to Liters", command=lambda: create_toplevel_window("btn_gallons_l"))
    btn_pounds_kg = ttk.Button(frame, text="Pounds to Kilograms", command=lambda: create_toplevel_window("btn_pounds_kg"))
    btn_ft_m = ttk.Button(frame, text="Feet to Meters", command=lambda: create_toplevel_window("btn_ft_m"))
    btn_inhg_mb = ttk.Button(frame, text="Inches of Mercury (inHg) to Milibars (mb)", command=lambda: create_toplevel_window("btn_inhg_mb"))
    btn_h_m_s_decimal_h = ttk.Button(frame, text="Hours:Minutes:Second to Decimal Hours", command=lambda: create_toplevel_window("btn_h_m_s_decimal_h"))

    btn_close = ttk.Button(frame, text="Go Back", command=frame.master.destroy)

    # Place labels and buttons on grid
    lbl_title.grid(row=0, pady=10)
                                 
    btn_cels_fahr.grid(row=1)
    btn_nautical_stature.grid(row=2)
    btn_nautical_km.grid(row=3)
    btn_gallons_l.grid(row=4)
    btn_pounds_kg.grid(row=5)
    btn_ft_m.grid(row=6)
    btn_inhg_mb.grid(row=7)
    btn_h_m_s_decimal_h.grid(row=8)

    btn_close.grid(row=18, pady=9)


# Define each populate window for the windows in convert units,
# and then, calculate the conversions inside each function 
def populate_cels_fahr_window(frame):
    """Populates a window for converting between Celsius and Fahrenheit.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and place it on grid
    ttk.Label(frame, text="Conversion Celsius to Fahrenheit and Viceversa", wraplength=200, justify="center").grid(row=0, pady=10)

    # Call populate_generic_window to set up the specifics of this GUI, including the convert functions necessary
    populate_generic_convert_window(frame, "\u00b0C", "\u00b0F", check_dash=True, convert_function1=convert_celsius_fahrenheit, convert_function2=convert_fahrenheit_celsius)
    

def populate_nautical_mi_window(frame):
    """Populates a window for converting between nautical miles and statute miles.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and place it on grid
    ttk.Label(frame, text="Conversion Nautical Miles to Stature Miles and Viceversa", wraplength=200, justify="center").grid(row=0, pady=10)

    # Call populate_generic_window to set up the specifics of this GUI, including the convert functions necessary
    populate_generic_convert_window(frame, "NM", "mi", check_positive_n=True, convert_function1=convert_naut_mi, convert_function2=convert_mi_naut)


def populate_nautical_km_window(frame):
    """Populates a window for converting between nautical miles and kilometers.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and place it on grid
    ttk.Label(frame, text="Conversion Nautical Miles to Kilometers and Viceversa", wraplength=200, justify="center").grid(row=0, pady=10)

    # Call populate_generic_window to set up the specifics of this GUI, including the convert functions necessary
    populate_generic_convert_window(frame, "NM", "km", check_positive_n=True, convert_function1=convert_naut_km, convert_function2=convert_km_naut)


def populate_gallons_l_window(frame):
    """Populates a window for converting between gallons and liters.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and place it on grid
    ttk.Label(frame, text="Conversion Gallons to Liters and Viceversa", wraplength=200, justify="center").grid(row=0, pady=10)

    # Call populate_generic_window to set up the specifics of this GUI, including the convert functions necessary
    populate_generic_convert_window(frame, "gal", "L", check_positive_n=True, convert_function1=convert_gallons_liters, convert_function2=convert_liters_gallons)


def populate_pounds_kg_window(frame):
    """Populates a window for converting between pounds and kilograms.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and place it on grid
    ttk.Label(frame, text="Conversion Pounds to Kilograms and Viceversa", wraplength=200, justify="center").grid(row=0, pady=10)

    # Call populate_generic_window to set up the specifics of this GUI, including the convert functions necessary
    populate_generic_convert_window(frame, "lb", "kg", check_positive_n=True, convert_function1=convert_pounds_kg, convert_function2=convert_kg_pounds)


def populate_ft_m_window(frame):
    """Populates a window for converting between feet and meters.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and place it on grid
    ttk.Label(frame, text="Conversion Feet to Meters and Viceversa", wraplength=200, justify="center").grid(row=0, pady=10)

    # Call populate_generic_window to set up the specifics of this GUI, including the convert functions necessary
    populate_generic_convert_window(frame, "ft", "m", check_positive_n=True, convert_function1=convert_ft_m, convert_function2=convert_m_ft)


def populate_inhg_mb_window(frame):
    """Populates a window for converting between inches of mercury and millibars.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and place it on grid
    ttk.Label(frame, text="Conversion Inches of Mercury (inHg) to Milibars (mb) and Viceversa", wraplength=200, justify="center").grid(row=0, pady=10)

    # Call populate_generic_window to set up the specifics of this GUI, including the convert functions necessary
    populate_generic_convert_window(frame, "inHg", "mb", check_dash=True, convert_function1=convert_inhg_mb, convert_function2=convert_mb_inhg)


def populate_h_m_s_decimal_h_window(frame):
    """Populates a window for converting between hours, minutes, seconds and decimal hours.

    Parameters:
        frame (Frame): The frame to populate.

    Returns:
        None
    """
    # Create title label and place it on grid
    ttk.Label(frame, text="Conversion Hours:Minutes:Second to Decimal Hours and Viceversa", wraplength=200, justify="center").grid(row=0, pady=10, columnspan=2)

    ttk.Label(frame, text="Quantity in").grid(row=1, column=0, pady=10)

    ttk.Label(frame, text="Hours:").grid(row=2, column=0)
    ent_h = ttk.Entry(frame, width=2, justify="left")
    ent_h.grid(row=2, column=1, padx=0)

    ttk.Label(frame, text="Minutes:").grid(row=3, column=0)
    ent_m = ttk.Entry(frame, width=2)
    ent_m.grid(row=3, column=1)

    ttk.Label(frame, text="Seconds:").grid(row=4, column=0)
    ent_s = ttk.Entry(frame, width=2)
    ent_s.grid(row=4, column=1)

    ttk.Label(frame, text="Result:").grid(row=5, column=0, pady=20)
    lbl_result = ttk.Label(frame, text="")
    lbl_result.grid(row=6, column=0)
    ttk.Label(frame, text="Decimal Hours").grid(row=6, column=1)

    ttk.Button(frame, text="Go Back", command=frame.master.destroy).grid(row=8, column=0, columnspan=2, pady=10)

    lbl_error = ttk.Label(frame, text="", wraplength=200, justify="center")
    lbl_error.grid(row=9, pady=10, columnspan=2)


    def calculate_decimal_h(event):
        """Calculates decimal hours from hours, minutes and seconds.

        Parameters:
            event (Event): The event that triggered this function.

        Returns:
            None
        """
        try:
            str_hours = ent_h.get()
            str_minutes = ent_m.get()
            str_seconds = ent_s.get()
            
            if str_hours == "":
                hours = 0
            elif str_hours.isdigit():
                hours = float(str_hours)
            else:
                raise ValueError

            if str_minutes == "":
                minutes = 0
            elif str_minutes.isdigit():
                minutes = float(str_minutes)
            else:
                raise ValueError

            if str_seconds == "":
                seconds = 0
            elif str_seconds.isdigit():
                seconds = float(str_seconds)
            else: 
                raise ValueError

        except ValueError:      
            # In case ValueError was raised because they were not empty strings
            # erase the entry boxes
            ent_h.delete(0, tk.END)
            ent_m.delete(0, tk.END)
            ent_s.delete(0, tk.END)

            # Show error message to user
            lbl_error.config(text="Only numbers allowed in the input boxes!")
            
            # Assign 0 for hours, minutes, and seconds
            hours, minutes, seconds = 0, 0, 0

        decimal_h = convert_h_min_s_decimal_h(hours, minutes, seconds)

        # Change result box values, by deleting and replacing it
        lbl_result.config(text=f"{decimal_h:.3f}")
    
    def clear():
        """Clears the entry boxes and result lbl.

        Returns:
            None
        """
        ent_h.delete(0, tk.END)
        ent_m.delete(0, tk.END)
        ent_s.delete(0, tk.END)

        lbl_result.config(text="")

    ttk.Button(frame, text="Clear", command=clear).grid(row=7, column=0, columnspan=2, pady=10)

    ent_h.bind("<KeyRelease>", calculate_decimal_h)
    ent_m.bind("<KeyRelease>", calculate_decimal_h)
    ent_s.bind("<KeyRelease>", calculate_decimal_h)
    

# Define main calculate functions
def calculate_dead_reckoning(course, latitude, longitude, speed, time):
    """Calculates the estimated latitude and longitude based on the course, speed and time.

    Parameters:
        course (float): The course in degrees.
        latitude (float): The current latitude.
        longitude (float): The current longitude.
        speed (float): The speed in knots.
        time (float): The time in minutes.

    Returns:
        dict: A dictionary containing the estimated latitude and longitude.
    """
    # Convert course from degrees to radians
    course_rad = radians(course)

    # Convert speed from knots to degrees per minute
    speed = speed / 60

    estimated_latitude = latitude + (speed * cos(course_rad)) * time
    estimated_longitude = longitude + (speed * sin(course_rad)) * time

    # Return results in a dict
    dictionary = {
        "latitude": estimated_latitude,
        "longitude": estimated_longitude
    }

    return dictionary


def calculate_true_airspeed(altitude, equivalent_airspeed):
    """Calculate the True Airspeed (TAS) given the altitude and the Equivalent Airspeed (EAS).
    
    Parameters:
    altitude (float): The altitude in feet.
    equivalent_airspeed (float): The Equivalent Airspeed in knots.
    
    Returns:
    float: The True Airspeed in knots.
    """
    tas = equivalent_airspeed * (1 + altitude / 50000)

    return tas


def calculate_ground_speed(tas, wind_speed, wind_direction, aircraft_direction):
    """Calculates the ground speed of an aircraft given its airspeed and wind conditions.

    Parameters:
        tas (float): The true airspeed of the aircraft in knots.
        wind_speed (float): The speed of the wind in knots.
        wind_direction (float): The direction which the wind is coming from, in degrees.
        aircraft_direction (float): The direction in which the aircraft is heading in degrees.

    Returns:
        float: The ground speed of the aircraft in knots.
    """
    # Convert angles to radians
    wind_direction_rad = radians(wind_direction)
    aircraft_direction_rad = radians(aircraft_direction)

    # Calculate wind component
    wind_component = wind_speed * cos(wind_direction_rad - aircraft_direction_rad)

    # Add component to the aircraft's true airspeed to get the ground speed
    groundspeed = tas + wind_component

    return groundspeed



def calculate_off_course_correction(distance_off_course, distance_flown, distance_remaining):
    """Calculates the total heading correction needed to get back on course.

    Parameters:
        distance_off_course (float): The distance off course in nautical miles.
        distance_flown (float): The distance flown in nautical miles.
        distance_remaining (float): The remaining distance to the destination in nautical miles.

    Returns:
        float: The total heading correction needed to get back on course in degrees.
    """
    # Calculate the correction angle in radians
    correction_angle = arctan(distance_off_course / (distance_flown + distance_remaining)) * (180 / pi)

    # If need to turn more than 180 degrees, subtract the result from 360 degrees.
    # If the angle is negative, add 360 to bring it into the range 0-360
    if correction_angle < 0:
        correction_angle += 360

    return correction_angle


def calculate_fuel_endurance(total_amount_fuel, average_fuel_burn):
    """Calculates the endurance of an aircraft given its fuel amount and burn rate.

    Parameters:
        total_amount_fuel (float): The total amount of fuel on board in gallons.
        average_fuel_burn (float): The average fuel burn rate in gallons per hour.

    Returns:
        float: The endurance of the aircraft in hours.
    """
    endurance = total_amount_fuel / average_fuel_burn

    return endurance


def calculate_rate_descent(groundspeed):
    """Calculates the rate of descent needed for a standard descent profile.

    Parameter:
        groundspeed (float): The groundspeed of the aircraft in knots.

    Returns:
        float: The rate of descent needed for a standard descent profile in feet per minute.
    """
    descent_rate = groundspeed * 5.0

    return descent_rate


def calculate_tod(current_altitude, altitude_airfield, rate_descent, groundspeed):
    """Calculates the top of descent point for an aircraft.

    Parameters:
        current_altitude (float): The current altitude of the aircraft in feet.
        altitude_airfield (float): The altitude of the airfield in feet.
        rate_descent (float): The desired rate of descent in feet per minute.
        groundspeed (float): The groundspeed of the aircraft in knots.

    Returns:
        float: The top of descent point from the destination airfield in nautical miles.
    """
    tod = ((current_altitude - altitude_airfield) / rate_descent) * groundspeed * (1/60)

    return tod


def calculate_distance_traveled(speed, time):
    """Calculates the distance traveled given a speed and time.

    Parameters:
        speed (float): The speed in knots.
        time (float): The time elapsed in minutes.

    Returns:
        float: The distance traveled in nautical miles.
    """
    distance = speed * (time/60)

    return distance


def calculate_toa(remaining_distance, groundspeed):
    """Calculates the estimated time of arrival at a destination given a remaining distance and groundspeed.

    Parameters:
        remaining_distance (float): The remaining distance to the destination in nautical miles.
        groundspeed (float): The groundspeed of the aircraft in knots.

    Returns:
        float: The estimated time of arrival at the destination in minutes.
    """
    estimated_time_of_arrival = (remaining_distance / groundspeed) * 60

    return estimated_time_of_arrival


# Define convert functions
def convert_celsius_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit.

    Parameters:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    fahrenheit = 9/5 * celsius + 32
    return fahrenheit


def convert_fahrenheit_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius.

    Parameters:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature in Celsius.
    """
    celsius = 5/9 * (fahrenheit - 32)
    return celsius


def convert_naut_mi(naut_mi):
    """Converts distance from nautical miles to miles.

    Parameters:
        naut_mi (float): The distance in nautical miles.

    Returns:
        float: The distance in miles.
    """
    mi = naut_mi * 1.15078
    return mi


def convert_mi_naut(mi):
    """Converts distance from miles to nautical miles.

    Parameters:
        mi (float): The distance in miles.

    Returns:
        float: The distance in nautical miles.
    """
    naut_mi = mi / 1.15078
    return naut_mi


def convert_naut_km(naut_mi):
    """Converts distance from nautical miles to kilometers.

    Parameters:
        naut_mi (float): The distance in nautical miles.

    Returns:
        float: The distance in kilometers.
    """
    km = naut_mi * 1.852
    return km


def convert_km_naut(km):
    """Converts distance from kilometers to nautical miles.

    Parameters:
        km (float): The distance in kilometers.

    Returns:
        float: The distance in nautical miles.
    """
    naut_mi = km / 1.852
    return naut_mi


def convert_gallons_liters(gallons):
    """Converts volume from gallons to liters.

    Parameters:
        gallons (float): The volume in gallons.

    Returns:
        float: The volume in liters.
    """
    liters = gallons * 3.78541
    return liters


def convert_liters_gallons(liters):
    """Converts volume from liters to gallons.

    Parameters:
        liters (float): The volume in liters.

    Returns:
        float: The volume in gallons.
    """
    gallons = liters / 3.78541
    return gallons


def convert_pounds_kg(pounds):
   """Converts weight from pounds to kilograms.

   Parameters:
       pounds (float): The weight in pounds.

   Returns:
       float: The weight in kilograms.
   """
   kg = pounds * 0.453592
   return kg


def convert_kg_pounds(kg):
   """Converts weight from kilograms to pounds.

   Parameters:
       kg (float): The weight in kilograms.

   Returns:
       float: The weight in pounds.
   """
   pounds = kg / 0.453592
   return pounds


def convert_ft_m(ft):
   """Converts length from feet to meters.

   Parameters:
       ft (float): The length in feet.

   Returns:
       float: The length in meters.
   """
   m = ft * 0.3048
   return m


def convert_m_ft(m):
   """Converts length from meters to feet.

   Parameters:
       m (float): The length in meters.

   Returns:
       float: The length in feet.
   """
   ft = m / 0.3048
   return ft


def convert_inhg_mb(inhg):
   """Converts pressure from inches of mercury to millibars.

   Parameters:
       inhg (float): The pressure in inches of mercury.

   Returns:
       float: The pressure in millibars.
   """
   mb = inhg * 33.86389
   return mb


def convert_mb_inhg(mb):
   """Converts pressure from millibars to inches of mercury.

   Parameters:
       mb (float): The pressure in millibars.

   Returns:
       float: The pressure in inches of mercury.
   """
   inhg = mb / 33.86389
   return inhg


def convert_h_min_s_decimal_h(hours, minutes, seconds):
   """Converts time from hours, minutes and seconds to decimal hours.

   Parameters:
       hours (int): Hours part of the time.
       minutes (int): Minutes part of the time.
       seconds (int): Seconds part of the time.

   Returns:
       float: Time converted into decimal hours.
   """
   decimal_h = hours + (minutes / 60) + (seconds / 3600)
   return decimal_h


# Define check functions
def check_positive(value):
    """Checks if a value is less than zero.

    Parameters:
        value (float): The value to check.

    Returns:
        bool: True if the value is less than zero, False otherwise.
    """
    if value < 0:
        return True
    else:
        return False


def check_dashes(value):
    """Checks if a value is a dash ("-").

    Parameters:
        value (str): The value to check.

    Returns:
        bool: True if the value is a dash, False otherwise.
    """
    if value == "-":
        return True
    else:
        return False


# This function is used for binding the units and conversion_function necessary
def calculate_conversion(event, ent_box1, ent_box2, convert_function, check_positive_n, check_dash):
    """Calculates a conversion between two units and updates the corresponding entry boxes.

    Parameters:
        event (Event): The event that triggered this function.
        ent_box1 (Entry): The entry box containing the value to convert.
        ent_box2 (Entry): The entry box where to display the converted value.
        convert_function (function): The function to use for the conversion.
        check_positive_n (bool): Whether to check if the input value needs to be positive.
        check_dash (bool): Whether to check if the input value is a dash.

    Returns:
        None
    """
    try:
        value = float(ent_box1.get())

        # Check if number needs to be positive
        if check_positive_n and check_positive(value):
            raise ValueError

        # Convert unit1 to unit2 by calling 
        # convert_function_1
        unit2 = convert_function(value) 

        # Change ent box value unit2, by deleting and replacing it
        ent_box2.delete(0, tk.END)
        ent_box2.insert(0, f"{unit2:.2f}")

    except ValueError:
        # Check if checking for dashes is necessary
        # If necessary, check if input was a single dash, indicating negative numbers, erase string otherwise
        if check_dash and check_dashes(ent_box1.get()):
            pass

        else:
            # In case the input is not a positive float, clear entry box and result value label
            ent_box1.delete(0, tk.END)
            ent_box2.delete(0, tk.END)


def populate_generic_convert_window(frame, unit1, unit2, convert_function1, convert_function2=None, check_positive_n=False, check_dash=False):
    """Populates a generic conversion window with labels, entry boxes and buttons.

    Parameters:
        frame (Frame): The frame to populate.
        unit1 (str): The first unit of conversion.
        unit2 (str): The second unit of conversion.
        convert_function1 (function): The function to convert from unit1 to unit2.
        convert_function2 (function, optional): The function to convert from unit2 to unit1. Defaults to None.
        check_positive_n (bool, optional): Whether to check if the input value needs to be positive. Defaults to False.
        check_dash (bool, optional): Whether to check if the input value is a dash. Defaults to False.

    Returns:
        None
    """
    # Set all labels and buttons
    lbl_value = ttk.Label(frame, text="Enter Value:")
    ent_value_unit1 = ttk.Entry(frame)
    lbl_unit1 = ttk.Label(frame, text=unit1)

    lbl_value2 = ttk.Label(frame, text="Enter Value:")
    ent_value_unit2 = ttk.Entry(frame)
    lbl_unit2 = ttk.Label(frame, text=unit2)

    btn_close = ttk.Button(frame, text="Go Back", command=frame.master.destroy)

    # Place labels and buttons on grid
    lbl_value.grid(row=1, column=0)
    ent_value_unit1.grid(row=2, column=0, pady=10)
    lbl_unit1.grid(row=2, column=1, padx=0)

    lbl_value2.grid(row=3)
    ent_value_unit2.grid(row=4, column=0, pady=10)
    lbl_unit2.grid(row=4, column=1)

    btn_close.grid(row=5, pady=20)

    # Bind the calculate functions to the appropriate value entry box so
    # that the computer calls it when the user changes the text in either entry box.
    # Using functools.partial to pass multiple arguments.
    
    ent_value_unit1.bind(
        "<KeyRelease>",
        partial(
            calculate_conversion,
            ent_box1=ent_value_unit1,
            ent_box2=ent_value_unit2,
            convert_function=convert_function1,
            check_positive_n=check_positive_n,
            check_dash=check_dash
        )
    )

    # If convert_function2 not defined, do not bind the following
    if convert_function2 != None:
        ent_value_unit2.bind(
            "<KeyRelease>",
            partial(
                calculate_conversion,
                ent_box1=ent_value_unit2,
                ent_box2=ent_value_unit1,
                convert_function=convert_function2,
                check_positive_n=check_positive_n,
                check_dash=check_dash
            )
        )


# This will populate the main feautures windows 
def populate_window(frame, n_widgets, labels):
    """Populates a window with a specified number of widgets and corresponding labels.

    Parameters:
        frame (Frame): The frame to populate.
        n_widgets (int): The number of widgets to create.
        labels (list): A list of labels for the widgets.

    Returns:
        dict: A dictionary containing all created widgets, with keys being: ["lbl_1"], ["lbl_2"], etc. ["ent_1"], ["ent_2"] etc.
    """
    # Validate number of widgets with number of labels provided
    if len(labels) != n_widgets:
        print("Number of labels does not equal the number of widgets specified.")
        raise ValueError
    
    # Create dictionary for returning all lbl and ent
    dictionary = {}

    # Loop through number of n_widgets and create the appropriate label and entry box
    for i in range(n_widgets):
        dictionary[f"lbl_{i}"] = ttk.Label(frame, text=labels[i])
        dictionary[f"ent_{i}"] = ttk.Entry(frame)

    # Place widgets on grid
    i = 1
    for value in dictionary.values():
        value.grid(row=i, columnspan=2)

        i += 1
    
    # Create result label, place it after the last widget
    dictionary["lbl_result"] = ttk.Label(frame, text="", wraplength=200)
    dictionary["lbl_result"].grid(row=n_widgets*2+2, pady=10, column=0, columnspan=2)

    # Create 'Calculate', 'Clear' and 'Close' btns
    dictionary["btn_calculate"] = ttk.Button(frame, text="Calculate")
    dictionary["btn_clear"] = ttk.Button(frame, text="Clear")
    dictionary["btn_close"] = ttk.Button(frame, text="Go Back", command=frame.master.destroy)

    # Place them on grids, after the result_label
    dictionary["btn_calculate"].grid(row=n_widgets*2+1, column=0, columnspan=2, pady=10)
    dictionary["btn_clear"].grid(row=n_widgets*2+3, column=0, columnspan=2)
    dictionary["btn_close"].grid(row=n_widgets*2+4, column=0, columnspan=2)

    return dictionary


# Call main
if __name__ == "__main__":
    main()
