"""
===============================================================================
LeetCode 99 - Recover Binary Search Tree
===============================================================================

PROBLEM
-------
You are given the root of a Binary Search Tree (BST).

Exactly TWO nodes have been swapped by mistake.

Recover the BST WITHOUT changing its structure.

You should only swap back the values of the two incorrect nodes.


===============================================================================
EXAMPLE 1
===============================================================================

Original BST

      2
     / \
    1   4
       /
      3


Suppose 2 and 3 are swapped


      3
     / \
    1   4
       /
      2


Recover it back


      2
     / \
    1   4
       /
      3


===============================================================================
KEY OBSERVATION
===============================================================================

BST Inorder Traversal is ALWAYS sorted.

Example

        4
      /   \
     2     6
    / \   / \
   1  3  5  7


Inorder

1 2 3 4 5 6 7


If two nodes are swapped

Inorder is NO LONGER sorted.


===============================================================================
CASE 1 : Adjacent Swap
===============================================================================

Correct

1 2 3 4 5


Swap

3 and 4


1 2 4 3 5


Only ONE inversion exists.

4 > 3


first = 4

second = 3


Swap them back.


===============================================================================
CASE 2 : Non-Adjacent Swap
===============================================================================

Correct

1 2 3 4 5 6


Swap

2 and 5


1 5 3 4 2 6


Violations

5 > 3

4 > 2


First violation

first = 5


Last violation

second = 2


Swap

5 and 2


Recovered.


===============================================================================
INTUITION
===============================================================================

During inorder traversal

Keep previous node.

Whenever

prev.val > current.val

BST property is violated.


First violation

Store

first = prev


Every violation

Update

second = current


Finally

Swap

first.val

second.val


===============================================================================
VISUALIZATION
===============================================================================

Inorder

1 5 3 4 2 6


Traversal


prev

↓

1

No problem


-------------------

prev

↓

5

Current

↓

3

Violation

5 > 3


first = 5

second = 3


-------------------

prev

↓

4

Current

↓

2

Violation

4 > 2


Update

second = 2


Final

Swap

5 ↔ 2


===============================================================================
ALGORITHM
===============================================================================

1.

Perform inorder traversal.

↓

2.

Maintain previous node.

↓

3.

Whenever

prev.val > current.val

↓

First violation

Store first.

↓

Every violation

Update second.

↓

Traversal finishes.

↓

Swap values.


===============================================================================
CODE (Recursive)
===============================================================================

class Solution:

    def recoverTree(self, root):

        self.first = None
        self.second = None
        self.prev = TreeNode(float("-inf"))

        def inorder(node):

            if node is None:
                return

            inorder(node.left)

            if self.prev.val > node.val:

                if self.first is None:
                    self.first = self.prev

                self.second = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        self.first.val, self.second.val = (
            self.second.val,
            self.first.val
        )


===============================================================================
DRY RUN
===============================================================================

Inorder

1 5 3 4 2 6


prev=1

OK


----------------

prev=5

current=3

5>3

first=5

second=3


----------------

prev=4

current=2

4>2

second=2


Traversal Complete


Swap

5

2


Recovered


===============================================================================
WHY second IS UPDATED EVERY TIME?
===============================================================================

Adjacent Swap

1 4 3 5

Only one violation

4>3


first=4

second=3


Done


--------------------------------------------

Non Adjacent Swap

1 5 3 4 2 6


Violation 1

5>3

first=5

second=3


Violation 2

4>2

Update

second=2


Finally

Swap

5

2


===============================================================================
TIME COMPLEXITY
===============================================================================

Inorder Traversal

O(N)


===============================================================================
SPACE COMPLEXITY
===============================================================================

Recursive Stack

O(H)

Balanced BST

O(log N)

Worst Case

O(N)


===============================================================================
MORRIS TRAVERSAL (FOLLOW-UP)
===============================================================================

Interview Follow-up

Can you solve in O(1) extra space?

YES

Use Morris Inorder Traversal.

Same logic.

Instead of recursion,

perform inorder using threaded binary tree.

Time

O(N)

Space

O(1)


===============================================================================
COMMON MISTAKES
===============================================================================

❌ Swapping TreeNodes instead of values.

Only values should be swapped.

----------------------------------------

❌ Stopping after first violation.

Need to continue traversal.

----------------------------------------

❌ Updating first multiple times.

Store first ONLY once.

----------------------------------------

❌ Forgetting second should be updated
at every violation.

===============================================================================
INTERVIEW TRICK
===============================================================================

BST

↓

Inorder must be Sorted

↓

Find Inversions

↓

First inversion

Store first

↓

Last inversion

Store second

↓

Swap values


===============================================================================
MEMORY TRICK
===============================================================================

Sorted Inorder

↓

Find Disorder

↓

First = Bigger Number

↓

Second = Smaller Number

↓

Swap

===============================================================================
PATTERN
===============================================================================

BST

↓

Inorder Traversal

↓

Detect Inversion

↓

Swap Values

↓

Recover BST

===============================================================================