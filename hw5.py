"""
CS 101 - Homework 5
Answer Key
"""
import turtle

# PRELAB
def GCD(a, b):
    """
    Determines the GCD (greatest common divisor) of positive integers a and b
    using the Euclidean Algorithm recursively
    """
    if a < b:
        temp = a
        a = b
        b = temp
    rem = a%b
    if rem == 0:
        return b
    else:
        return GCD(b, rem)

# HOMEWORK
def drawStairs(len, levels):
    """
    Draws stairs recursively where the length of a stair is len and there are levels stairs
    """
    if levels == 0:
        return
    else:
        # Draw the top and right parts of the square
        turtle.forward(len)
        turtle.right(90)
        turtle.forward(len)
        # Reset the orientation and call to begin drawing the next square
        turtle.left(90)
        drawStairs(len/2, levels-1)
        # Complete this stair
        turtle.right(180)
        turtle.forward(len)
        turtle.right(90)
        turtle.forward(len)
        # Reset the orientation
        turtle.right(90)

def drawStairsScene():
    """ 
    Moves the turtle to the top left of the screen and draws a staircase.
    """
    # pick up the pen and move the turtle so it starts at the left edge of the canvas 
    turtle.penup()
    turtle.goto(-turtle.window_width()/2 + 20, turtle.window_height()/2 - 20)
    turtle.pendown()    

    # draw the tree by calling your function
    drawStairs(200,5)

    # finished
    turtle.done()

def isPrime(n):
    """
    Returns True if positive integer n is prime, False otherwise (composite)
    Tests primality using a for loop
    Returns that 1 is prime?
    """
    for i in range(2, n):
        # If this number divides n, n is not prime
        if n%i == 0:
            return False
    # If none of the numbers have divided n, n is prime!
    return True

def printPrimes(n):
    """
    Prints the first n primes, where n is a positive integer
    Uses a while loop to do this
    """
    # This variable keeps track of how many primes we have printed
    i = 0
    # This variable keeps track of what number we are testing
    num = 1
    while (i < n):
        if isPrime(num):
            print(num)
            i += 1
        num += 1

def GCD2(a, b):
    """
    Determines the GCD (greatest common divisor) of positive integers a and b
    using the Euclidean Algorithm iteratively
    """
    if a < b:
        temp = a
        a = b
        b = temp

    rem = a%b
    while rem != 0:
        a = b
        b = rem
        rem = a%b
    
    return b

def caesar_encrypt(msg, shift):
    """
    "Encrypts" the text in msg (that should only contain lowercase letters and spaces)
    by shifting each character by shift characters
    """
    shiftString = 'abcdefghijklmnopqrstuvwxyz '
    lengthShiftString = len(shiftString)
    finalString = ""

    # Conver the letters
    for letter in msg:
        index = (shiftString.index(letter) + shift) % lengthShiftString
        newLetter = shiftString[index]
        finalString = finalString + newLetter
    
    return finalString

def firstPrimes(n):
    """
    Returns a list containing the first n primes, where n is a positive integer
    Does this by using a while loop
    """
    returnList = []
    # This variable keeps track of how many primes we are in the list
    # Could also call len(list)
    i = 0
    # This variable keeps track of what number we are testing
    num = 1
    while (i < n):
        if isPrime(num):
            returnList.append(num)
            i += 1
        num += 1
    return returnList

def factors(n):
    """
    Returns a list containing all factors of input parameter n, where n is a positive integer
    Does this by using a for loop
    """
    returnList = []

    for i in range(1, n+1):
        if n%i == 0:
            returnList.append(i)

    return returnList

# I didn't do BONUS 1 or 2
# BONUS 3
def sumNested(L):
    """
    Takes in a nested list of integers and returns the sum of all the lists.
    A nested list of integers contains 0 or more integers AND 0 or more nested lists of integers
    """
    sum = 0
    for element in L:
        if isinstance(element, list):
            sum += sumNested(element)
        else:
            sum += element
    
    return sum