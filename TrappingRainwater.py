"""
You have a landscape, in which puddles can form. 
You are given an array of non-negative integers representing the elevation at each location. 
Return the amount of water that would accumulate if it rains.

For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
       X               
   X███XX█X              
 X█XX█XXXXXX                   
# [0,1,0,2,1,0,1,3,2,1,2,1]
Here's your starting pont:

def capacity(arr):
  # Fill this in.

print capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# 6
"""
def capacity(arr):
    # Fill this in.

    # Create two array left and right of size n. 
    n = len(arr)
    left_arr = [0]*n
    right_arr = [0]*n

    # variable for units of water
    water = 0

    # Run one loop from start to end. 
    left_arr[0] = arr[0]
    for i in range(1,n):
        # left array stores the max height of the left col and col itself
        left_arr[i] = max(left_arr[i-1], arr[i])

    # Run another loop from end to start. 
    right_arr[n-1] = arr[n-1]
    for j in range(n-2, 0, -1):
        # right arr stores max height of right col and col
        right_arr[j] = max(right_arr[j+1], arr[j])

    # Traverse the array from start to end.
    for k in range(n):
        # for there to be water, both left and right of i must be higher than i
        # min of left and right makes sure that the least height between right and left is higher than i
        water += min(left_arr[k], right_arr[k]) - arr[k]

    return water

print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6