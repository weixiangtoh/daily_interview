"""
You are given a stream of numbers. Compute the median for each new element .

Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]

Here's a starting point:

def running_median(stream):
  # Fill this in.

running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2
"""
def running_median(stream):
    # Fill this in.
    result = [stream[0]]
    for i in range(1, len(stream)):
        sort = sorted(stream[:i+1])
        mid = i // 2

        if (i+1) % 2 == 0:
            median = (sort[mid] + sort[mid+1]) / 2
        else:
            median = sort[mid]
        
        result.append(median)
    
    print(result)
    return result

if __name__ == "__main__":
    ans = running_median([2, 1, 4, 7, 2, 0, 5])
    print("Answer is CORRECT!" if ans == [2, 1.5, 2, 3.0, 2, 2.0, 2] else "Answer is NOT correct!")