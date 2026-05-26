from collections import deque

class tree:

    def __init__(self, d):

        self.data = d
        self.left = None
        self.right = None


    def top_view(self, root):

        if root is None:
            return

        m = {}

        # queue stores tuple (node, horizontal distance)
        q = deque()

        q.append((root, 0))

        while q:

            node, d = q.popleft()

            if d not in m:
                m[d] = node.data

            if node.left:
                q.append((node.left, d - 1))

            if node.right:
                q.append((node.right, d + 1))

        for key in sorted(m):
            print(m[key], end=" ")


r = tree(2)

r.left = tree(3)
r.right = tree(4)

r.left.left = tree(5)
r.left.right = tree(6)

r.right.left = tree(7)
r.right.right = tree(8)

r.top_view(r)