"""
You 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.

Here's the signature:

def num_ways(n, m):
  # Fill this in.

print num_ways(2, 2)
# 2
"""

def factoral(num):
  output = 1
  for i in range(1, num + 1):
    output *= i
  return output

def num_ways(n, m):
  # Fill this in.
  # n width, m height
  # n choose m --> n! / m! (n-m)!
  if n > m:
    denominator = factoral(m) * factoral(n-m)
    # print("denominator>", denominator)
    return int(factoral(n) / denominator)

  elif n == m:
    paths = 1
    doubles = 1
    # total steps to move in a grid is n+m-2
    total_step = m + n - 2

    for j in range(1, n):
        paths *= total_step
        total_step -= 1
        doubles *= j

    paths = int(paths / doubles) 
    return paths

# does not take into account grids where n < m

print(num_ways(2, 2))
# 2
print(num_ways(5, 5))
# 70
print(num_ways(8, 3))
# 56