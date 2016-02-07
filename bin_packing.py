# ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: John Paxton
# Last Modified: January 25, 2016
# ----------------------------------------------
# Modified to include find_naive_solution so that
# driver does not need to be imported.  You may delete
# find_naive_solution from your submission.
# ----------------------------------------------

"""
FIND_NAIVE_SOLUTION:
    Line the the top left corners of the rectangles up along
the y = 0 axis starting with (0,0).
--------------------------------------------------
rectangles: a list of tuples, e.g. [(w1, l1), ... (wn, ln)] where
    w1 = width of rectangle 1,
    l1 = length of rectangle 1, etc.
--------------------------------------------------
RETURNS: a list of tuples that designate the top left corner placement,
         e.g. [(x1, y1), ... (xn, yn)] where
         x1 = top left x coordinate of rectangle 1 placement
         y1 = top left y coordinate of rectangle 1 placement, etc.
"""

def find_naive_solution (rectangles):   
    placement = []
    upper_left_x = 0
    upper_left_y = 0
    
    for rectangle in rectangles:
        width = rectangle[0]
        coordinate = (upper_left_x, upper_left_y)   # make a tuple
        placement.insert(0, coordinate)             # insert tuple at front of list
        upper_left_x = upper_left_x + width
        
    placement.reverse()                             # original order
    return placement

# -----------------------------------------------
"""
NOT WORKING CURRENTLY, TRYING TO FIGURE OUT OVERLAP ISSUE
"""
def lanes_attempt (rectangles):
    placement = []
    upper_left_x = 0
    upper_left_y = 0
    first_width = 0
    first_height = 0
    previous_width = 0
    previous_height = 0
    for rectangle in rectangles:
        first_width = width = rectangle[0]
        first_height = height = rectangle[1]
        if(height >= previous_height): #if height is larger flip rectangle
            rectangle = flip_rectangle(rectangle)
            width = rectangle[0]
            height = rectangle[1]
            if(height >= previous_height): #if height is still larger, start a new row
                upper_left_x = 0
                upper_left_y = first_height
                first_width = width
                first_height = height
        coordinate = (upper_left_x, upper_left_y)
        placement.insert(0, coordinate)
        previous_width = width
        previous_height = height
        upper_left_x = upper_left_x + width

    placement.reverse()    
    return placement

def flip_rectangle(rectangle):
    new_rectangle = (rectangle[1], rectangle[0])
    return rectangle

"""
FIND_SOLUTION:
    Define this function in bin_packing.py, along with any auxiliary
unctions that you need.  Do not change the driver.py file at all.
--------------------------------------------------
rectangles: a list of tuples, e.g. [(w1, l1), ... (wn, ln)] where
    w1 = width of rectangle 1,
    l1 = length of rectangle 1, etc.
--------------------------------------------------
RETURNS: a list of tuples that designate the top left corner placement,
         e.g. [(x1, y1), ... (xn, yn)] where
         x1 = top left x coordinate of rectangle 1 placement
         y1 = top left y coordinate of rectangle 1 placement, etc.
"""

def find_solution(rectangles):
    return lanes_attempt(rectangles)  # a working example!
