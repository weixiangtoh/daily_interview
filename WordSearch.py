'''
You are given a 2D array of characters, and a target string.  
Return whether or not the word target word exists in the matrix.
Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

Example:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.

Here's the function signature:

def word_search(matrix, word):
  # Fill this in.
  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print word_search(matrix, 'FOAM')
# True
'''

# def check_word(row_word, word):


def word_search(matrix, word):
    # Fill this in.

    # check left to right
    for row in matrix:
        for i in range(len(row)):
            row_word = "".join(row[i:len(word)+i])
            # print(row_word)
            if row_word == word:
                return True
    
    # check up down
    for j in range(len(matrix)):
        col_word = ""
        for k in range(len(matrix[i])):
            for l in range(len(word)):
                col_word += matrix[l][k]
            
            if col_word == word:
                return True

    return False

matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAM'))
# True
print(word_search(matrix, 'MASS'))
# True