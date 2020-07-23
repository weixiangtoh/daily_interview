"""
You are given an array of intervals - that is, an array of tuples (start, end). 
The array may not be sorted, and could contain overlapping intervals. 
Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

Here's a starting point:

def merge(intervals):
  # Fill this in.
  
print merge([(1, 3), (5, 8), (4, 10), (20, 25)])
# [(1, 3), (4, 10), (20, 25)]
"""
def merge(intervals):
    # Fill this in.
    
    intervals.sort()

    # initialise a counter
    i=1
    interval_list = []
    result = []

    # changing to tuples to lists
    for tuples in intervals:
        tuples = list(tuples)
        interval_list.append(tuples)

    # similar to for loop but allows loop to run without error when elements are removed
    while i<len(interval_list):
        
        if interval_list[i][0] <= interval_list[i-1][1]:
            
            interval_list[i-1][0] = min(interval_list[i-1][0],interval_list[i][0])
            interval_list[i-1][1] = max(interval_list[i-1][1],interval_list[i][1])
            
            interval_list.pop(i)
        
        else:
            i+=1

    # change lists back to tuples
    for lists in interval_list:
        lists = tuple(lists)
        result.append(lists)

    return result

print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]