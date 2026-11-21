class MinStack:

    def __init__(self):
        self.minValStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minValStack) > 0:
            self.minValStack.append(min(self.minValStack[-1], val))
        else:
            self.minValStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minValStack.pop()
        

    def top(self) -> int:
        item = self.stack[-1]
        return item
        

    def getMin(self) -> int:
        return self.minValStack[-1]



        
