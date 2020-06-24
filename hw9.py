"""
CS 101 - Homework 9
Answer Key
"""
import turtle as t

class Point():
    """
    Represents 2D Point objects
    """
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        """
        Returns a string representation of the Point
        """
        return '('+str(self.x)+','+str(self.y)+')'
    
    def print_point(p):
        """ This function prints the value of our point p"""
        print('(',p.x,',',p.y,')')
        
    def dist(p1,p2):
        """
        Returns the distance from one point to another
        """
        return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)** (1/2)

    def scale(self, factor):
        """
        Modifies a Point by multiplying its x-coordinate and y-coordinate by a scale factor
        passed in as a parameter
        """
        self.x = self.x * factor
        self.y = self.y * factor

    # BONUS 2: Translate
    def translate(self, xChange, yChange):
        """
        Translates a point by xChange in the x direction and yChange in the y direction
        """
        self.x = self.x + xChange
        self.y = self.y + yChange


def drawDots(points):
    """
    Takes a list points as input and draws a dot on the drawing window for each Point
    """
    for point in points:
        t.penup()
        t.goto(point.x, point.y)
        t.dot()
        t.pendown()
    t.penup()

def drawLines(points):
    """
    Takes as input a list points of Point objects, uses the turtle to visit each point,
    thereby tracing the outline of the shape. i.e., connect the dots
    """
    t.penup()
    for point in points:
        t.goto(point.x, point.y)
        t.pendown()
    t.penup()

def readPoints(filename):
    """
    Opens the specified file, processes each line by creating a Point object
    with each pair of floating point numbers, and then returns a list of list of the Point objects
    Each list in the list is separated by the word "break" in filename
    """
    returnList = []
    with open(filename, encoding="utf-8") as f:
        innerList = []
        for line in f:		# iterate over the lines of the file
            if line.lower().strip() == "break":
                # end this list
                returnList.append(innerList)
                innerList = []
            else:
                # turn the line into an array of numbers, i.e. a point
                pointString = line.split()
                point = Point(float(pointString[0]), float(pointString[1]))
                innerList.append(point)
        # Add the last inner list
        if innerList != []:
            returnList.append(innerList)

    return returnList

def scalePoints(points, factor):
    """
    Takes a list of Point objects and an integer factor as input parameters
    For each point p in the list of Point objects, call p.scale(factor) to stretch out the points by factor
    """
    for p in points:
        p.scale(factor)

# BONUS 2 = translate
def translatePoints(points, xChange, yChange):
    """
    Takes a list of Point objects and a float xChange and yChange as input parameters
    For each point p in the list of Point objects, call p.translate(xChange, yChange) to translate the points
    """
    for p in points:
        p.translate(xChange, yChange)

# BONUS 1 = color
def drawObject(filename, stretch_factor = 1, xChange = 0, yChange = 0, color = None):
    shape = readPoints(filename)
    # Scale
    for points in shape:
        scalePoints(points, stretch_factor)
    
    # Translate
    for points in shape:
        translatePoints(points, xChange, yChange)
    
    # Draw dots
    t.tracer(False)
    for points in shape:
        drawDots(points)
    t.tracer(True)
    
    # Connect the dots
    count = 0
    for points in shape:
        if color is not None:
            t.fillcolor(color[count])
            t.begin_fill()
        drawLines(points)
        if color is not None:
            t.end_fill()
            count += 1
    
    t.hideturtle()

drawObject("cat.txt", 12, -150, -170, ["orange", "pink", "pink"])
drawObject("jackolantern.txt", 5, 150, -200)
drawObject("witch.txt", 12, yChange=100, color=["purple", "white"])
t.done()