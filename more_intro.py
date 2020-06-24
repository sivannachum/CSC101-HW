"""
CS 101 - Homework 2
"""

# Part 1
'''
# Causes ModuleNotFoundError
import homework.py

# Causes IndexError
str1 = "cat"
str1[10]

# Causes NameError
print(meow)

# Causes SyntaxError
def uhoh

# Causes TypeError
"123" + 3

# Causes ZeroDivisionError
3/0
'''

def aspectRatio(width, height):
    """
    Takes in the width and height of a rectangle and
    return the aspect ratio (width/height) or 0 if the height is 0
    """
    try:
        ratio = width/height
    except ZeroDivisionError:
        ratio = 0.0

    return ratio


def flip(number):
    """
    Takes in an integer, converts it to a string, reverses it, turns it back into an integer and
    returns the result
    """
    numberString = str(number)
    reverseString = numberString[::-1]
    return int(reverseString)


def lastWord(s):
    """
    Extracts and returns the last word from a string
    """
    try:
        index = s.rfind(' ')
        last = s[index+1:]
    except IndexError:
        last = s

    return last

# Bonus:
def improvedLastWord(s):
    """
    Extracts and returns the last word from a string more effectively
    (accounting for extra whitespace at the end, removing punctuation, etc.)
    """
    try:
        s = s.strip()
        index = s.rfind(' ')
        last = s[index+1:]
    except IndexError:
        last = s
    
    if last[-1] in '!?.,\'"()':
        last = last[:-1]

    return last
