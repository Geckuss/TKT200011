class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    # Start with the number of children of the current node
    max_children = len(node.children)
    # Check the number of children of each child node
    for child in node.children:
        max_children = max(max_children, count(child))
    return max_children