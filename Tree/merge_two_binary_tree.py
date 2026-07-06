class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None

        val = 0
        if root1:
            val += root1.val
        if root2:
            val += root2.val

        node = TreeNode(val)

        node.left = self.mergeTrees(
            root1.left if root1 else None,
            root2.left if root2 else None
        )

        node.right = self.mergeTrees(
            root1.right if root1 else None,
            root2.right if root2 else None
        )

        return node
    



# jo interview question is to merge two binary trees. The solution uses a recursive approach to traverse both trees simultaneously and create a new tree with the sum of the values of the corresponding nodes. If a node is missing in one of the trees, it takes the value from the other tree. The base case for the recursion is when both nodes are None, in which case it returns None.

# best optimize version of the code is as follows:
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root










