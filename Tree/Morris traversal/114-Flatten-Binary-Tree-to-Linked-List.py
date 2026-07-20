# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        while root:
            # left part does not exit
            if not root.left:
                root=root.right

            # left part exit
            else:
                cur=root.left
                while cur.right!=None :
                    cur=cur.right
                
                cur.right=root.right
                root.right=root.left
                root.left=None
                root=root.right
        
        