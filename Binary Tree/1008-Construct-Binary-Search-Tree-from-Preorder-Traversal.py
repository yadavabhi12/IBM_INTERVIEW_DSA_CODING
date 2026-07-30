'''
1008. Construct Binary Search Tree from Preorder Traversal
Solved
Medium
Topics
premium lock icon
Companies
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

 

Example 1:


Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
Example 2:

Input: preorder = [1,3]
Output: [1,null,3]
 '''





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root =TreeNode(preorder[0])       # first create root tree
        def create(root,val):
            if root ==None: 
                # when root is null then create new node and return them
                return TreeNode(val)
            if root.val>val:         
                root.left=create(root.left,val)
            elif root.val<val:
                root.right=create(root.right,val)

            return root
        for i in range(1,len(preorder)):
            root= create(root,preorder[i])
        return root

        