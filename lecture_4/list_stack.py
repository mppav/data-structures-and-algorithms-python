class Stack:
    def __init__(self, size=5) -> None:
        self.data = []
        self.size = size

    def push(self, data):
        if len(self.data) >= self.size - 1:
            print("Stack Overflow")
        else:
            self.data.append(data)

    def pop(self):
        if len(self.data) == 0:
            print("Stack Underflow")
        else:
            return self.data.pop(self)

    def peek(self):
        if len(self.data) == 0:
            print("Stack is empty")
        else:
            return self.data[-1]
