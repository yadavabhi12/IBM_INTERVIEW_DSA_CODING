"""
Problem: Populating Next Right Pointers in Each Node

Goal:
Connect every node to the next node on the same level using the `next` pointer.
The last node of each level should point to None.

Example:

Before:
            1
          /   \
         2     3
        / \   / \
       4   5 6   7

After connecting `next` pointers:

            1 -> None
          /   \
         2 --> 3 -> None
        / \   / \
       4 -> 5 -> 6 -> 7 -> None


Approach: BFS / Level Order Traversal

1. Use a queue to process the tree level by level.
2. `len(q)` gives the number of nodes in the current level.
3. `temp` initially points to the first node of the current level.
4. Remove nodes one by one from the queue.
5. For every node after the first node:
       temp.next = current_node
   Then move temp forward:
       temp = temp.next
6. Add the left and right children to the queue for the next level.
7. Repeat until the queue becomes empty.

Example for one level:

Queue:
[4, 5, 6, 7]

Connections created:

temp = 4

4.next = 5
temp = 5

5.next = 6
temp = 6

6.next = 7

Result:

4 -> 5 -> 6 -> 7 -> None


Why store level size?

    level_size = len(q)

Because while processing the current level, we also add children
to the queue. Storing the size beforehand ensures that the current
loop processes only the nodes belonging to the current level.


Time Complexity:
O(N) - Every node is visited once.

Space Complexity:
O(N) - Queue can contain nodes from a complete level.

Pattern:
Binary Tree + BFS + Level Order Traversal + Next Pointer
"""







# this problem to solve my first interview question on binary trees.

from collections import deque

class Solution:
    def connect(self, root):
        if root is None:
            return None

        q = deque([root])

        while q:
            level_size = len(q)
            temp = q[0]

            for i in range(level_size):
                node = q.popleft()

                if i > 0:
                    temp.next = node
                    temp = temp.next

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return root
    






# method to solve the problem using a more concise approach without using an extra variable for the previous node.



class Solution:
    def connect(self, root):
        if root is None:
            return None

        q = deque([root])

        while q:
            size = len(q)
            prev = None

            for _ in range(size):
                node = q.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return root
    







# method to solve the problem using a more concise approach without using an extra variable for the previous node.

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root is None or root.left is None:
            return root

        # Same parent connection
        root.left.next = root.right

        # Different parent connection
        if root.next:
            root.right.next = root.next.left

        # Recursively connect next levels
        self.connect(root.left)
        self.connect(root.right)

        return root