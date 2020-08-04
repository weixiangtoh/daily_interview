"""
Students in a class are asked to stand in ascending order according to their heights for annual class photograph.
Determine the number of students not currently standing in their correct positions.

Example:
height = [1, 1, 3, 3, 4, 1]

The 3 students at indices 2, 4 and 5 are not in the right positions.
The correct positions are  [1, 1, 1, 3, 3, 4]. Return 3

Complete function countStudents and return integer: number of students not standing in correct position

Constraints:
- 1 <= n <= 10^5
- 1 <= height[i] <= 10^9
"""
def countStudents(students, size):
    sorted_heights = sorted(students)
    count = 0
    for i in range(size):
        if students[i] != sorted_heights[i]:
            count += 1
    return count

print(countStudents([1, 1, 3, 3, 4, 1], 6))