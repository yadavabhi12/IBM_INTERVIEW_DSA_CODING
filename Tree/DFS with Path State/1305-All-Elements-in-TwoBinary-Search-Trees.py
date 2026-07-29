
# my first approach is to do an in-order traversal of both trees and store the elements in a list. Then, I can merge the two lists into a single sorted list.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,l):
        if root is None:
            return 
        l.append(root.val)
        self.dfs(root.left,l)
        self.dfs(root.right,l)
        

    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        l=[]
        self.dfs(root1,l)
        self.dfs(root2,l)
        l.sort()
        return l
        


        Complexity
# DFS: O(n + m)
# Sorting: O((n + m) log(n + m))
# Total: O((n + m) log(n + m))
# Space: O(n + m)





# method 2: Optimized Approach  in which we can do an in-order traversal of both trees and merge the elements into a single sorted list without sorting at the end.

class Solution:
    def inorder(self, root, arr):
        if not root:
            return

        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)

    def merge(self, a, b):
        i = j = 0
        ans = []

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1

        ans.extend(a[i:])
        ans.extend(b[j:])

        return ans

    def getAllElements(self, root1, root2):
        a = []
        b = []

        self.inorder(root1, a)
        self.inorder(root2, b)

        return self.merge(a, b)
    



    '''Complexity
Inorder: O(n+m)
Merge: O(n+m)
Total: O(n+m)
Space: O(n+m)

This is the solution most interviewers expect.'''

















# method 3
 
'''Method 3 (Best / Advanced)

Use two stacks to perform simultaneous iterative inorder traversals.

No need to create two arrays.
Produce the answer directly.




class Solution:
    def pushLeft(self, stack, node):
        while node:
            stack.append(node)
            node = node.left

    def getAllElements(self, root1, root2):
        s1 = []
        s2 = []

        self.pushLeft(s1, root1)
        self.pushLeft(s2, root2)

        ans = []

        while s1 or s2:
            if not s2 or (s1 and s1[-1].val <= s2[-1].val):
                node = s1.pop()
                ans.append(node.val)
                self.pushLeft(s1, node.right)
            else:
                node = s2.pop()
                ans.append(node.val)
                self.pushLeft(s2, node.right)

        return ans







Complexity
Time: O(n+m)
Extra Space: O(h1+h2) (excluding the output list), where h1 and h2 are the heights of the two trees.

This is the most optimized solution because it avoids storing two intermediate sorted arrays.'''