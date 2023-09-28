class Node:
    """A singly-linked node."""

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
        self.size += 1
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def delete_first_node(self):
        if not self.head:
            print("No data element to delete")
            return None
        self.head = self.head.next
        self.size -= 1

    def delete_last_node(self):
        if not self.head:
            print("No data element to delete")
            return None
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next
        previous.next = None
        self.size -= 1

    def delete(self, data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def clear(self):
        self.head = None
        self.size = 0


if __name__ == "__main__":
    words = SinglyLinkedList()
    words.append("egg")
    words.append("ham")
    words.append("spam")

    words.delete_first_node()

    current = words.head
    while current:
        print(current.data)
        current = current.next

    words.delete_last_node()

    current = words.head
    while current:
        print(current.data)
        current = current.next

    words.delete("ham")
    current = words.head
    while current:
        print(current.data)
        current = current.next
