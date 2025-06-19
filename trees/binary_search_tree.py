"""
implements binary search tree and its node.
"""
from typing_extensions import Optional

class Node:
    """Class representing a node"""
    def __init__(self, value):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinarySearchTree:
    """ class representing a BST"""
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root

        while True:
            if value == temp.value:
                return False
            elif value <= temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True
        return False

    def insertNode(self, root, value):

        if root is None:
            return Node(value)
        elif value > root.value:
            root.right = self.insertNode(root.right, value)
        elif value < root.value:
            root.left = self.insertNode(root.left, value)

        return root

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.value, end = " ")
        self.inorder(root.right)
            


if __name__ == "__main__":
    my_tree = BinarySearchTree()
    my_tree.root = my_tree.insertNode(None, 3)
    my_tree.root = my_tree.insertNode(my_tree.root, 2)
    my_tree.root = my_tree.insertNode(my_tree.root, 5)
    my_tree.root = my_tree.insertNode(my_tree.root, 1)
    my_tree.root = my_tree.insertNode(my_tree.root, 9)

    print(my_tree.inorder(my_tree.root))
