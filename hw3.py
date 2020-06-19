"""
CS 101 - Homework 3
Answer Key
"""

# PRELAB
import turtle

def drawSquare(length):
    """
    Draw a square with sides of size length.
    """
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)

def drawSquareScene():
    """
    Helper function to call drawSquare() function.
    """
    drawSquare(100)
    turtle.done()

def drawKoch(length, generations):
    """
    Draws a Koch curve based on size length and with generations controlling the recursion
    """
    # Base case: draw a straight line
    if generations == 0:
        turtle.forward(length)
    elif generations > 0:
        drawKoch(length/3, generations-1)
        turtle.left(60)
        drawKoch(length/3, generations-1)
        turtle.right(120)
        drawKoch(length/3, generations-1)
        turtle.left(60)
        drawKoch(length/3, generations-1)
    
def drawKochScene():
    """ Setup the canvas for drawing the curve and draw it."""
	
    # pick up the pen and move the turtle so it starts at the left edge of the canvas 
    turtle.penup()
    turtle.goto(-turtle.window_width()/2 + 20,0)
    turtle.pendown()    
    
    # draw the curve by calling your function
    drawKoch(500, 2)
    
    # finished
    turtle.done()

# HOMEWORK
def drawSnowflake(length, generations):
    """
    Draws a Koch snowflake based on size length and with generations controlling the recursion
    in the drawKoch() function
    """
    drawKoch(length, generations)
    turtle.right(120)
    drawKoch(length, generations)
    turtle.right(120)
    drawKoch(length, generations)

def drawSnowflakeScene():
    """ Setup the canvas for drawing the snowflake and draw it."""
	
    # pick up the pen and move the turtle so it starts at the bottom left of the canvas 
    turtle.penup()
    # change the pen color
    turtle.pencolor("deep pink")
    turtle.goto(-turtle.window_width()/2 + 70, -turtle.window_height()/2 + 200)
    turtle.pendown()    
    
    # draw the snowflake by calling your function
    drawSnowflake(150, 1)
    
    # pick up the pen and move the turtle so it goes to the top middle of the canvas 
    turtle.penup()
    # change the pen color
    turtle.pencolor("firebrick")
    # change the fill color
    turtle.fillcolor("dark orchid")
    turtle.goto(0, turtle.window_height()/2 - 200)
    turtle.pendown()    
    
    # start filling in 
    turtle.begin_fill()
    # draw the snowflake by calling your function
    drawSnowflake(150, 3)
    # end filling in
    turtle.end_fill()

    # pick up the pen and move the turtle so it goes to the bottom left of the canvas 
    turtle.penup()
    # change the pen color
    turtle.pencolor("rosy brown")
    turtle.goto(turtle.window_width()/2 - 70, -turtle.window_height()/2 + 250)
    turtle.pendown()    
    
    # draw the snowflake by calling your function
    drawSnowflake(150, 2)

    # finished
    turtle.done()

def reverse(text):
    """
    Recursively reverses any string passed in as a parameter
    """
    # base case, 0 or 1 letter string
    if len(text) <= 1:
        return text
    else:
        return text[-1] + reverse(text[:-1])

def drawSpiral(initialLength, angle, multiplier):
    """
    Recursively draws a spiral;
    draws a loop that either collapses in to a fixed point or grows without bound depending on the angle.
    
    initialLength determines how long a line the turtle should draw
    angle determines how much the turtle should turn after drawing the line
    multiplier determines how the length of the line should change for the next iteration
    """
    if initialLength <= 1 or initialLength > 10000:
        return
    else:
        turtle.forward(initialLength)
        turtle.right(angle)
        drawSpiral(initialLength*multiplier, angle, multiplier)

def drawSpiralScene():
    """ Setup the canvas for drawing the spiral and draw it."""
	
    # pick up the pen and move the turtle so it starts at the bottom left of the canvas 
    turtle.penup()
    # change the pen color
    turtle.pencolor("midnight blue")
    turtle.goto(-turtle.window_width()/2 + 50, -turtle.window_height()/2 + 300)
    turtle.pendown()    
    
    # draw the spiral by calling your function
    # this is a spiral that gets smaller
    drawSpiral(300,90,0.9)

    # pick up the pen and move the turtle so it starts at the center of the canvas 
    turtle.penup()
    # change the pen color
    turtle.pencolor("dark turquoise")
    turtle.goto(0, 0)
    turtle.pendown()    

    # draw the spiral by calling your function
    # this is a spiral that gets bigger!
    drawSpiral(10,120,1.2)

    # finished
    turtle.done()

# BONUS
# Note that you could have just integrated this into your original spiral function
def drawBonusSpiral(initialLength, angle, multiplier):
    """
    Recursively draws the bonus spiral;
    draws a loop that either collapses in to a fixed point or grows without bound depending on the angle.
    
    initialLength determines how long a line the turtle should draw
    angle determines how much the turtle should turn after drawing the line
    multiplier determines how the length of the line should change for the next iteration
    """
    if initialLength <= 1 or initialLength > 10000:
        return
    else:
        turtle.forward(initialLength)
        turtle.right(angle)
        # Note that the angle is also changed for the next iteration - this is how we get the bonus spiral
        drawBonusSpiral(initialLength*multiplier, angle+.05, multiplier)

def drawBonusSpiralScene():
    """ Setup the canvas for drawing the bonus spiral and draw it."""
	
    # pick up the pen and move the turtle so it starts at the bottom left of the canvas 
    turtle.penup()
    # change the pen color
    turtle.pencolor("forest green")
    turtle.goto(-turtle.window_width()/2 + 50, -turtle.window_height()/2 + 300)
    turtle.pendown()    
    
    # draw the spiral by calling your function
    # this is a spiral that gets smaller
    drawBonusSpiral(300,91,0.95)

    # finished
    turtle.done()
