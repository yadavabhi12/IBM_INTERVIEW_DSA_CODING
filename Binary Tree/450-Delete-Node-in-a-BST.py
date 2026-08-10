class Solution:

    def deleteNode(self, root: Optional[TreeNode],
                   key: int) -> Optional[TreeNode]:

        # Node not found
        if root is None:
            return None

        # Search in left subtree
        if key < root.val:

            root.left = self.deleteNode(
                root.left,
                key
            )

        # Search in right subtree
        elif key > root.val:

            root.right = self.deleteNode(
                root.right,
                key
            )

        # Node found
        else:

            # Case 1:
            # No left child
            if root.left is None:
                return root.right

            # Case 2:
            # No right child
            if root.right is None:
                return root.left

            # Case 3:
            # Two children

            # Find inorder successor
            successor = root.right

            while successor.left:
                successor = successor.left

            # Copy successor value
            root.val = successor.val

            # Delete successor
            root.right = self.deleteNode(
                root.right,
                successor.val
            )

        return root
    






    '''"""
===============================================================================
LeetCode 450 - Delete Node in a BST
===============================================================================

PROBLEM
-------
Given the root of a Binary Search Tree and a key, delete the node containing
that key and return the root of the BST.

After deletion, the resulting tree must STILL be a valid BST.


===============================================================================
BST PROPERTY
===============================================================================

For every node:

        LEFT < ROOT < RIGHT


Example:

          5
        /   \
       3     7
      / \   / \
     2   4 6   8


If key = 3

We have to remove node 3 while maintaining BST property.


===============================================================================
THERE ARE 3 CASES
===============================================================================


CASE 1: Node is a LEAF
----------------------

        5
       /
      3

If 3 has no children:

        5


Simply remove it.

Return None for that node.


===============================================================================
CASE 2: Node has ONE CHILD
--------------------------

        5
       /
      3
       \
        4


Delete 3.

We can directly connect its parent to its child:

        5
       /
      4


If node has:

LEFT child only

Return node.left


If node has:

RIGHT child only

Return node.right


===============================================================================
CASE 3: Node has TWO CHILDREN
-----------------------------

This is the important case.

        5
       / \
      3   8
         /
        6


Suppose we delete 5.


We cannot simply remove it because both subtrees need to remain.

We need a replacement.


There are two choices:

1. Inorder Successor
2. Inorder Predecessor


===============================================================================
INORDER SUCCESSOR
===============================================================================

The inorder successor is:

SMALLEST value in the RIGHT subtree.


Example:

        5
       / \
      3   8
         /
        6
       /
      5.5


If deleting 5,

Right subtree:

8
/
6
/
5.5


Smallest = 5.5

So replace 5 with 5.5.


===============================================================================
WHY SUCCESSOR?
===============================================================================

We need a value that is:

Greater than everything in LEFT subtree

AND

Smaller than everything else in RIGHT subtree.


The smallest value from the right subtree satisfies this.


===============================================================================
ALGORITHM
===============================================================================

1.

Search for key using BST property.

If

key < root.val

Go LEFT.


If

key > root.val

Go RIGHT.


If

key == root.val

We found the node.


---------------------------------------------------

2.

Check children.


No child

↓

return None


---------------------------------------------------

One child

↓

return that child


---------------------------------------------------

Two children

↓

Find inorder successor.

↓

Copy successor value into current node.

↓

Delete successor from RIGHT subtree.


===============================================================================
IMPORTANT IDEA
===============================================================================

When we copy successor value:

        5
       / \
      3   8
         /
        6


Successor = 6


Become:

        6
       / \
      3   8
         /
        6


Now there are TWO 6s.


So we must delete the original 6.


        6
       / \
      3   8


===============================================================================
CODE - RECURSIVE
===============================================================================

class Solution:

    def deleteNode(self, root: Optional[TreeNode],
                   key: int) -> Optional[TreeNode]:

        # Node not found
        if root is None:
            return None

        # Search in left subtree
        if key < root.val:

            root.left = self.deleteNode(
                root.left,
                key
            )

        # Search in right subtree
        elif key > root.val:

            root.right = self.deleteNode(
                root.right,
                key
            )

        # Node found
        else:

            # Case 1:
            # No left child
            if root.left is None:
                return root.right

            # Case 2:
            # No right child
            if root.right is None:
                return root.left

            # Case 3:
            # Two children

            # Find inorder successor
            successor = root.right

            while successor.left:
                successor = successor.left

            # Copy successor value
            root.val = successor.val

            # Delete successor
            root.right = self.deleteNode(
                root.right,
                successor.val
            )

        return root


===============================================================================
DRY RUN
===============================================================================

Tree:

          5
        /   \
       3     8
      / \   / \
     2   4 6   9


Delete:

5


---------------------------------------------------

Step 1

root = 5

key = 5

Found.


5 has TWO children.


---------------------------------------------------

Step 2

Find successor.


Right subtree:

        8
       /
      6


Smallest value = 6


---------------------------------------------------

Step 3

Copy 6 into root.


Before:

          5
        /   \
       3     8
            /
           6


After:

          6
        /   \
       3     8
            /
           6


---------------------------------------------------

Step 4

Delete original 6.


Final:

          6
        /   \
       3     8
      / \     \
     2   4     9


Valid BST.


===============================================================================
WHY root.left = RECURSION RESULT?
===============================================================================

This line is extremely important:

root.left = self.deleteNode(root.left, key)


Suppose:

        5
       /
      3
     /
    2


Delete 3.


Recursive call:

deleteNode(3, 3)


returns:

2


Therefore:

root.left = 2


Result:

        5
       /
      2


The parent reconnects itself to the new subtree root.


Same for RIGHT:

root.right = self.deleteNode(root.right, key)


===============================================================================
SEARCH FLOW
===============================================================================

             5
           /   \
          3     8
         / \   / \
        2   4 6   9


Delete 6


6 > 5

↓

Go RIGHT


8

↓

6 < 8

↓

Go LEFT


6

↓

FOUND


This works because of BST ordering.


===============================================================================
TIME COMPLEXITY
===============================================================================

Searching:

O(H)


Finding successor:

O(H)


Overall:

O(H)


Balanced BST:

O(log N)


Worst-case skewed BST:

O(N)


===============================================================================
SPACE COMPLEXITY
===============================================================================

Recursive call stack:

O(H)


Balanced:

O(log N)


Worst case:

O(N)


===============================================================================
COMMON MISTAKES
===============================================================================

1.

Forgetting to reconnect the parent.

Wrong:

deleteNode(root.left, key)


Correct:

root.left = deleteNode(root.left, key)


---------------------------------------------------

2.

For two children, simply deleting the node.

Not possible.

Need successor/predecessor.


---------------------------------------------------

3.

Copying successor but NOT deleting original successor.

This creates duplicate value.


---------------------------------------------------

4.

Searching both subtrees.

Unnecessary.

BST tells us exactly where the key can exist.


===============================================================================
INTERVIEW TRICK
===============================================================================

Remember:

DELETE NODE


0 CHILDREN

↓

None


1 CHILD

↓

Return existing child


2 CHILDREN

↓

Successor

↓

Copy value

↓

Delete successor


===============================================================================
MEMORY TRICK
===============================================================================

Search

↓

Find

↓

0 child → None

1 child → Child

2 children → Successor


===============================================================================
PATTERN
===============================================================================

BST Search

+

Tree Deletion

+

Inorder Successor

+

Recursion


===============================================================================
"""'''
