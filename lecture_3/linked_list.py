"""
Class of single linked list
"""


class Node:
    """A node."""

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        # Encapsulate the data in a Node
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


if __name__ == "__main__":
    words = SinglyLinkedList()
    words.append("egg")
    words.append("ham")
    words.append("spam")

    # Simple iteration over the linked list

    # current = words.head
    # while current:
    #     print(current.data)
    #     current = current.next

    for word in words:
        print(word)
