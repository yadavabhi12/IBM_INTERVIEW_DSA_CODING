class Solution:

    def __init__(self):
        self.m = 0
        self.max = -1

    def dfs(self, root, d):

        if root is None:
            return

        if d > self.max:
            self.max = d
            self.m = root.val

        self.dfs(root.left, d + 1)
        self.dfs(root.right, d + 1)

    def findBottomLeftValue(self, root):

        self.dfs(root, 0)

        return self.m

