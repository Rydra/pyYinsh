from Domain import *



# Yinsh board is kind of weird. It looks like hexagonal,it points out 11 coordinates for X and 11 coordinates for Y,
# But there are a total of 85 intersections (which is far from 11x11). So this algorithm is NOT correct at all.
# We need to come up with a way to represent this. For instance, G11 exists, but B11 does not nor does A1
# (Grab a picture of Yinsh board to see it by yourself)
# Since the Yinsh board is so weird, let's declare an initialize function that does not take a width and height,
# but a number of intersections... however we still run into the problem of how to create the cells and assign a proper,
# valid coordinate...This makes me think I have two options... either I can hardcode the coordinates (and after that hardcoding
# for specific coordinates which are the valid moves, like B2, that allows for all directions except bottom-left) or
# try to find a suitable pattern (which will be somewhat difficult in this board)
# All these peculiarities and exceptions will end up becoming a source of ifs and cases, which by themselves
# pose a maintainability problem (we will have to think of a better alternative)
def initializeBoard():

    intersections = [
        Intersection(Empty(), Position(letter, num))
            for letter, lst in validRanges.items()
            for num in lst
        ]

    return Board(intersections)
