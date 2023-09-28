class Node:
    """A singly-linked node."""

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


words = SinglyLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")

current = words.head
while current:
    print(current.data)
    current = current.next
