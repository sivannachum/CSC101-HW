"""
CS 101 - Homework 4
"""

# PRELAB
import turtle
import random

def drawTree(length):
    """
    Draws a tree based on size length.

    Randomness, removal of generations, change of base angle, addition of width,
    new change in length between recursions, change in color are from HW.
    I did not add multiple trees to the scene.
    """
    new_length = length + random.randint(-length//10, length//10)
    base_angle = 30
    left_angle = base_angle + random.randint(-base_angle, base_angle)
    right_angle = base_angle + random.randint(-base_angle, base_angle)
    if length < 3:
        return
    else:
        # Change the width of the tree based on the length
        if length//11 == 0:
            turtle.width(1)
        else:
            turtle.width(length//11)
        
        # Change the color based on the generation/length
        if new_length < 40:
            color = random.randint(1, 5)
            if color == 1:
                turtle.pencolor("dark orange")
            elif color == 2:
                turtle.pencolor("chocolate")
            elif color == 3:
                turtle.pencolor("firebrick")
            elif color == 4:
                turtle.pencolor("sea green")
            elif color == 5:
                turtle.pencolor("gold")
        else:
            turtle.pencolor("saddle brown")

        turtle.pendown()
        turtle.forward(new_length)
        turtle.left(left_angle)
        drawTree(length*3/4)
        # Undo the left turn and do the right turn
        turtle.right(left_angle + right_angle)
        drawTree(length*3/4)
        # Undo the right turn to get back to center
        turtle.left(right_angle)
        # Move the turtle back to its original position and orientation
        turtle.penup()
        turtle.backward(new_length)


def drawTreeScene():
    """ 
    Moves the turtle to the bottom of the screen, points it upward, and draws a tree.
    """
    # turn off drawing animation (too slow otherwise)
    turtle.tracer(False)

    # pick up the pen and move the turtle so it starts at the bottom middle 
    turtle.penup()
    turtle.goto(0, -turtle.window_height()/2 + 20)
    turtle.left(90)
    turtle.pendown()    

    # draw the tree by calling your function
    drawTree(200)

    # finished
    turtle.update()
    turtle.done()

# HOMEWORK
def drawSierpinski(length, iterations):
    """
    Draws a Sierpinski triangle based on size length and with iterations controlling the recursion
    pendown/penup parts are optional
    """
    if iterations == 0:
        return
    else:
        # Draw the triangle
        turtle.pendown()
        turtle.left(60)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.left(240)
        turtle.forward(length)
        # Put the turtle back in the orientation it started in
        turtle.right(180)
        # Draw the lower left triangle
        drawSierpinski(length/2, iterations-1)

        # Draw the upper triangle
        turtle.penup()
        turtle.left(60)
        turtle.forward(length/2)
        turtle.pendown()
        turtle.right(60)
        drawSierpinski(length/2, iterations-1)
        turtle.penup()
        turtle.right(120)
        turtle.forward(length/2)
        turtle.left(120)

        # Draw the lower right triangle
        turtle.forward(length/2)
        turtle.pendown()
        drawSierpinski(length/2, iterations-1)
        turtle.penup()
        turtle.backward(length/2)


def drawSierpinskiScene(length, iterations):
    """
    Use this code to call your drawSierpinski() function. This provides
    the functionality of turning off the tracer and running turtle.done().
    """

    # turn off animation (too slow otherwise)
    turtle.tracer(False)
	
    # pick up the pen and move the turtle so it starts at the bottom left of the canvas
    turtle.penup()
    turtle.goto(-turtle.window_width()/3 + 20, -turtle.window_height()/3)
    turtle.pendown()
	
    drawSierpinski(length, iterations)
    
    # finish
    turtle.update()
    turtle.done()

# BONUS
def drawCarpet(length, iterations):
    """
    Draws a Sierpinski carpet based on size length and with iterations controlling the recursion
    pendown/penup parts are optional
    """
    if iterations == 0:
        # Draw and fill in the square
        turtle.fillcolor("medium violet red")
        turtle.begin_fill()
        turtle.left(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.end_fill()
        # Turn the turtle back to its original orientation
        turtle.right(180)
    else:
        # Draw the lower left square
        drawCarpet(length/3, iterations-1)

        # Draw the lower middle square
        turtle.penup()
        turtle.forward(length/3)
        turtle.pendown()
        drawCarpet(length/3, iterations-1)
        
        # Draw the lower right square
        turtle.penup()
        turtle.forward(length/3)
        turtle.pendown()
        drawCarpet(length/3, iterations-1)
        
        # Go back to the original position
        turtle.backward(length*2/3)

        # Go to the middle row
        turtle.penup()
        turtle.left(90)
        turtle.forward(length/3)
        turtle.right(90)
        
        # Draw the middle left square
        turtle.pendown()
        drawCarpet(length/3, iterations-1)

        # Draw the middle right square
        turtle.penup()
        turtle.forward(length*2/3)
        turtle.pendown()
        drawCarpet(length/3, iterations-1)

        # Go to the top row
        turtle.penup()
        turtle.backward(length*2/3)
        turtle.left(90)
        turtle.forward(length/3)
        turtle.right(90)
        
        # Draw the top left square
        turtle.pendown()
        drawCarpet(length/3, iterations-1)

        # Draw the top middle square
        turtle.penup()
        turtle.forward(length/3)
        turtle.pendown()
        drawCarpet(length/3, iterations-1)
        
        # Draw the top right square
        turtle.penup()
        turtle.forward(length/3)
        turtle.pendown()
        drawCarpet(length/3, iterations-1)

        # Go back to the original position
        turtle.backward(length*2/3)
        turtle.left(90)
        turtle.backward(length*2/3)
        turtle.right(90)

def drawCarpetScene(length, iterations):
    """
    Use this code to call the drawCarpet() function. This provides
    the functionality of turning off the tracer and running turtle.done().
    """

    # turn off animation (too slow otherwise)
    turtle.tracer(False)
	
    # pick up the pen and move the turtle so it starts at the bottom left of the canvas
    turtle.penup()
    turtle.goto(-turtle.window_width()/3 + 20, -turtle.window_height()/3)
    turtle.pendown()
	
    drawCarpet(length, iterations)
    
    # finish
    turtle.update()
    turtle.done()
