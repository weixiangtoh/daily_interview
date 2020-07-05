"""
You are given a positive integer N which represents the number of steps in a staircase. 
You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

def staircase(n):
  # Fill this in.
  
print staircase(4)
# 5
print staircase(5)
# 8

Can you find a solution in O(n) time?

"""

# n = 1: 1 way (1)
# n = 2: 2 ways (11, 2)
# n = 3: 3 ways (111, 12, 21)
# n = 4: 5 ways (1111, 112, 121, 211, 22)
# n = 5: 8 ways (11111, 221, 1211, 112, 1112, 122, 212, 2111)
# n = 6: 13 ways (111111, 11112, 11121, 11211, 12111, 21111, 1221, 1212, 2121, 2211, 2112, 1122, 222)
# Fibonacci's sequence! ways for n steps = ways for (n-1) + ways for (n-2)
def staircase(n):
    # Fill this in.
    fib_seq = [1, 2]
    for i in range(2, n):
        current = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(current)
    return fib_seq[n-1]
    
print(staircase(4))
# 5
print(staircase(5))
# 8