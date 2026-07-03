# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





# my first solution is to find the leaves of both trees and compare them. If they are the same, then the trees are leaf-similar.
class Solution:
    def leavesNode(self,root,l):
        if root is None:
            return l
        if root.left is None and root.right is None:
            l.append(root.val)
            return l
        self.leavesNode(root.left,l)
        self.leavesNode(root.right,l)
        return l
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
      l=  self.leavesNode(root1,[])
      n= self.leavesNode(root2,[])
      print(l)
      print(n)
      if len(l)!=len(n):
        return False
      for i in range(len(l)):
        if l[i]!=n[i]:
            return False
      return True
    






#  this approach, we can simplify the code significantly. 
class Solution:
    def leaves(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        return self.leaves(root.left) + self.leaves(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leaves(root1) == self.leaves(root2)
    

        