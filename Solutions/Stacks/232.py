class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.transfer()
        return self.s2.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        self.transfer()
        return self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2
        
    def transfer(self, s1=self.s1, s2=self.s2):
        if not s2:
            while s1:
                s2.append(s1.pop())
    

        
        
