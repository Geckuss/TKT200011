class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count_nodes(node):
    return 1 + sum(count_nodes(child) for child in node.children)

def count(node):
    # Count the number of nodes in each subtree
    subtree_counts = [count_nodes(child) for child in node.children]
    # Check if all subtrees have the same number of nodes
    same_subtree_count = len(set(subtree_counts)) <= 1
    # Count the number of nodes with the same subtree count in the subtrees
    same_subtree_count += sum(count(child) for child in node.children)
    return same_subtree_count