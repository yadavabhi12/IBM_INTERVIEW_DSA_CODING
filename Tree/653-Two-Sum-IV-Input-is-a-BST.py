# this my code first time i am trying to solve this problem




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(s,r,k,d):
        if r is None:
            return False
        if r.val in d:
            return True
        else :
            t=k-r.val
            d[t]=t
        
        return s.find(r.left,k,d) or s.find(r.right,k,d)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        d={}
        return self.find(root,k,d)
    












#     Aur bhi Better Version (Most Common Interview Solution)

# Ye complements store nahi karta, values store karta hai.

class Solution:
    def dfs(self, node, k, seen):
        if not node:
            return False

        if k - node.val in seen:
            return True

        seen.add(node.val)

        return self.dfs(node.left, k, seen) or \
               self.dfs(node.right, k, seen)

    def findTarget(self, root, k):
        return self.dfs(root, k, set())
