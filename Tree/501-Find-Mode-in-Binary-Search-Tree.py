class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        self.prev = None
        self.count = 0
        self.max_count = 0

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            # Same value as previous
            if self.prev is not None and self.prev == node.val:
                self.count += 1
            else:
                self.count = 1

            # New maximum frequency found
            if self.count > self.max_count:
                self.max_count = self.count
                ans.clear()
                ans.append(node.val)

            # Same maximum frequency
            elif self.count == self.max_count:
                ans.append(node.val)

            self.prev = node.val

            inorder(node.right)

        inorder(root)

        return ans
    


    '''501. Find Mode in Binary Search Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]'''