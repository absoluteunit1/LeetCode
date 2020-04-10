# Implements a simple stack using Python's built in methods

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.contents = []


    def push(self, x):
        self.contents.append(x)

    def pop(self):
        self.contents.pop()

    def top(self):
        top = self.contents.pop()
        self.contents.append(top)
        return top

    def getMin(self):
        return min(self.contents) if self.contents else []
