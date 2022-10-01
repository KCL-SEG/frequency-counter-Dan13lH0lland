"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(*items):
    frequencies = {}
    print(items)
    newItems = []
    for z in items:
        if isinstance(z, int):
            newItems.append(str(z))
        else:
            newItems.append(z)
    for item in newItems:
        counter = 0
        for x in newItems:
            y = str(x)
            if y == item:
                counter += 1
        frequencies[item] = counter
    print(frequencies)
    # Your code goes here
    return frequencies
