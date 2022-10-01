"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    print(items)
    for item in items:
        counter = 0
        for x in items:
            if x == item:
                counter += 1
        frequencies[item] = counter
    print(frequencies)
    # Your code goes here
    return frequencies
