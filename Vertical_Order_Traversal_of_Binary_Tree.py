from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root):
    if not root:
        return []

    column_table = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
        node, column = queue.popleft()

        column_table[column].append(node.val)

        if node.left:
            queue.append((node.left, column - 1))

        if node.right:
            queue.append((node.right, column + 1))

    result = []

    for col in sorted(column_table.keys()):
        result.append(column_table[col])

    return result


# Example
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(verticalTraversal(root))
