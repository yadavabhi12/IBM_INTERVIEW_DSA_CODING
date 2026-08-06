"""
===============================================================================
LeetCode 174 - Dungeon Game
===============================================================================

PROBLEM
-------
A knight starts from the TOP-LEFT cell and wants to rescue the princess
located at the BOTTOM-RIGHT cell.

Each cell contains:

Positive number (+)
    -> Health increases.

Negative number (-)
    -> Health decreases.

Zero
    -> No effect.

Knight can move only:

    Right
    Down

The knight dies immediately if his health becomes 0 or below.

Find the MINIMUM initial health required so that the knight can always
reach the princess alive.


===============================================================================
EXAMPLE
===============================================================================

Dungeon

   -2   -3    3
   -5  -10    1
   10   30   -5


Answer

7


===============================================================================
VERY IMPORTANT OBSERVATION
===============================================================================

This is NOT

Maximum Path Sum

This is NOT

Minimum Path Sum

This is NOT

Greedy.


Question asks

Minimum INITIAL HEALTH.


Health changes while travelling.

Need to ensure

Health NEVER becomes <= 0.


===============================================================================
WHY GREEDY FAILS?
===============================================================================

Example

      -2     100

      -5    -100


Greedy says

Take +100

Looks good.

But maybe another path requires less initial health.

Therefore

Greedy fails.


===============================================================================
MAIN IDEA
===============================================================================

Instead of asking

"What health do I have?"

Ask

"How much health do I NEED before entering this cell?"


This changes the problem completely.


===============================================================================
DP STATE
===============================================================================

dp[i][j]

=

Minimum health required

BEFORE entering

cell (i,j).


Not

After leaving.


===============================================================================
START FROM THE END
===============================================================================

Princess cell

Suppose

-5


Need

6

Because

6 + (-5)

=

1

Minimum alive.


If princess cell is

10


Need only

1


Because

1 + 10

=

11


Still alive.


Formula

max(1, 1-dungeon[last])


===============================================================================
TRANSITION
===============================================================================

From current cell

You can go

Right

or

Down


Choose

Minimum health path.


Need

=

min(

Right Cell Need,

Down Cell Need

)


Suppose

Need on right

=

8


Current cell

=

-3


Need before entering current

=

8 - (-3)

=

11


Suppose current cell

=

+10


Need

=

8 - 10

=

-2


Impossible

Minimum health can never be below 1


So

Need

=

max(1, calculated value)


FINAL FORMULA

dp[i][j]

=

max(

1,

min(right,down)

-

dungeon[i][j]

)


===============================================================================
VISUALIZATION
===============================================================================

Dungeon

  -2   -3    3
  -5  -10    1
  10   30   -5


Start

Bottom Right


           ?

           ?

           6


Now

Move backward.


===============================================================================
FILL DP TABLE
===============================================================================

Dungeon

  -2   -3    3
  -5  -10    1
  10   30   -5


DP

  7    5    2

  6   11    5

  1    1    6


Answer

Top Left

7


===============================================================================
WHY BACKWARD DP?
===============================================================================

Current answer depends on

Future cells.


Forward traversal

Cannot know future requirement.


Backward traversal

Already knows

Required health.


===============================================================================
RECURSION
===============================================================================

solve(i,j)

returns

Minimum health needed before entering (i,j).


Base

Princess Cell


Recursive

Need Right

Need Down

Take minimum

Apply formula


===============================================================================
MEMOIZATION CODE
===============================================================================

class Solution:

    def calculateMinimumHP(self, dungeon):

        m=len(dungeon)
        n=len(dungeon[0])

        memo={}

        def dfs(i,j):

            if i>=m or j>=n:
                return float('inf')

            if (i,j) in memo:
                return memo[(i,j)]

            if i==m-1 and j==n-1:
                return max(1,1-dungeon[i][j])

            right=dfs(i,j+1)
            down=dfs(i+1,j)

            need=min(right,down)-dungeon[i][j]

            memo[(i,j)]=max(1,need)

            return memo[(i,j)]

        return dfs(0,0)


===============================================================================
BOTTOM-UP DP
===============================================================================
"""
class Solution:

    def calculateMinimumHP(self,dungeon):

        m=len(dungeon)
        n=len(dungeon[0])

        dp=[[float('inf')]*(n+1) for _ in range(m+1)]

        dp[m][n-1]=1
        dp[m-1][n]=1

        for i in range(m-1,-1,-1):

            for j in range(n-1,-1,-1):

                need=min(dp[i+1][j],dp[i][j+1])

                dp[i][j]=max(1,need-dungeon[i][j])

        return dp[0][0]









"""
===============================================================================
TIME COMPLEXITY
===============================================================================

Memoization

O(M*N)


Bottom-Up DP

O(M*N)


===============================================================================
SPACE COMPLEXITY
===============================================================================

Memoization

O(M*N)


Bottom-Up

O(M*N)


Can be optimized to

O(N)


===============================================================================
COMMON MISTAKES
===============================================================================

❌ Maximizing health.

❌ Using BFS.

❌ Greedy.

❌ Starting from top-left.

❌ Forgetting health can never become <=0.

❌ Forgetting max(1,...).


===============================================================================
INTERVIEW TRICK
===============================================================================

Think backwards.

Never think

Current Health.

Always think

Health REQUIRED before entering current cell.


===============================================================================
PATTERN
===============================================================================

Grid DP

↓

Backward DP

↓

Minimum Requirement DP

↓

State

Health Needed

↓

Transition

max(

1,

min(right,down)

-

currentCell

)

===============================================================================
"""