# Exceeding Requirements: To achieve this, I followed the example provided to make my functions more reusable with parameters,
# making it possible to call them with different arguments if necessary. Note this specifically in the draw_pine_tree function,
# which was called 18 times using for loops inside the draw_ground function.

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

from random import randint, choice


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draws the sky and all objects in it (ex. sun and clouds).

    Parameters
        canvas: canvas used for outputting image
        scene_width: the width of the image
        scene_height: the height of the image
    Return: nothing
    """
    # Draw sky
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="deepSkyBlue")

    # Draw sun at a random x position
    position_height = scene_height - 150

    draw_sun(canvas, position_height, scene_width)

    # Draw 4 clouds at random positions  
    for i in range(4):
        draw_cloud(canvas, scene_width, scene_height)


def draw_sun(canvas, position_height, scene_width):
    """Draws the sun at a random x position in the canvas.

    Parameters
        canvas: canvas used for outputting image
        position_height: the height where the sun will be positioned in the image
        scene_width: the width of the image
    Return: nothing
    """
    # Get random position (x) for the sun
    x0 = randint(0, scene_width - 50)
    draw_oval(canvas, x0, position_height, x0 + 100, position_height + 100, outline="yellow", fill="yellow")


def draw_cloud(canvas, scene_width, scene_height):
    """Draws a single cloud at a random position in the canvas.
    
    Parameters
        canvas: canvas used for outputting image
        scene_width: the width of the image
        scene_height: the height of the image
    Return: nothing
    """
    # Set the initial x0 and y0 coordinates to be random
    x0 = randint(0, scene_width)
    y0 = randint(int(scene_height / 3), scene_height)
    
    # Draw four ovals in the sky
    for i in range(4):
        x1 = x0 + 100
        y1 = y0 + 70

        # Ensure clouds are inside scene display
        if x0 < scene_width:

            # First oval, keep the values as assigned
            draw_oval(canvas, x0, y0, x1, y1, width=0, fill="white")

            # Update the start x coordinate to the right
            x0 += 50

            # Update the height of the start y coordinate of the second oval
            if i == 0:
                y0 += 25
            
            # Set the height of the start y coordinate of the third oval to be the same as the first
            elif i == 1:
                y0 -= 25
            
            # Set x and y start coordinates to be exactly below as the first oval
            else:
                x0 -= 100
                y0 -= 20


def draw_ground(canvas, scene_width, scene_height):
    """Draws the ground area and all objects on it.

    Parameters
        canvas: canvas used for outputting image
        scene_width: the width of the image
        scene_height: the height of the image
    Return: nothing
    """
    # Draw ground
    # Define ground height
    ground_height = scene_height / 3

    draw_rectangle(canvas, 0, 0, scene_width, ground_height, width=0, fill="green")
    
    # Draw grass on ground
    grass_height = ground_height + 20
    draw_grass(canvas, scene_width, ground_height, grass_height)

    # Draw 18 trees in three diagonal lines
    tree_height = 150
    location_x = 50
    location_y = ground_height

    for i in range(3):
        for j in range(6):
            draw_pine_tree(canvas, tree_height, location_x, location_y)
            
            location_x += 40
            location_y -= 30

            if location_y < 0 or location_x > scene_width:
                break
        
        # Separate the lines of the trees by 250 (x being 300 the first iteration and 550 the second)
        location_x = 300 if i == 0 else 550
        location_y = ground_height


def draw_grass(canvas, scene_width, ground_height, grass_height):
    """Draw grass all over the ground.

    Parameters
        canvas: canvas used for outputting image
        scene_width: the width of the image
        ground_height: the place where the grass will start being drawn
        grass_height: the height the grass should be built
    Return: nothing
    """
    # Define initial values for the x0 coordinate 
    x0 = 0

    # Ensure the grass row won't go out the screen
    while x0 != scene_width:
        # Update the location each iteration
        x1 = x0 + 10
        x2 = x1 + 10

        draw_polygon(canvas, x0, ground_height, x1, grass_height, x2, ground_height, width=1, outline="green", fill="green")

        # Move x0 right
        x0 += 10


def draw_pine_tree(canvas, tree_height, location_x, location_y):
    """Draw a pine tree.

    Parameters
        canvas: canvas used for outputting image
        tree_height: the height of the tree
        location_x: the start x coordinate
        location_y: the start y coordiante
    Return: nothing
    """
    # Get height of trunk
    trunk_height = location_y + 45

    # Draw trunk of tree
    draw_rectangle(canvas, location_x, location_y, location_x + 25, trunk_height, width=0, fill="brown4")

    # Draw top of tree
    bottom_x = location_x - 35
    bottom_y = trunk_height
    tip = trunk_height + tree_height
    tree_width = location_x + 60

    # Assign random color for the top of the tree
    top_colors = [
        "darkGreen", "green4", "green3", "springGreen4", "forestGreen", "chartreuse4", "limeGreen", "darkOliveGreen", "oliveDrab4", "yellow4",
        "gold4", "darkGoldenrod4", "darkOrange"
    ]

    top_color = choice(top_colors)

    for i in range(2):
        draw_polygon(canvas, bottom_x, bottom_y, location_x + 12.5, tip, tree_width, bottom_y, width=1, outline=top_color, fill=top_color)

        # Draw the second top of pine tree,
        bottom_y += 50


# Call the main function so that
# this program will start executing.
main()
