"""
Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 52 + 122 = 132.

def findPythagoreanTriplets(nums):
  # Fill this in.

print findPythagoreanTriplets([3, 12, 5, 13])
# True
"""

def findPythagoreanTriplets(nums):
    # Fill this in.
    array = []
    for item in nums:
        array.append(item**2)
    # to get squared arr 
    array.sort()

    for i in range(len(nums)):
        j = 0
        k = i - 1
        while j < k:
            if array[j] + array[k] == array[i]:
                return True
            else:
                if array[j] + array[k] < array[i]:
                    j += 1
                else:
                    k += 1
    
    return False

print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
print(findPythagoreanTriplets([3, 1, 4, 6, 5]))
# True