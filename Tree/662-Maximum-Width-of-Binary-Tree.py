from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        queue = deque([(root, 0)])
        ans = 0

        while queue:

            level_size = len(queue)

            # First index of current level
            base = queue[0][1]

            for _ in range(level_size):

                node, idx = queue.popleft()

                # Normalize index
                idx -= base

                # First node of this level
                if _ == 0:
                    first = idx

                # Last node of this level
                if _ == level_size - 1:
                    last = idx

                # Add children .
                if node.left:
                    queue.append((node.left, 2 * idx + 1))

                if node.right:
                    queue.append((node.right, 2 * idx + 2))

            ans = max(ans, last - first + 1)

        return ans