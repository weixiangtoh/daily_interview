"""
Implement a queue class using two stacks. 
A queue is a data structure that supports the FIFO protocol (First in = first out). 
Your class should support the enqueue and dequeue methods like a standard queue.

Here's a starting point:

class Queue:
  def __init__(self):
    # Fill this in.
    
  def enqueue(self, val):
    # Fill this in.

  def dequeue(self):
    # Fill this in.

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print q.dequeue()
print q.dequeue()
print q.dequeue()
# 1 2 3
"""
class Queue:
    def __init__(self):
        # Fill this in.
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, val):
        # Fill this in.
        self.stack1.append(val)

    def dequeue(self):
        # Fill this in.
        if not self.stack1 and not self.stack2:
            return "Empty"
        
        # add everything from stack1 to stack2 in reverse
        if self.stack1 and not self.stack2:
            for element in self.stack1[::-1]:
                self.stack2.append(element)

        return self.stack2.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3