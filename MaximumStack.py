"""
Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() 
which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.

class MaxStack:
  def __init__(self):
    # Fill this in.

  def push(self, val):
    # Fill this in.

  def pop(self):
    # Fill this in.

  def max(self):
    # Fill this in.

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
print s.max()
# 2
"""
class MaxStack:
    def __init__(self):
        # Fill this in.
        self.main = []
        self.track = []

    def push(self, val):
        # Fill this in.
        self.main.append(val)
        if len(self.main) == 1:
            self.track.append(val)
            return
        
        # if current item is greater than the top of the stack of main,
        # add into the track stack
        if val > self.track[-1]:
            self.track.append(val)
        # else append the top value of track stack back into it again
        # to make sure len is the same as mainstack
        else:
            self.track.append(self.track[-1])

    def pop(self):
        # Fill this in.
        self.main.pop()
        self.track.pop()

    def max(self):
        # Fill this in.
        if len(self.track) > 0:
            return self.track[-1]
        return None
        
s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2