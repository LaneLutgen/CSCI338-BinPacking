# ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: John Paxton
# Last Modified: January 25, 2016
# ----------------------------------------------
# Modified to include find_naive_solution so that
# driver does not need to be imported.  You may delete
# find_naive_solution from your submission.
# ----------------------------------------------

import operator

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

def lanes_attempt(rectangles):
    placement = []
    upper_left_x = 0
    upper_left_y = 0
    loop_count = 0;

    rectangles.sort(key=operator.itemgetter(1))
    rectangles.reverse()
    #for rectangle in rectangles:
    #    print (rectangle)

    max_height = rectangles[0][1]
    
    for rectangle in rectangles:
        if loop_count == 0:
            max_height = rectangle[1]
        width = rectangle[0]
        coordinate = (upper_left_x, upper_left_y)  
        placement.insert(0, coordinate)             
        upper_left_x = upper_left_x + width
        loop_count = loop_count + 1
        if loop_count == 100:
            upper_left_y = upper_left_y + max_height
            loop_count = 0
            upper_left_x = 0

        
    placement.reverse()                            
    return placement


"""
Sorted the rectangles accoring to height. The list is then
reversed so the tallest rectangle is inserted first. The
rectangles are added and the insertion lest is reversed and
returned. The rows have no more than 75 rectangles each, and
result in 92+% improvement over the naive solution. The
Average Ratio stays between .027 and .029 on 70 random sets.
"""
def johns_attempt(rectangles):
    placement = []
    upper_left_x = 0
    upper_left_y = 0
    loop_count = 0;

    rectangles.sort(key=operator.itemgetter(0))
    rectangles.reverse()
    
    max_width = rectangles[0][0]
    
    for rectangle in rectangles:
        if loop_count == 0:
            max_width = rectangle[0]
        height = rectangle[1]
        coordinate = (upper_left_x, upper_left_y)  
        placement.insert(0, coordinate)             
        upper_left_y = upper_left_y + height
        loop_count = loop_count + 1
        if loop_count == 75:
            upper_left_x = upper_left_x + max_width
            loop_count = 0
            upper_left_y = 0
        
    placement.reverse()                            
    return placement


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
    #return lanes_attempt(rectangles) 
    return johns_attempt(rectangles)

