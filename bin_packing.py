# ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: John Paxton
# Last Modified: January 25, 2016
# ----------------------------------------------
# Modified to include find_naive_solution so that
# driver does not need to be imported.  You may delete
# find_naive_solution from your submission.
# ----------------------------------------------

#***************************
#Lane Lutgen and John Waters
"""
This solution relies on the original indexes of the inputted list.
The list is cloned with a new value, 'num' added to keep track of
the index that each rectangle has in the original list. The rectangles
are then sorted accoring to width, largest first, and placed into
the placement list with their original index still attached to them. 
Once this is complete, the algorithm sorts the placement list according
to the original indexes and returns a list of just the coordinate tuples
back to the driver for testing. The final solution is the def:johns_attempt.
This solution reliably showed 95.5+% increase over the naive solution.
"""
#***************************

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
        height = rectangle[1]
        coordinate = (upper_left_x, upper_left_y)   # make a tuple
        placement.insert(0, coordinate)             # insert tuple at front of list
        upper_left_y = upper_left_y - height
        
    placement.reverse()                             # original order
    return placement

# -----------------------------------------------
"""
Sorts rectangles according to width and then reverses the order
so that the widest rectangle is used first. After 100 rectangles 
have been placed, we take the height of the first rectangle in
the row and make that our new upper_left_y point. This process
then repeates until all rectangles have been placed

def lanes_attempt(rectangles):
    placement = []
    upper_left_x = 0
    upper_left_y = 0
    loop_count = 0;

    #Sorts rectangles
    rectangles.sort(key=operator.itemgetter(1))
    #Reverses order so widest is first
    rectangles.reverse()

    #find the height of the first rectangle
    max_height = rectangles[0][1]
    

    for rectangle in rectangles:
        if loop_count == 0:
            max_height = rectangle[1]
        width = rectangle[0]
        coordinate = (upper_left_x, upper_left_y)  
        placement.insert(0, coordinate)
        #set our new x coordinate             
        upper_left_x = upper_left_x + width
        loop_count = loop_count + 1

        #if we have placed 100 rectangles, start a new row
        #by setting the y coordinate to the height of the
        #rectangle placed in the row first
        if loop_count == 100:
            upper_left_y = upper_left_y + max_height
            loop_count = 0
            upper_left_x = 0

        
    placement.reverse()                            
    return placement
"""


def johns_attempt(rectangles):
    # placement list with the index values still attached
    placement = []
    # clone of the original rectangles list
    clone = []
    # return list with just the coordinates
    returnList = []
    
    upper_left_x = 0
    upper_left_y = 0
    loop_count = 0
    
    # add the index from the original list to the cloned list
    for num in range(len(rectangles)):
        clone.append((num, rectangles[num]))
        
    # sort the cloned list to order the rectangles from largest
    # width to smallest width.        
    clone.sort(key=operator.itemgetter(1), reverse = True)

    # first row maximum width is in the first index, first element
    # in the clone list. 
    max_width = clone[0][1][0]
   
    for rectangle in clone:
        if loop_count == 0:
            # if a new collumn is created, set the width of that
            # collumn to the next biggest rectangle's width
            max_width = rectangle[1][0]
        # the height of the current rectangle
        height = rectangle[1][1]
        coordinate = (upper_left_x, upper_left_y)
        # insert the coordinates and original index into the
        # placement list
        placement.insert(0, (coordinate, rectangle[0]))
        # adjust the height for the next rectangle insertion below
        # the one before it
        upper_left_y = upper_left_y - height
        # increment the loop counter
        loop_count = loop_count + 1

        if loop_count == 50:
            # to have the smallest perimeter possible, 50 rectangles
            # proved to be the best option. when 50 rectangles
            # are inserted, a new collumn is started
            upper_left_x = upper_left_x + max_width
            # reset the loop counter and the starting y value
            loop_count = 0
            upper_left_y = 0

    # sort the list accoring to original index value     
    placement.sort(key=operator.itemgetter(1))

    # strip the index value and return only the coordinates to the
    # driver
    for num in range(len(placement)):
        returnList.append(placement[num][0])

    return returnList

 
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

