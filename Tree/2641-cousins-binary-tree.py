from collections import deque

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # First BFS: calculate level sums
        levelSum = []

        q = deque([root])

        while q:
            total = 0

            for _ in range(len(q)):
                node = q.popleft()

                total += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            levelSum.append(total)

        # Second BFS: replace values
        root.val = 0

        q = deque([root])

        level = 0

        while q:

            for _ in range(len(q)):

                node = q.popleft()

                childSum = 0

                if node.left:
                    childSum += node.left.val

                if node.right:
                    childSum += node.right.val

                if node.left:
                    node.left.val = levelSum[level + 1] - childSum
                    q.append(node.left)

                if node.right:
                    node.right.val = levelSum[level + 1] - childSum
                    q.append(node.right)

            level += 1

        return root