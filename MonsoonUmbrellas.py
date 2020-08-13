"""
Umbrellas are available in different sizes that are able to shelter a certain number of ppl.
Given the number of ppl needing shelter and a list of umbrella sizes, determine the min num of umbrellas necessary to cover 
exactly the num of ppl given, and no more.
If there is no combination tuat covers exactly that number of ppl, return -1

Example:
requirement = 5
sizes = [3,5]
one umbrella can cover exactly cover 5 ppl, so function should return 1

Example:
requirement = 6
sizes = [3,5]
it is possible to use 2 umbrellas of size 3 to cover exactly 6 ppl, so function should return 2

Example:
requirement = 7
sizes = [3,5]
There is no combination of umbrellas that cover exactly 7 ppl, so function should return -1

Function getUmbrellas has following parameters:
- int requirement: num of ppl to shelter
- int sizes[n]: an array of umbrella sizes available

Returns:
- int: min number of umbrellas required to cover exactly requirement ppl or  -1 if impossible

Constraints:
- 1 <= requirement, m, sizes[i] <= 1000
"""
def getUmbrellas(requirement, sizes):
    stack = [0] + [float('inf')] * requirement

    for umbrella in sizes:
        for i in range(umbrella, requirement+1):
            stack[i] = min(stack[i], stack[i-umbrella]+1)
            
    if stack[-1] != float('inf'):
        return stack[-1] 
    else:
        return -1

print(getUmbrellas(5, [3,5]))
# 1
print(getUmbrellas(6, [3,5]))
# 2
print(getUmbrellas(7, [3,5]))
# -1