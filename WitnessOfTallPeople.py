"""
There are n people lined up, and each have a height represented as an integer. A murder has happened right in front of them, and only people who are taller than everyone in front of them are able to see what has happened. How many witnesses are there?

Example:
Input: [3, 6, 3, 4, 1]  
Output: 3
Explanation: Only [6, 4, 1] were able to see in front of them.
 #
 #
 # #
####
####
#####
36341                                 x (murder scene)
Here's your starting point:

def witnesses(heights):
  # Fill this in.

print witnesses([3, 6, 3, 4, 1])
# 3
"""

def witnesses(heights):
    # Fill this in.
    count = 1
    min_height = heights[-1]
    for person in heights[::-1]:
        if person > min_height:
            count += 1
            min_height = person
    return count

print(witnesses([3, 6, 3, 4, 1]))
# 3