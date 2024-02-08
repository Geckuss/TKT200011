class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

def check(node, depth=0, leaf_depth=None):
    # If the node is a leaf
    if not node.children:
        # If it's the first leaf we've seen
        if leaf_depth is None:
            return True
        # If it's not the first leaf, check if its depth is the same as the previous leaves
        else:
            return depth == leaf_depth
    # If the node is not a leaf, check all its children
    else:
        for child in node.children:
            same_depth = check(child, depth + 1, leaf_depth)
            if not same_depth:
                return False
        return True

def check_tree(node):
    same_depth = check(node)
    return same_depth