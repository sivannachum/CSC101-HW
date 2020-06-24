"""
CS 101 - Homework 7
Answer Key
"""
from PIL import Image

def power(L, exponent):
    """
    Takes in a list of numbers L and returns a new list
    where each value of the original list has been raised to exponent
    Does this using a list comprehension instead of a loop
    """
    squares = [x**exponent for x in L]
    return squares

def average(L):
    """
    Returns the average (arithmetic mean) of a list of numbers L
    Does this using a loop
    """
    sum = 0
    for element in L:
        sum += element
    
    try:
        average = sum/len(L)
    except ZeroDivisionError:
        average = 0
    
    return average

def pigLatin(s):
    """
    Takes in a string (with no punctuation other than spaces)
    and returns a new string with every word converted to pig latin

    We will use three rules for converting a word to pig latin:
    1. If the word is one character long, leave it alone
    2. If the word starts with a vowel (a,e,i,o,u), just add ‘yay’ to the end of the word. (e.g., “apple” => “appleyay”)
    3. Otherwise, the first letter of the word is moved to the back and ‘ay’ is appended to the end (e.g., “dalek” => “alekday”)
    """
    returnString = []

    for word in s.split():
        if len(word) <= 1:
            newWord = word
        elif word[0] in "aeiou":
            newWord = word + "yay"
        else:
            newWord = word[1:] + word[0] + "ay"
        
        returnString.append(newWord)
    
    return ' '.join(returnString)

def blackwhite(image, threshold):
    """
    Takes in an image and a threshold value as parameters and returns a black and white version
    """
    # create a copy of the original image so we don't lose the original
    newImage = image.copy()

    # create our 2D structure of pixels from the image so we can work with individual pixels
    pixels = newImage.load()

    # get the bounding box -- this is returned as a tuple and we use some python
    # magic to automatically break the tuple up into four variables
    minX,minY,width,height = image.getbbox()

    # iterate over every pixel in the image
    for y in range(height):
        for x in range(width):
            # get the rgb value of the pixel (as a tuple in the order (red, green, blue))
            rgb = pixels[x,y]

            # if the average is less than the threshold, make the pixel black
            if average(rgb) < threshold:
                pixels[x,y] = (0, 0, 0)
            # otherwise make it white
            else:
                pixels[x, y] = (255, 255, 255)

    # return the new image
    return newImage

def sepia(image):
    """
    Takes in an image and returns a sepia version of it
    """
    # create a copy of the original image so we don't lose the original
    newImage = image.copy()

    # create our 2D structure of pixels from the image so we can work with individual pixels
    pixels = newImage.load()

    # get the bounding box -- this is returned as a tuple and we use some python
    # magic to automatically break the tuple up into four variables
    minX,minY,width,height = image.getbbox()

    # iterate over every pixel in the image
    for y in range(height):
        for x in range(width):
            # get the rgb value of the pixel (as a tuple in the order (red, green, blue))
            rgb = pixels[x,y]

            # set the pixel to a new RGB value
            avg = average(rgb)
            
            # Set the red and blue according to the average and the sepia filter rules
            if avg <= 62:
                red = 1.1 * avg
                blue = .9 * avg
            elif avg <= 192:
                red = 1.15 * avg
                blue = .85 * avg
            else:
                red = 1.08 * avg
                blue = .93 * avg

            # Make sure red is an appropriate number
            if red > 255:
                red = 255

            pixels[x,y] = (int(red), int(avg), int(blue))

    # return the new image
    return newImage

def grayscaleWeighted(image, redWeight, greenWeight, blueWeight):
    """
    Create a better grayscale image by taking a weighted average of the colors
    """
    # create a copy of the original image so we don't lose the original
    newImage = image.copy()

    # create our 2D structure of pixels from the image so we can work with individual pixels
    pixels = newImage.load()

    # get the bounding box -- this is returned as a tuple and we use some python
    # magic to automatically break the tuple up into four variables
    minX,minY,width,height = image.getbbox()

    # iterate over every pixel in the image
    for y in range(height):
        for x in range(width):
            # get the rgb value of the pixel (as a tuple in the order (red, green, blue))
            rgb = pixels[x,y]

            # set the pixel to a new RGB value 
            # that is the average of the old
            avg = int((rgb[0] * redWeight + rgb[1] * greenWeight + rgb[2] * blueWeight))
            pixels[x,y] = (avg, avg, avg)

    # return the new image
    return newImage

def mirror(image):
    """
    Takes an image and returns another image that has the left side reflected
    across the center line onto the right side.
    """
    # create a copy of the original image so we don't lose the original
    newImage = image.copy()

    # create our 2D structure of pixels from the image so we can work with individual pixels
    pixels = newImage.load()

    # get the bounding box -- this is returned as a tuple and we use some python
    # magic to automatically break the tuple up into four variables
    minX,minY,width,height = image.getbbox()

    # iterate over every pixel in the image
    for y in range(height):
        for x in range(int(width/2)):
            # get the rgb value of the pixel (as a tuple in the order (red, green, blue))
            rgb = pixels[x,y]

            # set the pixel to a new RGB value 
            # that is the average of the old
            pixels[width-x-1,y] = (rgb[0], rgb[1], rgb[2])

    # return the new image
    return newImage

# BONUS
def fourUp(image):
    """
    Takes in an image and returns a image that has four 1/4 sized versions of the original in it
    """
    # create a copy of the original image so we don't lose the original
    newImage = image.copy()

    # create our 2D structure of pixels from the image so we can work with individual pixels
    pixels = newImage.load()

    # get the bounding box -- this is returned as a tuple and we use some python
    # magic to automatically break the tuple up into four variables
    minX,minY,width,height = image.getbbox()

    # So that we have access to the pixels in the original image
    origPixels = image.load()
    # iterate over every pixel in the image
    # top left
    for y in range(0, height, 2):
        for x in range(0, width, 2):
            # get the rgb value of the corresponding pixel (as a tuple in the order (red, green, blue))
            rgb = origPixels[x, y]

            # top left
            pixels[x//2, y//2] = (rgb[0], rgb[1], rgb[2])
            # top right
            pixels[width//2 + x//2, y//2] = (rgb[0], rgb[1], rgb[2])
            # bottom left
            pixels[x//2, height//2 + y//2] = (rgb[0], rgb[1], rgb[2])
            # bottom right
            pixels[width//2 + x//2, height//2 + y//2] = (rgb[0], rgb[1], rgb[2])

    # return the new image
    return newImage

# image = Image.open('hw6_image.png')
# image.save('hw6_image_mirror.png')
# gray_image = grayscaleWeighted(image, 0.299, 0.587, 0.114)
# image.show()