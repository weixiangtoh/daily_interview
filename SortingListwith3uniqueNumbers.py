"""
Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
def sortNums(nums):
  # Fill this in.

print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]
"""

def sortNums(nums):
    # Fill this in.
    
    # iterate through the loop:
        # check each element if its bigger than the element next to it
        # if bigger, swap place
        # if smaller, move on
        # if same, check further until not the same then do the smaller and bigger check

    # bubble sort --> but its not in O(n) time!
    # for i in range(len(nums)):

    #     for j in range(len(nums) - i - 1):
    #         if nums[j] > nums[j+1]:
    #             nums[j], nums[j+1] = nums[j+1], nums[j]
    # return nums

    # only got 3 numbers --> find out what numbers are there
    number_arr = []
    for element in nums:
        if element not in number_arr:
            number_arr.append(element)
        
    num1, num2, num3 = number_arr
    
    # rearrange the numbers such that they are in ascending order WITHOUT BUBBLE SORTING
    if num1 > num3:
        num1, num3 = num3, num1
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2

    # get the num of times each digit appears
    count1 = 0
    count2 = 0
    count3 = 0

    for item in nums:
        if item == num1:
            count1 += 1
        elif item == num2:
            count2 += 1
        else:
            count3 += 1

    # return the in order multipying the number of times it appeared
    return [num1] * count1 + [num2] * count2 + [num3] * count3

if __name__ == "__main__":
    print("Test 1:")
    if sortNums([3, 3, 2, 1, 3, 2, 1]) == [1, 1, 2, 2, 3, 3, 3]:
        print("Pass!")
    else:
        print("Fail")
    # [1, 1, 2, 2, 3, 3, 3]
    print("Test 2:")
    if sortNums([4, 4, 2, 1, 4, 2, 1]) == [1, 1, 2, 2, 4, 4, 4]:
        print("Pass!")
    else:
        print("Fail")
    # [1, 1, 2, 2, 4, 4, 4]
    print("Test 3:")
    if sortNums([30, 30, 12, 1, 30, 12, 1]) == [1, 1, 12, 12, 30, 30, 30]:
        print("Pass!")
    else:
        print("Fail")
    # [1, 1, 12, 12, 30, 30, 30]
    print("Test 4:")
    if sortNums([36, 36, 22, 11, 36, 22, 11]) == [11, 11, 22, 22, 36, 36, 36]:
        print("Pass!")
    else:
        print("Fail")
    # [11, 11, 22, 22, 36, 36, 36]