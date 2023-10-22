"""
This module contains the implementation of a binary tree data structure.

Classes:
- Node: represents a node in the binary tree.

Functions:
- inorder: performs inorder traversal of the binary tree.
- preorder: performs preorder traversal of the binary tree.
- postorder: performs postorder traversal of the binary tree.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")
n1.left_child = n2
n1.right_child = n3
n2.left_child = n4

current = n1
while current:
    print(current.data)
    current = current.left_child

print("\n")


def inorder(root_node):
    """
    Performs inorder traversal of the binary tree.

    Args:
    - root_node: the root node of the binary tree.

    Returns:
    None
    """
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)


def preorder(root_node):
    """
    Performs preorder traversal of the binary tree.

    Args:
    - root_node: the root node of the binary tree.

    Returns:
    None
    """
    current = root_node
    if current is None:
        return
    print(current.data)
    preorder(current.left_child)
    preorder(current.right_child)


def postorder(root_node):
    """
    Performs postorder traversal of the binary tree.

    Args:
    - root_node: the root node of the binary tree.

    Returns:
    None
    """
    current = root_node
    if current is None:
        return
    postorder(current.left_child)
    postorder(current.right_child)
    print(current.data)


inorder(n1)
print("\n")
preorder(n1)
print("\n")
postorder(n1)
