import turtle
import BoundingBox
from TurtleShapes import drawOneShape, drawOneDESCRIPTION

def drawRowsOfRows(t, draw_func):
    """
    Draws 10 rows of shapes with increasing size and different y-coordinates.
    Shapes are drawn within the bounds of -500 to 500 on the x-axis and -250 to 250 on the y-axis.
    
    Parameters:
    t (Turtle): The turtle used to draw.
    draw_func (function): The function to draw each shape.
    """
    num_rows = 10  # Number of rows to draw
    num_shapes_per_row = 10  # Number of shapes in each row

    start_size = 10  # Starting size for the shapes
    size_increment = 10  # Increment size between consecutive rows

    start_x = -500  # Starting x-coordinate for shapes in a row
    start_y = 250  # Starting y-coordinate for the first row
    y_step = -10  # Vertical step between rows

    # Outer loop to draw each row
    for row in range(num_rows):
        size = start_size + row * size_increment  # Size for the current row
        y = start_y + row * y_step  # Calculate y-coordinate for the current row

        # Inner loop to draw shapes in the current row
        for shape in range(num_shapes_per_row):
            x = start_x + shape * (size + 5)  # Calculate x-coordinate for the current shape

            # Move turtle to the starting point for this shape
            t.penup()
            t.goto(x, y)
            t.pendown()

            # Draw the shape using the provided draw function
            draw_func(t, size)


def main():
    """
    Sets up the turtle screen and calls the drawRowsOfRows function to draw rows of shapes.
    """
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Draw rows of shapes using the drawOneDESCRIPTION function from TurtleShapes
    drawRowsOfRows(t, drawOneDESCRIPTION)


if __name__ == '__main__':
    win = turtle.Screen()  # Initialize the turtle window
    BoundingBox.drawBoundingBox()  # Draw the bounding box to constrain shapes
    main()  # Call the main function to draw rows of shapes
    win.exitonclick()  # Close the window when clicked
