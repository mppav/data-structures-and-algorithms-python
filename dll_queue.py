"""
Linked list based queues
"""


class Node(object):
    """
    Node
    """

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    """
    Queue on double linked list
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        """
        Add data to the queue
        """
        new_node = Node(data, None, None)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def dequeue(self):
        """
        Get data from the queue
        """
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
        elif self.count < 1:
            print("Queue is empty")
        self.count -= 1


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue("dog")
    q.enqueue("True")

    print(q.count)

    q.dequeue()

    print(q.count)
