# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

# Return the minimum number of cameras needed to monitor all nodes of the tree.

 

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        cameras = 0

        def dfs(node):
            nonlocal cameras

            if not node:
                return 2          # Null nodes are considered covered.

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                cameras += 1
                return 1          # Place camera here

            if left == 1 or right == 1:
                return 2          # Covered by child camera

            return 0              # Needs camera

        if dfs(root) == 0:
            cameras += 1

        return cameras