class MinStack:
    stack=[]
    maxstack = []
    minstack = []
    def __init__(self):
        self.stack = []
        self.maxstack = []
        self.minstack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.maxstack:
            self.maxstack.append(val)
        else:
            if self.maxstack[-1] <= val:
                self.maxstack.append(val)
            else:
                self.maxstack.append(self.maxstack[-1])
        if not self.minstack:
            self.minstack.append(val)
        else:
            if self.minstack[-1] >= val:
                self.minstack.append(val)
            else:
                self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        self.maxstack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        else:
            return None










