import turtle, BoundingBox

def drawOneShape(t, size):
    """
    Draws a square with the given turtle t and size.
    Parameters:
    t (Turtle): The turtle used to draw the square.
    size (int or float): The length of the sides of the square.
    """
    for _ in range(4):
        t.color("green")
        t.forward(size)
        t.right(90)

def drawOneDESCRIPTION(t, size):
    """
    Draws a house with a rectangular base, a triangular roof, and a circular window.
    Parameters:
    t (Turtle): The turtle used to draw the house.
    size (int or float): The base size of the house's rectangular part.
    """
    # Draw rectangular base
    t.color("blue")
    for _ in range(2):
        t.forward(size)
        t.right(90)
        t.forward(size * 0.75)
        t.right(90)

    # Draw triangular roof
    t.color("brown")
    t.begin_fill()
    t.forward(size)
    t.left(135)
    t.forward(size / (2 ** 0.5))
    t.left(90)
    t.forward(size / (2 ** 0.5))
    t.left(135)
    t.end_fill()

    # Draw circular window
    t.penup()
    t.goto(t.xcor() + size / 2, t.ycor() - size * 0.5)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(size / 7)
    t.end_fill()

# Main program block
if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()

    t = turtle.Turtle()
    t.speed(5)

    # Draw house
    t.penup()
    t.goto(200, 0)
    t.pendown()
    drawOneDESCRIPTION(t, 100)

    # Draw square
    t.penup()
    t.goto(50, 100)
    t.pendown()
    drawOneShape(t, 20)

    win.exitonclick()
