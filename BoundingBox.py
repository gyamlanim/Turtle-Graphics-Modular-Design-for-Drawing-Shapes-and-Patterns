import turtle

def drawBoundingBox():
    """
    Draws a bounding box; this is a rectangular boundary within which all required shapes must be drawn.
    """
    width = 1150
    height = 550
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.setposition(-width/2, height/2)
    t.pendown()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.penup()
