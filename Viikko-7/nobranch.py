class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def check(node):
    # If the node has more than one child, the tree is branching
    if len(node.children) > 1:
        return False
    # If the node has children, check if all subtrees are non-branching
    return all(check(child) for child in node.children)