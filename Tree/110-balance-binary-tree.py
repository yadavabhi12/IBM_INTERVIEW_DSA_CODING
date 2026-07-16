class Solution:
    def height(self, root):
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        if not root:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)