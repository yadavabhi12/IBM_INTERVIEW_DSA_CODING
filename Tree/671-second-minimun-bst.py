class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        first = root.val
        self.ans = float('inf')

        def dfs(node):
            if not node:
                return

            if first < node.val < self.ans:
                self.ans = node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans if self.ans != float('inf') else -1