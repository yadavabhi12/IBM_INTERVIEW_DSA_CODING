"""
===============================================================================
LeetCode 331 - Verify Preorder Serialization of a Binary Tree
===============================================================================

PROBLEM
-------
Given a preorder serialization of a binary tree, determine whether it is valid.

The serialization consists of comma-separated values.

Numbers represent actual tree nodes.

'#' represents a NULL node.

IMPORTANT:
-----------
We DO NOT reconstruct the tree.
We only verify whether the preorder string can represent a valid binary tree.


Example 1
---------

Input

9,3,4,#,#,1,#,#,2,#,6,#,#


Tree

          9
        /   \
       3     2
      / \     \
     4   1     6


Output

True


-------------------------------------------------------------------------------

Example 2

Input

1,#


Tree

    1
   /
 NULL

Right child missing.

Output

False


-------------------------------------------------------------------------------

Example 3

Input

9,#,#,1


Tree

9

Serialization already finished.

Extra node "1" appears afterwards.

Output

False


===============================================================================
INTUITION
===============================================================================

Instead of constructing the tree,
think in terms of CHILD SLOTS.

Every node needs exactly ONE incoming slot.

Every non-null node creates TWO outgoing slots.

Every NULL node creates ZERO slots.


Initially

There is only ONE slot available for the ROOT.


slots = 1


===============================================================================
RULES
===============================================================================

Whenever we read one token:

Step 1

Use one slot.

slots -= 1


If slots become negative

Serialization is invalid.


---------------------------------------------------------

If token is NOT '#'

It creates two children.

slots += 2


If token is '#'

Nothing is added.


===============================================================================
VISUALIZATION
===============================================================================

Example

9,3,4,#,#,1,#,#,2,#,6,#,#


Initially

slots = 1


Read 9

Use one slot

1 -> 0

Create two children

0 -> 2


slots = 2


----------------------------------------------------

Read 3

Use one

2 -> 1

Create two

1 -> 3


slots = 3


----------------------------------------------------

Read 4

Use one

3 -> 2

Create two

2 -> 4


slots = 4


----------------------------------------------------

Read #

Use one slot

4 -> 3

NULL creates nothing


slots = 3


----------------------------------------------------

Read #

3 -> 2


----------------------------------------------------

Read 1

2 -> 1

Create two

1 -> 3


----------------------------------------------------

Read #

3 -> 2


----------------------------------------------------

Read #

2 -> 1


----------------------------------------------------

Read 2

1 -> 0

Create two

0 -> 2


----------------------------------------------------

Read #

2 -> 1


----------------------------------------------------

Read 6

1 -> 0

Create two

0 -> 2


----------------------------------------------------

Read #

2 -> 1


----------------------------------------------------

Read #

1 -> 0


Finished

slots == 0

Valid Serialization


===============================================================================
INVALID CASE
===============================================================================

Input

9,#,#,1


Initially

slots = 1


9

1 -> 2


#


2 -> 1


#


1 -> 0


Serialization should finish here.

But another node exists.


Read 1

Need one slot

0 -> -1

Negative slot

INVALID


===============================================================================
WHY DOES THIS WORK?
===============================================================================

Every node occupies exactly one position in the tree.

Every non-null node opens two new positions.

Every null node closes one position forever.

If slots become negative

Means

There is no place available to attach the current node.

Hence invalid.


===============================================================================
CODE
===============================================================================

class Solution:

    def isValidSerialization(self, preorder: str) -> bool:

        slots = 1

        for node in preorder.split(','):

            slots -= 1

            if slots < 0:
                return False

            if node != '#':
                slots += 2

        return slots == 0


===============================================================================
TIME COMPLEXITY
===============================================================================

Split string

O(N)

Traverse once

O(N)

Overall

O(N)


===============================================================================
SPACE COMPLEXITY
===============================================================================

O(1)

Ignoring split() output.

If counting split list,

O(N).


===============================================================================
INTERVIEW NOTES
===============================================================================

Do NOT build the tree.

Think in terms of

AVAILABLE CHILD SLOTS.

Rules:

Number

Consumes 1 slot
Creates 2 slots

Net Change

+1


'#'

Consumes 1 slot

Creates 0 slots

Net Change

-1


Initially

slots = 1

Finally

slots must become exactly 0.

If slots become negative anytime

Serialization is invalid.


===============================================================================
PATTERN
===============================================================================

Tree Verification

↓

Incoming Slot

↓

Outgoing Slots

↓

Greedy Counting

↓

No Tree Construction Required

===============================================================================
"""