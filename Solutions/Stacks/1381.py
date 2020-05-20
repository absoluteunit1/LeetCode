class customStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.n = 0
    
    def push(self, x: int) -> None:
        if self.n != self.maxSize:
            self.stack.append(x)
            self.n += 1

    def pop(self) -> int:
        if self.n:
            self.n -= 1
            return self.stack.pop()
        return -1 

    def increment(self, k: int, val: int) -> None:
        if self.n <= k:
            for i in range(self.n):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val