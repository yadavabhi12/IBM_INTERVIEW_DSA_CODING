# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(
        self, 
        inorder: List[int], 
        postorder: List[int]
    ) -> Optional[TreeNode]:

        # Store inorder positions
        mp = {}

        for i in range(len(inorder)):
            mp[inorder[i]] = i

        # Start from last element of postorder
        self.index = len(postorder) - 1

        def construct(start, end):
            if start > end:
                return None

            # Last element of postorder is root
            val = postorder[self.index]
            self.index -= 1

            root = TreeNode(val)

            # Find root position in inorder
            pos = mp[val]

            # IMPORTANT: First construct RIGHT
            root.right = construct(pos + 1, end)

            # Then construct LEFT
            root.left = construct(start, pos - 1)

            return root

        return construct(0, len(inorder) - 1)