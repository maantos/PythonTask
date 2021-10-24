class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, n):
        self.items.append(n)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def f(s):
    stack = Stack()
    index = 0;
    while index < len(s):
        x = s[index]
        if x is '(':
            stack.push(x)
        else:
            if stack.isEmpty():
                return False
            stack.pop()
        index += 1

    if stack.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(f('(())'))