class MinStack:

    def __init__(self):
        self.stack = []
        self.n = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.n = self.n +1

    def pop(self) -> None:
        self.stack.pop()
        self.n = self.n -1

    def top(self) -> int:
        return(self.stack[-1])

    def getMin(self) -> int:
        minVal = self.stack[0]
        for val in self.stack:
            if val < minVal:
                minVal = val
        return(minVal)
