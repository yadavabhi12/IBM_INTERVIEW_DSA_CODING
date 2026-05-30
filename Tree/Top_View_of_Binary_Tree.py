


from collections import deque

# Tree Node class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def topView(root):

    # If tree is empty
    if not root:
        return []

    # Dictionary:
    # key   = horizontal distance (HD)
    # value = first node seen at that HD
    top_nodes = {}

    # Queue for BFS
    # Store pair: (node, horizontal_distance)
    queue = deque()

    # Root node has HD = 0
    queue.append((root, 0))

    # BFS traversal
    while queue:

        # Pop front node from queue
        node, hd = queue.popleft()

        # IMPORTANT:
        # Only store FIRST node of every HD
        # because top view needs top-most node
        if hd not in top_nodes:
            top_nodes[hd] = node.val

        # Move left
        # Left child HD = current HD - 1
        if node.left:
            queue.append((node.left, hd - 1))

        # Move right
        # Right child HD = current HD + 1
        if node.right:
            queue.append((node.right, hd + 1))

    # Sort by horizontal distance
    # because output should be left -> right
    result = []

    for hd in sorted(top_nodes):
        result.append(top_nodes[hd])

    return result


# ---------------- DRIVER CODE ----------------

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(4)

root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

print(topView(root))













# Example Tree:

#           1
#         /   \
#        2     3
#         \   / \
#          4 5   6

# Top View:

# 2 1 3 6

# Why?

# Column -1 → 2
# Column 0 → 1
# Column +1 → 3
# Column +2 → 6

# Nodes 4 and 5 are hidden behind top nodes.

# EASY LOGIC

# We use:

# BFS (Level Order Traversal) → because top node comes first
# Horizontal Distance (HD)

# Rules:

# Root HD = 0
# Left child HD = parent - 1
# Right child HD = parent + 1