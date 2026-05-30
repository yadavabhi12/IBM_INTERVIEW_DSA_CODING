from collections import deque

# Tree Node class
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bottomView(root):

    # If tree is empty
    if not root:
        return []

    # Dictionary
    # key   = horizontal distance
    # value = latest(bottom-most) node
    bottom_nodes = {}

    # Queue for BFS
    # Store:
    # (node, horizontal_distance)
    queue = deque()

    # Root starts from HD = 0
    queue.append((root, 0))

    # BFS traversal
    while queue:

        # Pop front element
        node, hd = queue.popleft()

        # IMPORTANT:
        # Always overwrite
        # because bottom-most node should remain
        bottom_nodes[hd] = node.val

        # Go left
        # HD decreases
        if node.left:
            queue.append((node.left, hd - 1))

        # Go right
        # HD increases
        if node.right:
            queue.append((node.right, hd + 1))

    # Final answer
    result = []

    # Sort by HD
    for hd in sorted(bottom_nodes):
        result.append(bottom_nodes[hd])

    return result


# ---------------- DRIVER CODE ----------------

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(4)

root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

print(bottomView(root))