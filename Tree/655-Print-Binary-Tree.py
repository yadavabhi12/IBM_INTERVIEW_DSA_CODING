class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        # Find number of levels
        def height(node):
            if node is None:
                return 0

            return 1 + max(height(node.left), height(node.right))

        h = height(root)

        rows = h
        cols = (2 ** h) - 1

        ans = [["" for _ in range(cols)] for _ in range(rows)]

        def dfs(node, row, left, right):
            if node is None:
                return

            # Current node goes in the middle
            mid = (left + right) // 2

            ans[row][mid] = str(node.val)

            # Left subtree gets left half
            dfs(node.left, row + 1, left, mid - 1)

            # Right subtree gets right half
            dfs(node.right, row + 1, mid + 1, right)

        dfs(root, 0, 0, cols - 1)

        return ans
    


    '''655. Print Binary Tree
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res.

 

Example 1:


Input: root = [1,2]
Output: 
[["","1",""],
 ["2","",""]]
Example 2:


Input: root = [1,2,3,null,4]
Output: 
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]'''