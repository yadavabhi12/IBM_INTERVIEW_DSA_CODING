"""
===============================================================================
LeetCode 1932 - Merge BSTs to Create Single BST
===============================================================================

PROBLEM
-------
You are given several SMALL Binary Search Trees.

Each tree has at most 3 nodes.

Your task is to merge all these small BSTs into ONE valid BST.

Merge Rule:

A leaf node of one tree can be replaced by another tree
ONLY IF

leaf value == root value of another tree.

Every tree can be used only once.

Finally,

Exactly ONE valid BST should remain.

Otherwise return NULL.


===============================================================================
EXAMPLE
===============================================================================

Input

Tree1

      2
     / \
    1   3

Tree2

      3
       \
        5

Tree3

      5
     /
    4


Merge


      2
     / \
    1   3
         \
          5
         /
        4


Output

Valid BST


===============================================================================
KEY OBSERVATION
===============================================================================

Every merge happens

Leaf

↓

Root

Never

Root

↓

Middle Node


Therefore

Only LEAF values can be merged with ROOT values.


===============================================================================
STEP 1
===============================================================================

Store every tree root.

HashMap

value -> Tree


Example

2 -> Tree1

3 -> Tree2

5 -> Tree3


Now

Whenever we see leaf value 3

We immediately know

Tree2 should be attached.


Lookup

O(1)


===============================================================================
STEP 2
===============================================================================

Find the FINAL ROOT

Suppose

Root values

2
3
5


Leaves

1
3
4
5


Notice

3 appears as leaf

5 appears as leaf

Only

2

never appears as leaf.


Therefore

2

must be the final root.


If

No unique root exists

Return NULL.


===============================================================================
STEP 3
===============================================================================

DFS Merge
===============================================================================

Start DFS from final root.

Whenever current node is

Leaf

AND

Its value exists in HashMap

Attach that tree.


Example

        2
       / \
      1   3

HashMap

3 ->

      3
       \
        5


Replace

Leaf 3


Result

        2
       / \
      1   3
           \
            5


Remove

3

from HashMap

because every tree can be used only once.


===============================================================================
STEP 4
===============================================================================

BST Validation

While doing DFS

Maintain

Lower Bound

Upper Bound


Every node must satisfy

low < value < high


Example

        4
       / \
      2   7


Left subtree

(-∞,4)

Right subtree

(4,+∞)


This guarantees

Merged tree is still a valid BST.


===============================================================================
DFS VISUALIZATION
===============================================================================

           2
         /   \
        1     3

Visit

2

↓

Visit Left

↓

1

Leaf

No tree

Return

↓

Visit Right

↓

3

Leaf

Tree exists

Attach

↓

Continue DFS


===============================================================================
HASHMAP STATE
===============================================================================

Initially

{

2

3

5

}

Merge 3

{

2

5

}

Merge 5

{

2

}


Finally

Only root remains.

Success.


===============================================================================
FAILURE CASES
===============================================================================

1.

Multiple possible roots

Impossible

Return NULL


----------------------------------------------------

2.

Cycle formed

DFS detects duplicate usage

Return NULL


----------------------------------------------------

3.

BST property breaks

Return NULL


----------------------------------------------------

4.

Some trees never merged

HashMap not empty

Return NULL


===============================================================================
ALGORITHM
===============================================================================

1.

Store every root in HashMap.

2.

Collect every leaf value.

3.

Find unique root.

4.

DFS

Whenever leaf value matches HashMap

Attach subtree.

5.

Validate BST simultaneously.

6.

If all trees used

Return root

Else

Return NULL.


===============================================================================
TIME COMPLEXITY
===============================================================================

Building HashMap

O(N)

DFS

O(N)

Overall

O(N)


===============================================================================
SPACE COMPLEXITY
===============================================================================

HashMap

O(N)

Recursion

O(H)


Overall

O(N)


===============================================================================
IMPORTANT INTERVIEW POINT
===============================================================================

This problem is NOT about building a BST.

It is about

HashMap

+

BST Validation

+

DFS

+

Tree Merging


The biggest trick is finding the UNIQUE ROOT.

Without that,

DFS cannot even start.


===============================================================================
PATTERN
===============================================================================

Multiple Small Trees

↓

HashMap(root)

↓

Find Unique Root

↓

DFS Merge

↓

BST Validation

↓

One Valid BST

===============================================================================
"""







from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:

        # root value -> tree
        rootMap = {}

        # Count every value occurrence
        indegree = {}

        for root in trees:
            rootMap[root.val] = root
            indegree[root.val] = indegree.get(root.val, 0)

            if root.left:
                indegree[root.left.val] = indegree.get(root.left.val, 0) + 1

            if root.right:
                indegree[root.right.val] = indegree.get(root.right.val, 0) + 1

        # Find unique root
        root = None

        for tree in trees:
            if indegree[tree.val] == 0:
                root = tree
                break

        if root is None:
            return None

        # DFS + Merge + BST Validation
        def dfs(node, low, high):

            if node is None:
                return True

            # BST validation
            if node.val <= low or node.val >= high:
                return False

            # Merge if current node is a leaf
            if node.left is None and node.right is None:

                if node.val in rootMap and rootMap[node.val] != node:

                    mergeTree = rootMap.pop(node.val)

                    node.left = mergeTree.left
                    node.right = mergeTree.right

            return (
                dfs(node.left, low, node.val)
                and
                dfs(node.right, node.val, high)
            )

        # Remove final root from map
        rootMap.pop(root.val)

        if not dfs(root, float("-inf"), float("inf")):
            return None

        # All trees must be merged
        if rootMap:
            return None

        return root