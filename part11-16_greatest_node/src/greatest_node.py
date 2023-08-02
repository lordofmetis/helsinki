# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None, current_max: int = 0):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.current_max = current_max

def greatest_node(root: Node):
    if root is None:
        return float('-inf')
  
    left_max = greatest_node(root.left_child)
    right_max = greatest_node(root.right_child)
  
    current_max = max(root.value, left_max, right_max)

    return current_max


if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))