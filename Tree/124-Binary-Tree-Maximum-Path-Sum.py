class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")

        def dfs(root):
            if not root:
                return 0

            l = max(0, dfs(root.left))
            r = max(0, dfs(root.right))

            self.ans = max(self.ans, l + r + root.val)

            return root.val + max(l, r)

        dfs(root)
        return self.ans