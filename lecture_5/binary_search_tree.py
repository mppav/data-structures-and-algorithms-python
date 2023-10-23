class Node:
    """
    A class used to represent a node in a binary search tree.

    Attributes
    ----------
    data : int
        The value of the node.
    right_child : Node
        The right child of the node.
    left_child : Node
        The left child of the node.
    """

    def __init__(self, data):
        """
        Constructs all the necessary attributes for the node object.

        Parameters
        ----------
        data : int
            The value of the node.
        """
        self.data = data
        self.right_child = None
        self.left_child = None


class Tree:
    """
    A class used to represent a binary search tree.

    Attributes
    ----------
    root_node : Node
        The root node of the binary search tree.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the tree object.
        """
        self.root_node = None

    def insert(self, data):
        """
        Inserts a new node with the given value into the binary search tree.

        Parameters
        ----------
        data : int
            The value of the node to be inserted.

        Returns
        -------
        Node
            The root node of the binary search tree.
        """
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return self.root_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return self.root_node
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return self.root_node

    def inorder(self, root_node):
        """
        Traverses the binary search tree in inorder traversal.

        Parameters
        ----------
        root_node : Node
            The root node of the binary search tree.
        """
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data)
        self.inorder(current.right_child)

    def get_node_with_parent(self, data):
        """
        Returns the parent and the node with the given value in the binary
        search tree.

        Parameters
        ----------
        data : int
            The value of the node to be searched.

        Returns
        -------
        tuple
            A tuple containing the parent and the node with the given value in
            the binary search tree.
        """
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return (parent, current)

    def delete(self, val):
        """
        Deletes the node with the given value from the binary search tree.

        Args:
            val: The value of the node to be deleted.

        Returns:
            None
        """
        root = self

        def delete_helper(root, val):
            """
            Deletes a node with the given value from the binary search
            tree rooted at the given root.

            Args:
                root: The root of the binary search tree.
                val: The value of the node to be deleted.

            Returns:
                The root of the binary search tree after the node with the
                given value has been deleted.
            """
            if not root:
                return root

            if val < root.val:
                root.left = delete_helper(root.left, val)
            elif val > root.val:
                root.right = delete_helper(root.right, val)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                # Шукаємо найменший елемент в дереві (як правило самий лівий)
                current = root
                while current.left:
                    current = current.left

                root.val = current.val
                root.right = delete_helper(root.right, root.val)
            return root

        delete_helper(root, val)

    def search(self, data):
        """
        Searches for the node with the given value in the binary search tree.

        Parameters
        ----------
        data : int
            The value of the node to be searched.

        Returns
        -------
        int or None
            The value of the node if found, None otherwise.
        """
        current = self.root_node
        while True:
            if current is None:
                print("Item not found")
                return None
            elif current.data is data:
                print("Item found", data)
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child

    def find_min(self):
        """
        Finds the minimum value in the binary search tree.

        Returns
        -------
        int
            The minimum value in the binary search tree.
        """
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current.data

    def find_max(self):
        """
        Finds the maximum value in the binary search tree.

        Returns
        -------
        int
            The maximum value in the binary search tree.
        """
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current.data


if __name__ == "__main__":
    tree = Tree()
    r = tree.insert(5)
    r = tree.insert(2)
    r = tree.insert(7)
    r = tree.insert(9)
    r = tree.insert(1)

    tree.inorder(r)

    tree.search(9)

    tree.remove(9)
    tree.search(9)

    tree = Tree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    tree.insert(9)
    tree.insert(1)

    print(tree.find_min())
    print(tree.find_max())
