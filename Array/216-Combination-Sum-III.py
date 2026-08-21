"""
===============================================================================
LeetCode 216 - Combination Sum III
===============================================================================

PROBLEM
-------
Find all valid combinations of k numbers that add up to n.

Rules:

1. We can use numbers only from 1 to 9.
2. Exactly k numbers must be selected.
3. Every number can be used ONLY ONCE.
4. The sum of selected numbers must be exactly n.

Return all possible combinations.

The order of numbers inside a combination does not matter.


===============================================================================
EXAMPLE 1
===============================================================================

Input:

k = 3
n = 7


We need:

3 numbers
whose sum = 7


Possible combination:

1 + 2 + 4 = 7


Answer:

[[1,2,4]]


===============================================================================
EXAMPLE 2
===============================================================================

Input:

k = 3
n = 9


Possible:

1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9


Answer:

[
    [1,2,6],
    [1,3,5],
    [2,3,4]
]


===============================================================================
KEY OBSERVATION
===============================================================================

This is a BACKTRACKING problem.

We need to:

    choose a number
        ↓
    move to the next number
        ↓
    continue choosing
        ↓
    stop when k numbers are selected


Because numbers can be used only once,

after choosing:

i

we only consider:

i + 1, i + 2, ...


===============================================================================
WHY DO WE START FROM start?
===============================================================================

Suppose we choose:

1


Next we should choose from:

2,3,4,5,6,7,8,9


NOT:

1 again.


If we allowed 1 again:

[1,1,5]

would be possible.

But the problem says every number can be used only once.


Therefore:

dfs(start)

and next call:

dfs(i + 1)


===============================================================================
BACKTRACKING TREE
===============================================================================

Suppose:

k = 2
n = 5


Start:

                    []
          /          |          \
        [1]         [2]         [3]
       /  \          |
    [1,2] [1,3]    [2,3]
      ↓      ↓        ↓
     sum    sum      sum
      3      4        5


Only:

[2,3]

is valid.


===============================================================================
BACKTRACKING STATE
===============================================================================

At every recursive call we need 4 pieces of information:

1. start
   → next number we are allowed to choose

2. k
   → how many numbers are still required

3. target
   → how much sum is still required

4. path
   → numbers selected so far


Example:

dfs(start, k, target, path)


===============================================================================
BASE CASE
===============================================================================

If:

k == 0


Then we have selected exactly k numbers.


Now check:

target == 0


If yes:

    valid combination

Otherwise:

    invalid


Therefore:

if k == 0:

    if target == 0:
        ans.append(path)


===============================================================================
CHOICE
===============================================================================

Try every number:

start ... 9


For each number:

1. Add it to path.
2. Reduce target.
3. Reduce k.
4. Recursively continue.
5. Remove it using backtracking.


===============================================================================
VISUALIZATION
===============================================================================

k = 3
n = 7


Choose 1:

        [1]
          |
      target = 6
      k = 2


Choose 2:

        [1,2]
            |
        target = 4
        k = 1


Choose 4:

        [1,2,4]
              |
          target = 0
          k = 0


VALID


===============================================================================
MAIN CODE - BACKTRACKING ⭐
===============================================================================
"""

class Solution:

    def combinationSum3(self, k: int, n: int):

        ans = []

        def backtrack(start, k, target, path):

            # Exactly k numbers selected
            if k == 0:

                if target == 0:
                    ans.append(path.copy())

                return

            # Try numbers from start to 9
            for num in range(start, 10):

                # If number is already greater than target,
                # later numbers will also be greater.
                if num > target:
                    break

                path.append(num)

                backtrack(
                    num + 1,
                    k - 1,
                    target - num,
                    path
                )

                path.pop()

        backtrack(1, k, n, [])

        return ans


"""
===============================================================================
DRY RUN
===============================================================================

k = 3
n = 9


backtrack(1, 3, 9, [])


Choose 1:

path = [1]

target = 8
k = 2


Choose 2:

path = [1,2]

target = 6
k = 1


Choose 3:

path = [1,2,3]

target = 3
k = 0


target != 0

INVALID


Backtrack:

[1,2]


Try 4:

[1,2,4]

target = 2

k = 0

INVALID


...


Eventually:

[1,2,6]

target = 0
k = 0

VALID


Add:

[1,2,6]


Similarly:

[1,3,5]


And:

[2,3,4]


Final:

[
    [1,2,6],
    [1,3,5],
    [2,3,4]
]


===============================================================================
WHY path.pop()?
===============================================================================

This is the HEART of backtracking.


Suppose:

path = [1,2]


We choose 4:

path = [1,2,4]


After exploring this choice,

we need to go back and try:

[1,2,5]

Therefore:

path.pop()


removes 4.


path becomes:

[1,2]


Then we can try another number.


===============================================================================
BACKTRACKING PATTERN
===============================================================================

Always remember:

    choose
       ↓
    explore
       ↓
    undo


Code:

path.append(num)

backtrack(...)

path.pop()


This pattern appears in:

- Subsets
- Permutations
- Combination Sum
- N-Queens
- Sudoku
- Letter Combinations
- Combination Sum III


===============================================================================
WHY num + 1?
===============================================================================

Suppose we choose:

num = 3


We cannot choose 3 again.


So next recursion starts from:

4


Therefore:

backtrack(num + 1, ...)


This automatically guarantees:

NO DUPLICATES.


===============================================================================
WHY IS THE RESULT SORTED?
===============================================================================

Because we always choose numbers in increasing order.


Example:

[1,2,6]


We will never create:

[2,1,6]


Because after choosing 2,

we can only choose:

3,4,5,...

This removes duplicate combinations automatically.


===============================================================================
OPTIMIZATION 1 - TARGET PRUNING
===============================================================================

Because all numbers are positive:

if:

num > target


then all later numbers will also be greater.

So we can stop:

if num > target:
    break


This avoids unnecessary recursion.


===============================================================================
OPTIMIZATION 2 - NOT ENOUGH NUMBERS
===============================================================================

Suppose:

k = 4


but only:

2 numbers

remain from start to 9.


There is no possible solution.


We can immediately stop.


Example:

remaining numbers:

8,9


but need:

3 numbers


Impossible.


===============================================================================
OPTIMIZED CODE
===============================================================================
"""

class Solution:

    def combinationSum3(self, k: int, n: int):

        ans = []

        def backtrack(start, k, target, path):

            # Need exactly k numbers
            if k == 0:

                if target == 0:
                    ans.append(path.copy())

                return

            # Not enough numbers left
            if 10 - start < k:
                return

            for num in range(start, 10):

                if num > target:
                    break

                path.append(num)

                backtrack(
                    num + 1,
                    k - 1,
                    target - num,
                    path
                )

                path.pop()

        backtrack(1, k, n, [])

        return ans


"""
===============================================================================
EVEN BETTER PRUNING
===============================================================================

We can also check:

Minimum possible sum

and

Maximum possible sum.


Suppose:

k = 3
start = 5


Smallest possible 3 numbers:

5 + 6 + 7 = 18


If target < 18:

Impossible.


Largest possible 3 numbers:

9 + 8 + 7 = 24


If target > 24:

Impossible.


Therefore we can prune the branch immediately.


===============================================================================
MINIMUM SUM
===============================================================================

start + (start+1) + ... + (start+k-1)


===============================================================================
MAXIMUM SUM
===============================================================================

9 + 8 + ... for k numbers


===============================================================================
OPTIMIZED VERSION
===============================================================================
"""

class Solution:

    def combinationSum3(self, k: int, n: int):

        ans = []

        def backtrack(start, k, target, path):

            if k == 0:

                if target == 0:
                    ans.append(path.copy())

                return

            # Not enough numbers
            if 10 - start < k:
                return

            # Minimum possible sum
            min_sum = sum(
                range(start, start + k)
            )

            if min_sum > target:
                return

            # Maximum possible sum
            max_sum = sum(
                range(10 - k, 10)
            )

            if max_sum < target:
                return

            for num in range(start, 10):

                if num > target:
                    break

                path.append(num)

                backtrack(
                    num + 1,
                    k - 1,
                    target - num,
                    path
                )

                path.pop()

        backtrack(1, k, n, [])

        return ans


"""
===============================================================================
ITERATIVE / BITMASK APPROACH
===============================================================================

Because numbers are ONLY:

1 to 9

there are only:

2^9 = 512

possible subsets.


We can simply generate every subset.

For every subset:

1. Count selected numbers.
2. Calculate sum.
3. If count == k AND sum == n:
       add it.


This is surprisingly simple.


===============================================================================
BITMASK IDEA
===============================================================================

9 numbers:

1 2 3 4 5 6 7 8 9


Each bit represents whether the number is selected.


Example:

mask:

000001011


Selected:

1
2
4


Count:

3


Sum:

1 + 2 + 4 = 7


===============================================================================
CODE
===============================================================================
"""

class Solution:

    def combinationSum3(self, k: int, n: int):
        # array to hold the final combinations
        ans = []

        for mask in range(1 << 9):

            path = []
            total = 0

            for i in range(9):

                if mask & (1 << i):

                    path.append(i + 1)
                    total += i + 1

            if len(path) == k and total == n:

                ans.append(path)

        return ans


"""
===============================================================================
BITMASK COMPLEXITY
===============================================================================

There are:

2^9 = 512


subsets.


For every subset we inspect 9 bits.


Time:

O(2^9 × 9)


Since 9 is constant:

O(1)


Space:

O(K)


for the generated result/path,
excluding the output.


===============================================================================
APPROACH COMPARISON
===============================================================================

1. Backtracking

Most natural solution.

Time: exponential in general, but the search space is tiny because
numbers are only 1..9.

Space: O(K) recursion/path, excluding output.


2. Backtracking + Pruning ⭐

Preferred interview solution.

Same worst-case bounded search space,
but avoids many impossible branches.


3. Bitmask

Since there are only 9 numbers:

2^9 = 512


Very simple and completely valid.

Time: O(2^9 × 9)

Space: O(K), excluding output.


===============================================================================
COMMON MISTAKES
===============================================================================

1.

Using the same number twice.

Wrong:

[1,1,5]


Every number can be used only once.


Use:

num + 1


for the next recursion.


--------------------------------------------------

2.

Forgetting path.pop().

Without pop():

previous choices remain in the path
and corrupt other branches.


--------------------------------------------------

3.

Appending path directly.

Wrong:

ans.append(path)


Correct:

ans.append(path.copy())


because path is mutable.


--------------------------------------------------

4.

Using:

start = 1

in every recursive call.

This allows duplicate numbers and duplicate combinations.


--------------------------------------------------

5.

Checking only the sum.

We ALSO need exactly k numbers.







For example:

k = 3
target = 7


[7]

has correct sum but only one number.

Invalid.


===============================================================================
INTERVIEW TRICK
===============================================================================

This is basically:

COMBINATION / SUBSET BACKTRACKING


Think:

    start
      ↓
    choose number
      ↓
    k - 1
      ↓
    target - number
      ↓
    recurse from number + 1
      ↓
    pop


===============================================================================
10-SECOND MEMORY TRICK
===============================================================================

Need:

k numbers

+

sum = n

+

numbers 1..9

+

no repetition


Therefore:

BACKTRACKING


Template:

path.append(num)

↓

dfs(num + 1, k - 1, target - num)

↓

path.pop()


===============================================================================
FINAL TAKEAWAY
===============================================================================

The most important thing is:

    num + 1


Why?

Because it ensures that once we choose a number,
we never choose it again.


And because numbers are selected in increasing order,
we automatically avoid duplicate combinations.


===============================================================================
"""