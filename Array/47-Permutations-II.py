"""
===============================================================================
LeetCode 47 - Permutations II
===============================================================================

PROBLEM
-------
Given an array nums that may contain duplicates, return all possible unique
permutations.

Example:

nums = [1, 1, 2]

Possible UNIQUE permutations:

[
    [1,1,2],
    [1,2,1],
    [2,1,1]
]


===============================================================================
WHY IS THIS DIFFERENT FROM LEETCODE 46?
===============================================================================

LeetCode 46:

    nums contains DISTINCT numbers.

Example:

    [1,2,3]

Every permutation is automatically unique.


LeetCode 47:

    nums can contain DUPLICATES.

Example:

    [1,1,2]


If we blindly generate permutations, we get:

[1,1,2]
[1,2,1]
[1,1,2]   <-- duplicate
[1,2,1]   <-- duplicate
[2,1,1]
[2,1,1]   <-- duplicate


We need only:

[1,1,2]
[1,2,1]
[2,1,1]


===============================================================================
CORE IDEA
===============================================================================

This is:

        BACKTRACKING   add

plus:

        DUPLICATE SKIPPING


The most important trick is:

        SORT THE ARRAY FIRST


Example:

[2,1,1]

becomes:

[1,1,2]


Now duplicate values become adjacent.


Then while choosing a number:

    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
        continue


This prevents generating the same permutation more than once.


===============================================================================
WHY SORT?
===============================================================================

Suppose:

[1,2,1]


Duplicates are separated:

1 ... 1


It is harder to detect duplicates.


After sorting:

[1,1,2]


Now duplicates are next to each other:

1 1 2
↑ ↑
same


This makes duplicate skipping possible.


===============================================================================
BACKTRACKING TREE
===============================================================================

For:

[1,1,2]


At first position:

                []
             /   |   \
            1    1    2
                 ↑
              duplicate
              branch skipped


Choose first 1:

                []
                |
                1
              /   \
             1     2
            /       \
           2         1


Results:

[1,1,2]
[1,2,1]


Choose 2:

                []
                |
                2
                |
                1
                |
                1

Result:

[2,1,1]


Final:

[1,1,2]
[1,2,1]
[2,1,1]


===============================================================================
APPROACH 1 - BACKTRACKING + USED ARRAY ⭐⭐⭐
===============================================================================
"""

class Solution:

    def permuteUnique(self, nums):

        nums.sort()

        result = []
        current = []

        used = [False] * len(nums)


        def backtrack():

            # ----------------------------------------------------------
            # Complete permutation
            # ----------------------------------------------------------

            if len(current) == len(nums):

                result.append(current.copy())

                return


            # ----------------------------------------------------------
            # Try every number
            # ----------------------------------------------------------

            for i in range(len(nums)):

                # Already used in current permutation
                if used[i]:
                    continue


                # ------------------------------------------------------
                # DUPLICATE SKIPPING
                # ------------------------------------------------------

                if (
                    i > 0
                    and nums[i] == nums[i - 1]
                    and not used[i - 1]
                ):
                    continue


                # Choose
                used[i] = True
                current.append(nums[i])


                # Explore
                backtrack()


                # Undo
                current.pop()
                used[i] = False


        backtrack()

        return result


"""
===============================================================================
THE MOST IMPORTANT CONDITION
===============================================================================

This line:

if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
    continue


looks complicated initially.


Let's understand it deeply.


===============================================================================
WHY "not used[i-1]"?
===============================================================================

Suppose:

nums = [1,1,2]


At some level we have:

[ ]


We have two identical 1s.


We want to choose ONLY the FIRST 1
as the starting choice.


So:

i = 0:

choose 1


i = 1:

another 1


But the previous identical 1 is NOT currently being used.


Therefore:

    not used[i-1] == True


So skip the second 1.


--------------------------------------------------

But consider:

current = [1]


Now we want another 1.


At this point:

used[0] = True


So for i = 1:

not used[0] == False


Therefore we DO NOT skip it.


We are allowed to use the second 1.


This is very important.


===============================================================================
VISUALIZATION
===============================================================================

nums:

index:

  0   1   2
  ↓   ↓   ↓
 [1] [1] [2]


At the same recursion level:


        []
       /  \
      1    1
      ↑
    choose
   only first


The second 1 is skipped because it would create
the exact same branch.


But after choosing the first 1:


        []
        |
        1
        |
        1


The second 1 is allowed.


Because now the two 1s have different roles:

first 1 = already selected
second 1 = next element


===============================================================================
DRY RUN
===============================================================================

nums:

[1,1,2]


Initially:

current = []


--------------------------------------------------

i = 0

choose 1

current:

[1]


used:

[True, False, False]


--------------------------------------------------

Next level:

Try i = 0

Already used.

Skip.


Try i = 1

nums[1] == nums[0]

BUT:

used[0] = True


So:

not used[0] = False


Therefore we can choose it.


current:

[1,1]


--------------------------------------------------

Next:

choose 2


current:

[1,1,2]


Complete.


Add:

[1,1,2]


--------------------------------------------------

BACKTRACK

Remove 2.


current:

[1,1]


Then remove second 1.


current:

[1]


--------------------------------------------------

Try 2:

current:

[1,2]


Then choose 1:

[1,2,1]


Add.


--------------------------------------------------

Back to:

[]


Now i = 1:


nums[1] == nums[0]


and:

used[0] == False


Therefore:

SKIP.


Otherwise we would generate the same permutations
again.


--------------------------------------------------

Try i = 2:

choose 2


current:

[2]


Then:

2 → 1 → 1


Result:

[2,1,1]


===============================================================================
FINAL RESULT
===============================================================================

[
    [1,1,2],
    [1,2,1],
    [2,1,1]
]


===============================================================================
TIME COMPLEXITY
===============================================================================

Let:

n = len(nums)


There can be up to:

n!


permutations.


For each complete permutation we copy:

current.copy()


which costs:

O(n)


Therefore the usual output-sensitive upper bound is:

O(n × n!)


Worst case happens when all elements are distinct.


If duplicates exist, the number of UNIQUE permutations is smaller.


For frequencies:

n1, n2, n3, ...


the number of unique permutations is:

n! / (n1! × n2! × n3! × ...)


Therefore actual output size can be much smaller.


===============================================================================
SPACE COMPLEXITY
===============================================================================

Recursion depth:

O(n)


current array:

O(n)


used array:

O(n)


Output:

O(n × number_of_unique_permutations)


If output is included:

O(n × U)


where U = number of unique permutations.


Auxiliary space excluding output:

O(n)


===============================================================================
APPROACH 2 - COUNTER / FREQUENCY MAP ⭐⭐⭐
===============================================================================

Instead of maintaining:

used[]


we can store:

value -> frequency


Example:

nums = [1,1,2]


frequency:

1 -> 2
2 -> 1


At each level:

choose a number whose frequency > 0.


Then:

frequency[x] -= 1


DFS


frequency[x] += 1


This automatically handles duplicates.


This is often one of the cleanest approaches.


===============================================================================
CODE
===============================================================================
"""

from collections import Counter


class Solution:

    def permuteUnique(self, nums):

        count = Counter(nums)

        result = []
        current = []

        n = len(nums)


        def backtrack():

            if len(current) == n:

                result.append(current.copy())

                return


            for num in count:

                if count[num] == 0:
                    continue


                # Choose
                current.append(num)
                count[num] -= 1


                # Explore
                backtrack()


                # Undo
                count[num] += 1
                current.pop()


        backtrack()

        return result


"""
===============================================================================
WHY FREQUENCY MAP IS NICE
===============================================================================

For:

[1,1,2]


Frequency:

1 → 2
2 → 1


At the first position:

choose 1

frequency becomes:

1 → 1
2 → 1


Next:

choose 1

frequency:

1 → 0
2 → 1


Then:

choose 2


Permutation:

[1,1,2]


No duplicate branch is generated because
we choose VALUES based on available frequency,
not individual duplicate indexes.


===============================================================================
COMPARISON
===============================================================================

METHOD 1:

Sort + used[]

Advantages:

- Very common interview pattern
- Easy to extend from LeetCode 46
- Explicit duplicate handling


METHOD 2:

Counter / Frequency Map

Advantages:

- No duplicate-index problem
- Very clean conceptually
- Naturally handles repeated values


For interviews:

Know BOTH.


===============================================================================
APPROACH 3 - SET AT EACH LEVEL
===============================================================================

Another way is:

At every recursion level,
maintain a set of values already chosen at that level.


Example:

nums = [1,1,2]


At root:

used_at_level = {}


Choose first 1.

Then:

used_at_level = {1}


When we encounter second 1 at the SAME LEVEL:

1 is already in the set.

Skip it.


But inside the next recursion level,
we create a NEW set.


This is different from a global visited set.


===============================================================================
CODE
===============================================================================
"""

class Solution:

    def permuteUnique(self, nums):

        result = []
        current = []
        used = [False] * len(nums)


        def backtrack():

            if len(current) == len(nums):

                result.append(current.copy())

                return


            level_used = set()


            for i in range(len(nums)):

                if used[i]:
                    continue


                if nums[i] in level_used:
                    continue


                level_used.add(nums[i])

                used[i] = True
                current.append(nums[i])


                backtrack()


                current.pop()
                used[i] = False


        backtrack()

        return result


"""
===============================================================================
IMPORTANT DIFFERENCE
===============================================================================

used:

    Tracks whether an INDEX is already used
    in the CURRENT permutation.


level_used:

    Tracks whether a VALUE has already been chosen
    at the CURRENT recursion LEVEL.


They solve two different problems.


===============================================================================
EXAMPLE
===============================================================================

nums = [1,1,2]


current:

[1]


used:

[True, False, False]


At next level:

level_used = {}


Choose second 1:

level_used = {1}


Now another 1 at THIS SAME LEVEL:

already in level_used

→ skip.


But if we go deeper:

new recursion call

creates:

level_used = {}


So another 1 can be chosen if it represents
a different position in the permutation.


===============================================================================
APPROACH 4 - SWAP + SET
===============================================================================

Another classic permutation technique is
in-place swapping.


For each position:

swap current position with every possible element.


To handle duplicates,
use a set at each recursion level.


===============================================================================
CODE
===============================================================================
"""

class Solution:

    def permuteUnique(self, nums):

        result = []


        def backtrack(start):

            if start == len(nums):

                result.append(nums.copy())

                return


            used_at_level = set()


            for i in range(start, len(nums)):

                if nums[i] in used_at_level:
                    continue


                used_at_level.add(nums[i])


                nums[start], nums[i] = nums[i], nums[start]


                backtrack(start + 1)


                nums[start], nums[i] = nums[i], nums[start]


        backtrack(0)

        return result


"""
===============================================================================
HOW SWAP APPROACH WORKS
===============================================================================

nums:

[1,1,2]


start = 0


We decide:

"What number should occupy index 0?"


Choices:

1
1
2


But both 1s are identical.


So only one 1 branch is needed.


After choosing 1:

[1,1,2]


Now:

start = 1


"What should occupy index 1?"


Possible:

1
2


Generate:

[1,1,2]

and:

[1,2,1]


Then backtrack.


Choose 2 for index 0:

[2,1,1]


Done.


===============================================================================
APPROACH COMPARISON
===============================================================================

1. SORT + USED ARRAY

Most common:

    nums.sort()
    used[]
    skip duplicates


Complexity:

Time: O(n × n!)
Space: O(n) auxiliary


--------------------------------------------------

2. COUNTER

Use:

Counter(nums)


Very clean duplicate handling.


Time:

O(n × n!) worst case


Space:

O(n)


--------------------------------------------------

3. LEVEL SET

Use:

level_used = set()


No sorting required.


Time:

O(n × n!) worst case


Space:

O(n)


--------------------------------------------------

4. SWAP + LEVEL SET

In-place permutation generation.


Time:

O(n × n!)


Auxiliary:

O(n) recursion


===============================================================================
WHICH ONE SHOULD YOU USE IN INTERVIEW?
===============================================================================

My recommendation:

FIRST learn:

        Sort + Used Array


Because it teaches the most important backtracking concept:

        "skip duplicate choices at the same level"


Then learn:

        Counter


because it is elegant and avoids index-level duplicate handling.


Then learn:

        Swap + Set


because it is another important permutation pattern.


===============================================================================
46 vs 47
===============================================================================

LeetCode 46:

        Permutations


Input:

[1,2,3]


No duplicates.


Pattern:

DFS + used[]


--------------------------------------------------

LeetCode 47:

        Permutations II


Input:

[1,1,2]


Duplicates.


Pattern:

SORT
  ↓
DFS
  ↓
used[]
  ↓
SKIP DUPLICATE CHOICE
  ↓
BACKTRACK


===============================================================================
MOST IMPORTANT INTERVIEW CONCEPT
===============================================================================

Duplicate handling is NOT:

"Never use the same number twice."


That would be WRONG.


For:

[1,1,2]


we absolutely CAN use both 1s:


[1,1,2]


The rule is:

"Don't make the SAME CHOICE at the SAME recursion level
when the values are identical."


This distinction is extremely important.


===============================================================================
MEMORY TRICK
===============================================================================

PERMUTATION II:


        SORT
          ↓
      BACKTRACK
          ↓
      used[i]?
       /     \
     YES      NO
      ↓        ↓
    skip    duplicate?
                ↓
           YES → skip
                ↓
              choose
                ↓
             recurse
                ↓
             undo


Duplicate condition:

        same value
             +
        same level
             ↓
           SKIP


===============================================================================
ONE-LINE FORMULA
===============================================================================

Unique permutations:

        n!
-------------------------
n1! × n2! × n3! × ...


Example:

[1,1,2,2]


n = 4

frequency:

1 → 2
2 → 2


Unique permutations:

4! / (2! × 2!)

= 24 / 4

= 6


===============================================================================
FINAL TAKEAWAY
===============================================================================

LeetCode 47 is fundamentally:

        BACKTRACKING


The extra challenge is:

        DUPLICATES


The most important pattern is:

        sort
          ↓
        choose
          ↓
        skip same value at same level
          ↓
        recurse
          ↓
        undo


Remember this sentence for interviews:

"Duplicate values are allowed in the permutation,
but I should not choose the same value twice
at the same recursion level."


===============================================================================
"""