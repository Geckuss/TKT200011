class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    # If the node has no children, it is a leaf
    if not node.children:
        return 1
    # If the node has children, count the leaves in the subtrees
    return sum(count(child) for child in node.children)