"""
CS 101 - Homework 8
"""
import string

def analyzeFile(filename):
    """
    Analyzes a file and return a few statistics in a tuple:
    most common word, least common word, longest word, and shortest word
    """
    f = open(filename, encoding="utf-8") # open the file
	# Keep track of how many times each word occurs in the file
    counts = {}

    for line in f:		# iterate over the lines of the file
        words = line.split()            # turn the line into an array of words
        for word in words:
            # Get rid of any whitespace and punctuation
            word = word.strip(string.whitespace + string.punctuation)
            # Put the word in lowercase
            word = word.lower()
            counts[word] = counts.get(word, 0) + 1

    # Find the most common word, least common word, longest word, and shortest word
    mostCommonWord = word
    mostCount = counts[word]
    leastCommonWord = word
    leastCount = counts[word]

    longestWord = word
    longestLength = len(word)
    shortestWord = word
    shortestLength = len(word)
    
    for key, value in counts.items():
        if value > mostCount:
            mostCommonWord = key
            mostCount = value
        elif value < leastCount:
            leastCommonWord = key
            leastCount = value

        if len(key) > longestLength:
            longestWord = key
            longestLength = len(key)
        elif len(key) < shortestLength:
            shortestWord = key
            shortestLength = len(key)

    f.close()
            
    return (mostCommonWord, leastCommonWord, longestWord, shortestWord)
