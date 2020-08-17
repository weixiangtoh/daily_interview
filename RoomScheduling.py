"""
You are given an array of tuples (start, end) representing time intervals for lectures. 
The intervals may be overlapping. Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
"""
def timeIntervals(array):
    startList = []
    endList = []
    rooms = 0

    for start,end in sorted(array):
        if start not in startList:
            startList.append(start)
        if end not in endList:
            endList.append(end)

    startList = sorted(startList)
    endList = sorted(endList)

    while len(startList) > 0:
        # extract first item of startList
        start = startList.pop(0)
        # check earliest end timing
        end = endList[0]
        # check if meeting that has started will end
        if start >= end:
            endList.pop(0)
        else:
            rooms += 1

    return rooms

if __name__ == "__main__":
    print(timeIntervals([(30, 75), (0, 50), (60, 150)]))
    # 2
    print(timeIntervals([(1, 18),(18, 23),(15, 29),(4, 15),(2, 11),(5, 13)]))
    # 4