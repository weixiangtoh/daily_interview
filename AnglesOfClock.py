"""
Given a time in the format of hour and minute, 
calculate the angle of the hour and minute hand on a clock.

def calcAngle(h, m):
  # Fill this in.

print calcAngle(3, 30)
# 75
print calcAngle(12, 30)
# 165
"""
def calcAngle(h, m):
    # Fill this in.
    # find angle of hour hand wrt 12 o clock
    # in a min, hour hand moves 0.5 degrees --> 30 degrees in 1hr
    # must take in account that hour hand moves as min hand moves
    if h == 12:
        h = 0
    elif m == 60:
        h += 1
        m = 0
        if h > 12:
            h -= 12

    hour = (h * 60 + m) * 0.5

    # every min, minute hand moves by 6 degrees
    minute = m * 6

    # find the difference
    angle = abs(hour - minute)

    # the angle could be the obtuse angle, thus this gets the smaller angle
    angle = min(360-angle, angle)
    return int(angle)


print (calcAngle(3, 30))
# 75
print (calcAngle(12, 30))
# 165