class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if self.data:
            self.data.append([val, min(val, self.data[-1][0])])
        else:
            self.data.append([val, val])

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:

        return self.data[len(self.data) - 1][0]

    def getMin(self) -> int:
        return self.data[-1][1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-1)

print(obj.getMin())


