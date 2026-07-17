class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index_map = {}
        for i, val in enumerate(inorder):
            index_map[val] = i

        self.index = 0

        def construct(start, end):
            if start > end:
                return None

            val = preorder[self.index]
            self.index += 1

            root = TreeNode(val)

            pos = index_map[val]

            root.left = construct(start, pos - 1)
            root.right = construct(pos + 1, end)

            return root

        return construct(0, len(inorder) - 1)
    















    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.preIndex = 0

        def construct(start, end):
            if start > end:
                return None

            root = TreeNode(preorder[self.preIndex])
            self.preIndex += 1

            # Linear Search
            pos = start
            while inorder[pos] != root.val:
                pos += 1

            root.left = construct(start, pos - 1)
            root.right = construct(pos + 1, end)

            return root

        return construct(0, len(inorder) - 1)
    


# Complexity
# Time: O(n²) (हर recursive call में linear search)
# Space: O(h) (recursion stack)