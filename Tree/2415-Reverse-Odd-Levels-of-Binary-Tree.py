"""
===============================================================================
LeetCode 2415 - Reverse Odd Levels of Binary Tree
===============================================================================

PROBLEM:
--------
Given the root of a PERFECT binary tree, reverse the node VALUES at every
odd level of the tree.

Important:
We are NOT changing the structure of the tree.
We only swap/reverse the VALUES of nodes present at odd levels.


LEVEL NUMBERING:
----------------

Root starts at Level 0.

Example:

                    2                 Level 0 (Even)
                  /   \
                3       5             Level 1 (Odd)
               / \     / \
              8  13   21  34          Level 2 (Even)


At Level 1:

Before:
3, 5

After reversing:
5, 3


Final tree:

                    2
                  /   \
                5       3
               / \     / \
              8  13   21  34


===============================================================================
IMPORTANT OBSERVATION
===============================================================================

The tree is a PERFECT binary tree.

Because of this, nodes can be processed as MIRROR PAIRS.

Example:

                    1
                 /     \
                2       3
              /  \     /  \
             4    5   6    7


Mirror pairs:

Level 1:
                2 <------> 3

Level 2:
                4 <------> 7
                5 <------> 6


To move through mirror pairs recursively:

left.left   <----> right.right

left.right  <----> right.left


That's why recursion is:

dfs(left.left,  right.right)
dfs(left.right, right.left)


===============================================================================
APPROACH 1 - RECURSIVE MIRROR DFS
===============================================================================

This is the cleanest solution for this problem.

Instead of traversing one node at a time, traverse TWO mirror nodes together.

Start with:

root.left and root.right

These nodes are at Level 1.


For every mirror pair:

1. If current level is odd:
       swap their VALUES.

2. Move deeper using mirror positions:

       left.left  <-> right.right
       left.right <-> right.left


IMPORTANT:

We swap:

    left.val, right.val

We DO NOT swap:

    left, right

because the problem asks us to reverse VALUES, not modify the tree structure.


Example:

                    1
                 /     \
                2       3
              /  \     /  \
             4    5   6    7


dfs(2, 3, level=1)

Level 1 is odd:

2.val <-> 3.val


Then:

dfs(4, 7, level=2)
dfs(5, 6, level=2)

Level 2 is even, so values are not swapped.


TIME COMPLEXITY:
----------------
O(N)

Every node is processed at most once.


SPACE COMPLEXITY:
-----------------
O(H)

H = height of the tree.

For a perfect binary tree:

H = O(log N)

Therefore recursion stack:

O(log N)


===============================================================================
SOLUTION 1 - RECURSIVE MIRROR DFS
===============================================================================
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def reverseOddLevels(self, root):

        def dfs(left, right, level):

            # Base condition
            if left is None or right is None:
                return

            # Reverse values only on odd levels
            if level % 2 == 1:
                left.val, right.val = right.val, left.val

            # Process mirror pairs
            dfs(left.left, right.right, level + 1)
            dfs(left.right, right.left, level + 1)

        # root.left and root.right are on Level 1
        dfs(root.left, root.right, 1)

        return root


"""
===============================================================================
APPROACH 2 - BFS / LEVEL ORDER TRAVERSAL
===============================================================================

Another intuitive solution is Level Order Traversal using a queue.

For every level:

1. Store all nodes of that level.
2. Check whether the level is odd.
3. If odd:
       reverse the VALUES using two pointers.

Example:

Level:

        4    5    6    7

Store:

nodes = [4, 5, 6, 7]

Use:

left = 0
right = 3


Swap:

4 <-> 7

then:

5 <-> 6


Result:

7, 6, 5, 4


NOTE:
Again, we reverse VALUES.
We do not reverse actual node pointers.


TIME COMPLEXITY:
----------------
O(N)

Every node enters and leaves the queue once.


SPACE COMPLEXITY:
-----------------
O(N)

At the widest level, the queue can contain approximately N/2 nodes.

Therefore:

O(N)


===============================================================================
SOLUTION 2 - BFS
===============================================================================
"""


from collections import deque


class SolutionBFS:
    def reverseOddLevels(self, root):

        if root is None:
            return None

        q = deque([root])

        level = 0

        while q:

            size = len(q)
            nodes = []

            # Process one complete level
            for _ in range(size):

                node = q.popleft()

                nodes.append(node)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            # Reverse values on odd levels
            if level % 2 == 1:

                left = 0
                right = len(nodes) - 1

                while left < right:

                    nodes[left].val, nodes[right].val = (
                        nodes[right].val,
                        nodes[left].val
                    )

                    left += 1
                    right -= 1

            level += 1

        return root


"""
===============================================================================
APPROACH 3 - BFS WITH VALUE ARRAY
===============================================================================

This is another BFS variation.

Instead of directly using two pointers on the nodes, we can:

1. Collect all nodes of the current level.
2. Extract their values.
3. Reverse the values.
4. Assign reversed values back to the nodes.

Example:

nodes:

[A, B, C, D]

values:

[4, 5, 6, 7]

reverse:

[7, 6, 5, 4]

assign back:

A.val = 7
B.val = 6
C.val = 5
D.val = 4


This approach is easy to understand, but it uses an additional values list.

TIME:
O(N)

SPACE:
O(N)


===============================================================================
SOLUTION 3 - BFS + REVERSED VALUE LIST
===============================================================================
"""


class SolutionBFSValues:
    def reverseOddLevels(self, root):

        if root is None:
            return None

        q = deque([root])

        level = 0

        while q:

            size = len(q)
            nodes = []

            for _ in range(size):

                node = q.popleft()
                nodes.append(node)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if level % 2 == 1:

                values = [node.val for node in nodes]

                values.reverse()

                for i in range(len(nodes)):
                    nodes[i].val = values[i]

            level += 1

        return root


"""
===============================================================================
APPROACH 4 - DFS: COLLECT NODES LEVEL-WISE, THEN REVERSE
===============================================================================

We can also use normal DFS.

During DFS:

Store nodes according to their level.

Example:

levels[0] = [1]
levels[1] = [2, 3]
levels[2] = [4, 5, 6, 7]


After DFS completes:

For every odd level:

reverse node values.


This works, but requires extra storage for all levels.

TIME:
O(N)

SPACE:
O(N)

This is simpler conceptually but less optimized than mirror DFS.


===============================================================================
SOLUTION 4 - DFS + LEVEL STORAGE
===============================================================================
"""


class SolutionDFSLevels:
    def reverseOddLevels(self, root):

        levels = []

        def dfs(node, level):

            if node is None:
                return

            if level == len(levels):
                levels.append([])

            levels[level].append(node)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        # Reverse values on odd levels
        for level in range(1, len(levels), 2):

            nodes = levels[level]

            left = 0
            right = len(nodes) - 1

            while left < right:

                nodes[left].val, nodes[right].val = (
                    nodes[right].val,
                    nodes[left].val
                )

                left += 1
                right -= 1

        return root


"""
===============================================================================
WHY THE ORIGINAL SUBTREE-SWAPPING IDEA DOES NOT WORK
===============================================================================

A tempting approach is:

if level is odd:
    swap(root.left, root.right)

But this changes the TREE STRUCTURE.

The question only asks to reverse node VALUES.

Wrong idea:

        root.left = root.right
        root.right = old_left

This moves complete subtrees.


Correct idea:

        left.val, right.val = right.val, left.val

Only values change.


===============================================================================
WHY MIRROR DFS IS POSSIBLE
===============================================================================

This problem specifically gives us a PERFECT binary tree.

That means every internal node has exactly two children and all leaf nodes
are at the same level.

Because of this symmetry:

                    root
                  /      \
               LEFT      RIGHT


The outside children are mirror nodes:

LEFT.left <----------> RIGHT.right


The inside children are mirror nodes:

LEFT.right <---------> RIGHT.left


Therefore:

dfs(left.left, right.right)
dfs(left.right, right.left)


===============================================================================
COMMON MISTAKES
===============================================================================

1. Starting level from 0 after passing root.left/root.right.

Wrong:

    dfs(root.left, root.right, 0)

Because root is Level 0.

Therefore:

root.left and root.right are Level 1.

Correct:

    dfs(root.left, root.right, 1)


-------------------------------------------------------------------------------

2. Putting recursion only inside else.

Wrong:

    if level % 2 == 1:
        swap values
    else:
        dfs(...)

This causes recursion to STOP after an odd level.


Correct:

    if level % 2 == 1:
        swap values

    dfs(...)
    dfs(...)


Recursion must continue for BOTH odd and even levels.


-------------------------------------------------------------------------------

3. Traversing the same mirror pair twice.

Wrong:

    dfs(left.left, right.right)
    dfs(right.right, left.left)


Correct:

    dfs(left.left, right.right)
    dfs(left.right, right.left)


-------------------------------------------------------------------------------

4. Checking root inside the recursive helper.

Wrong:

    def dfs(left, right):
        if root is None:
            return


`root` never changes during recursion.

Correct:

    if left is None or right is None:
        return


-------------------------------------------------------------------------------

5. Returning the helper result.

Wrong:

    return dfs(root.left, root.right, 1)

The helper does not return the tree.
It modifies values in-place.

Correct:

    dfs(root.left, root.right, 1)

    return root


===============================================================================
QUICK REVISION / INTERVIEW NOTES
===============================================================================

Problem:
Reverse values at odd levels of a perfect binary tree.

Do NOT:
Swap nodes/subtrees.

Do:
Swap node values.


BEST APPROACH:

Use two pointers/nodes representing mirror positions.

Start:

    dfs(root.left, root.right, 1)


Odd Level:

    left.val, right.val = right.val, left.val


Move to next mirror pairs:

    dfs(left.left, right.right, level + 1)

    dfs(left.right, right.left, level + 1)


Visual:

                    1
                 /     \
                2  <->  3
              /  \     /  \
             4    5   6    7
             ^    ^   ^    ^
             |    |   |    |
             +----|---|----+
                  |   |
                  +---+

Mirror:

2 <-> 3

4 <-> 7
5 <-> 6


===============================================================================
APPROACH COMPARISON
===============================================================================

1. Mirror DFS
   Time  : O(N)
   Space : O(log N) recursion stack
   Best / Recommended for this problem.

2. BFS + Two Pointers
   Time  : O(N)
   Space : O(N)
   Very intuitive and easy to explain.

3. BFS + Value Array
   Time  : O(N)
   Space : O(N)
   Easy but uses an additional list of values.

4. DFS + Level Storage
   Time  : O(N)
   Space : O(N)
   General level-based solution, but uses more memory.


===============================================================================
PATTERN TO REMEMBER
===============================================================================

Binary Tree
    +
Perfect Binary Tree
    +
Mirror Traversal
    +
Odd/Even Level
    +
Swap Values


Whenever a perfect/symmetric binary tree problem asks us to compare or modify
nodes from opposite sides, think about traversing TWO nodes simultaneously:

    left.left   with right.right

    left.right  with right.left


===============================================================================
FINAL RECOMMENDED SOLUTION FOR GITHUB / INTERVIEW
===============================================================================


class Solution:
    def reverseOddLevels(self, root):

        def dfs(left, right, level):

            if left is None or right is None:
                return

            if level % 2 == 1:
                left.val, right.val = right.val, left.val

            dfs(left.left, right.right, level + 1)
            dfs(left.right, right.left, level + 1)

        dfs(root.left, root.right, 1)

        return root


Time Complexity  : O(N)
Space Complexity : O(log N)

===============================================================================
"""