"""
You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

Here is a starting point:

def matrix_spiral_print(M):
  # Fill this in.

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
"""
# first need to have a function that rotates matrix 
def rotate_matrix(M):
    new_M = []
    if len(M) == 1:
        return [M[0][::-1]]

    if len(M) < 1:
        return M

    col_length = len(M[-1])

    for col in range(col_length-1, -1, -1):
        line = []
        for row in range(len(M)):
            line.append(M[row][col])
        new_M += [line]
    
    return new_M

def matrix_spiral_print(M):
    # Fill this in.
    num_list = []
    while len(M) > 0:
        num_list += M.pop(0)
        M = rotate_matrix(M)

    result = ""
    for item in num_list:
        result += str(item) + " "

    print(result)

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
print("1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12")
# print(rotate_matrix(grid))