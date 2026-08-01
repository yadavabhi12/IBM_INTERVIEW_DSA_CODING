'''"""
===============================================================================
LeetCode 96 - Unique Binary Search Trees
===============================================================================

PROBLEM
-------
Given an integer n, return the number of structurally unique Binary Search
Trees (BSTs) that can be built using values from 1 to n.

NOTE:
Unlike LeetCode 95, we DO NOT return the actual trees.
We only return the COUNT of all unique BSTs.

Example:
---------
Input:
n = 3

Output:
5

The 5 unique BSTs are:

        1           1          2          3         3
         \           \        / \        /         /
          2           3      1   3      1         2
           \         /                  \       /
            3       2                    2     1


===============================================================================
INTUITION
===============================================================================

Instead of building every BST (Problem 95),
here we only count them.

For every number from start...end:

    Treat that number as ROOT.

Then:

    Left side can create X BSTs.

    Right side can create Y BSTs.

Total trees using this root:

    X × Y

because every left tree can combine with every right tree.


Example:

Values:

1 2 3

--------------------------------------------------

Root = 1

Left subtree:

Empty

Count = 1

Right subtree:

2,3

Count = 2

Contribution:

1 × 2 = 2

--------------------------------------------------

Root = 2

Left:

1

Count = 1

Right:

3

Count = 1

Contribution:

1 × 1 = 1

--------------------------------------------------

Root = 3

Left:

1,2

Count = 2

Right:

Empty

Count = 1

Contribution:

2 × 1 = 2

--------------------------------------------------

Final Answer

2 + 1 + 2 = 5


===============================================================================
WHY MULTIPLY?
===============================================================================

Suppose

Left subtree has

2 possible BSTs

L1
L2


Right subtree has

3 possible BSTs

R1
R2
R3


Every left tree can combine with every right tree.


            ROOT

        L1 + R1
        L1 + R2
        L1 + R3

        L2 + R1
        L2 + R2
        L2 + R3


Total

2 × 3 = 6


===============================================================================
RECURSION TREE
===============================================================================

count(1,3)

               (1,3)

        /         |         \

      root=1    root=2    root=3

      /    \     /   \     /   \

 Empty   (2,3) (1,1) (3,3) (1,2) Empty


Every subtree is again solved in exactly the same way.


===============================================================================
WHY DOES RECURSION GIVE TLE?
===============================================================================

Without Memoization

Same subproblem is solved many times.

Example:

count(1,5)

    |
    +----------------------+
    |                      |
count(1,2)             count(2,5)
    |                      |
count(2,2)            count(2,2)
    |                      |
 Again calculated      Again calculated


Many repeated computations occur.

Hence

Time Limit Exceeded.


===============================================================================
MEMOIZATION IDEA
===============================================================================

Store answer of every

(start,end)

Once computed.

Next time:

Instead of recursion,

simply return stored answer.


Example:

memo

(1,1) -> 1

(2,3) -> 2

(1,3) -> 5

Now recursion becomes Dynamic Programming.


===============================================================================
RECURSIVE + MEMOIZATION
===============================================================================

class Solution:

    def numTrees(self, n):

        memo = {}

        def count(start, end):

            if start > end:
                return 1

            if (start, end) in memo:
                return memo[(start, end)]

            ans = 0

            for root in range(start, end + 1):

                left = count(start, root - 1)

                right = count(root + 1, end)

                ans += left * right

            memo[(start, end)] = ans

            return ans

        return count(1, n)


===============================================================================
DP (CATALAN NUMBER)
===============================================================================

dp[i]

=

Number of unique BSTs using i nodes.


Transition

dp[nodes]

=

Σ

dp[left_nodes]

×

dp[right_nodes]


Example

nodes = 4


Root = 1

left = 0

right = 3

Contribution

dp[0] × dp[3]


Root = 2

left = 1

right = 2

Contribution

dp[1] × dp[2]


Root = 3

left = 2

right = 1

Contribution

dp[2] × dp[1]


Root = 4

left = 3

right = 0

Contribution

dp[3] × dp[0]


===============================================================================
DP CODE
===============================================================================

class Solution:

    def numTrees(self, n):

        dp = [0]*(n+1)

        dp[0] = 1
        dp[1] = 1

        for nodes in range(2,n+1):

            for root in range(1,nodes+1):

                left = root-1
                right = nodes-root

                dp[nodes] += dp[left]*dp[right]

        return dp[n]


===============================================================================
COMPLEXITY
===============================================================================

1. Pure Recursion

Time  : Exponential
Space : O(N)

-----------------------------------------

2. Memoization

Time  : O(N²)

Space : O(N²)

-----------------------------------------

3. DP (Catalan)

Time  : O(N²)

Space : O(N)

(Best Solution)


===============================================================================
INTERVIEW NOTES
===============================================================================

Difference between 95 and 96

LeetCode 95

Return actual BSTs

Return Type

List<TreeNode>

------------------------------------

LeetCode 96

Return only COUNT

Return Type

int

------------------------------------

95:

Create TreeNode

96:

Multiply counts

left_count × right_count


===============================================================================
PATTERN
===============================================================================

Choose every node as ROOT

↓

Solve Left

↓

Solve Right

↓

Multiply Left × Right

↓

Add contribution

↓

Repeat for every possible ROOT

===============================================================================
"""'''







class Solution:
    def numTrees(self, n: int):

        memo = {}

        def count(start, end):

            if start > end:
                return 1

            if (start, end) in memo:
                return memo[(start, end)]

            ans = 0

            for root in range(start, end + 1):

                left = count(start, root - 1)
                right = count(root + 1, end)

                ans += left * right

            memo[(start, end)] = ans

            return ans

        return count(1, n)