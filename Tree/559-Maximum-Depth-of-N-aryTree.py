# 559. Maximum Depth of N-ary Tree



class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        m = 0

        def depth(root, h):
            nonlocal m

            if root is None:
                return

            m = max(m, h)

            for child in root.children:
                depth(child, h + 1)

        depth(root, 1)

        return m