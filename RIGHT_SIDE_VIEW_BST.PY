# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def view(self,root,l,h):
        if root is None:
            return
        if len(l)==h:
            l.append(root.val)
        self.view(root.right,l,h+1)
        self.view(root.left,l,h+1)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        self.view(root,l,0)
        return l