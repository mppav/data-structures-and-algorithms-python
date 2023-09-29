"""
Stack-based queues
"""


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.Stack1.pop())
        if not self.stack2:
            print("No element to dequeue")
            return
        return self.stack2.pop()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print(queue.stack1)

    queue.dequeue()
    print(queue.stack1)
    print(queue.stack2)
    queue.dequeue()
    print(queue.stack2)
