
import turtle, BoundingBox,random
from TurtleShapes import drawOneShape, drawOneDESCRIPTION
def drawEverywhere(t, draw_func):
    '''
    Function to draw the images at random locations and with random sizes
    '''
    num_shapes = int(input("How many shapes do you want to draw? "))

    for _ in range(num_shapes):
        # Generate random coordinates for drawing the shape
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)

        # Generate random size
        size = random.randint(20, 100)

        # Move the turtle to the random coordinates without drawing
        t.penup()
        t.goto(x, y)
        t.pendown()

        draw_func(t, size)

def main():
    """
    Sets up the turtle screen, prompts the user to choose between drawing a shape or house,
    and calls drawEverywhere with the corresponding function based on user input, with basic error handling.
    """
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Ask the user to choose the drawing function
    funcNumber = input("Input 0 for drawOneShape, 1 for drawOneDESCRIPTION: ")

    # Call drawEverywhere based on the user's choice
    if funcNumber == '0':
        drawEverywhere(t, drawOneShape)
    elif funcNumber == '1':
        drawEverywhere(t, drawOneDESCRIPTION)
    else:
        print("Invalid input. Please enter 0 or 1.")


if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    screen = turtle.Screen()
    main()
    win.exitonclick()
