class Solution:
    def binaryTreePaths(self, root):
        ans = []

        def dfs(node, path):
            if not node:
                return

            if path:
                path += "->"
            path += str(node.val)

            if not node.left and not node.right:
                ans.append(path)
                return

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return ans