'''965. Univalued Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: root = [2,2,2,5,2]
Output: false
 '''








# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # root is None 
        if not root :
           return True
        # left side and right sine not None then check parent and children value same or not if not same return False 
        if  root.left!=None and root.left.val!=root.val or root.right!=None and root.right.val!=root.val:
            return False
        
        return self.isUnivalTree(root.left)and self.isUnivalTree(root.right)

        

     """  time complexity is O(n) where n is number of nodes in the tree
        Time: O(n)
Space:  O(h) recursion stack.
"""

# this approach interview best approach is to use DFS and check if all nodes have the same value as the root node. If any node has a different value, return False. Otherwise, return True.

class Solution:
    def isUnivalTree(self, root):
        target = root.val

        def dfs(node):
            if not node:
                return True

            if node.val != target:
                return False

            return dfs(node.left) and dfs(node.right)

        return dfs(root)
    










#     3. Iterative DFS — Stack

# Recursion zaroori nahi hai. Stack use karke bhi kar sakte ho.

class Solution:
    def isUnivalTree(self, root):
        if not root:
            return True

        value = root.val
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val != value:
                return False

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return True