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

    def append_at_a_location(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 1
        while current:
            if count == 1:
                node.next = current
                self.head = node
                self.size += 1
                # print(count)
                return
            elif index == index:
                node.next = current
                prev.next = node
                self.size += 1
                return
            count += 1
            prev = current
            current = current.next
        if count < index:
            print("The list has less number of elements")

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __contains__(self, data):
        for node in self:
            if node == data:
                return True
        return False

    def __len__(self):
        # return self.size
        count = 0
        for _ in self:
            count += 1
        return count


if __name__ == "__main__":
    words = SinglyLinkedList()
    words.append("egg")
    words.append("ham")
    words.append("spam")
    print("=" * 10)

    current = words.head
    while current:
        print(current.data)
        current = current.next

    words.append_at_a_location("new", 2)
    print("=" * 10)
    current = words.head
    while current:
        print(current.data)
        current = current.next
    print("=" * 10)

    print("new" in words)
    print("gold" in words)
    print("=" * 10)
