class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node, depth=0):
    # The depth of the current node is added to the sum
    total_depth = depth
    # Add the depth of each child node
    for child in node.children:
        total_depth += count(child, depth + 1)
    return total_depth