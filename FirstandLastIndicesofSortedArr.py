"""
Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
Here is a function signature example:

class Solution: 
  def getRange(self, arr, target):
    # Fill this in.
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
"""

class Solution: 
    def getRange(self, arr, target):
        # Fill this in.
        
        # corner case: not inside
        # --> first and last = -1

        if target not in arr:
            return [-1,-1]

        # return index of the target --> first and last
        # output must be in []

        # --> 2 variables: first and last index
                                # ==> initialise first with last index of arr
                                # ==> initialise last with first index of arr
        first_index = len(arr) - 1
        last_index = 0

        # loop through the arr --> range
        for i in range(len(arr)):

            if arr[i] == target:
                
                # if i < first index ==> first = i
                # if i > last index ==> last = i
                if i < first_index:
                    first_index = i
                if i > last_index:
                    last_index = i
        
        return [first_index,last_index]

        # another method
        # if --> element == target 
            # --> add into store_arr
            # output will just take the first and last item in store arr

  

if __name__ == "__main__":
    # Test program 
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
    x = 2
    print(Solution().getRange(arr, x))
    # [1, 4]

    # Input: 
    A = [1,3,3,5,7,8,9,9,9,15]
    target = 9
    print(Solution().getRange(A, target))
    # Output: [6,8]

    # Input: 
    A = [100, 150, 150, 153]
    target = 150
    print(Solution().getRange(A, target))
    # Output: [1,2]

    # Input: 
    A = [1,2,3,4,5,6,10]
    target = 9
    print(Solution().getRange(A, target))
    # Output: [-1, -1]