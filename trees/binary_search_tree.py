from typing_extensions import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinarySearchTree:
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
            



my_tree = BinarySearchTree()
my_tree.insert(3)
print(my_tree.root.value)
