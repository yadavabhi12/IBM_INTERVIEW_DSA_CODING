"""
===============================================================================
LeetCode 260 - Single Number III
===============================================================================

PROBLEM
-------
Given an integer array nums:

- Every number appears EXACTLY TWICE.
- Exactly TWO numbers appear ONLY ONCE.

Return those two numbers.

The answer can be returned in any order.


===============================================================================
EXAMPLE
===============================================================================

Input:

nums = [1, 2, 1, 3, 2, 5]


Frequency:

1 -> 2 times
2 -> 2 times
3 -> 1 time
5 -> 1 time


Answer:

[3, 5]


===============================================================================
MAIN CHALLENGE
===============================================================================

LeetCode 136:

Every number appears twice
EXCEPT ONE.

Therefore:

XOR of everything

gives the single number.


But here:

Every number appears twice
EXCEPT TWO.


So:

XOR of everything

will NOT directly give both answers.

Instead it gives:

unique1 ^ unique2


We need to separate these two numbers.


===============================================================================
APPROACH 1 - HASHMAP
===============================================================================

The easiest solution is to count frequencies.


CODE
===============================================================================
"""

class Solution:

    def singleNumber(self, nums):

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        ans = []

        for num, count in freq.items():

            if count == 1:
                ans.append(num)

        return ans


"""
===============================================================================
COMPLEXITY
===============================================================================

Time:

O(N)


Space:

O(N)


This is easy, but the interesting part of the problem is solving it
in O(1) extra space.


===============================================================================
APPROACH 2 - SORTING
===============================================================================

Sort the array.

Then equal numbers become adjacent.


Example:

[1, 2, 1, 3, 2, 5]

After sorting:

[1, 1, 2, 2, 3, 5]


Now:

1,1 -> pair

2,2 -> pair

3 -> unique

5 -> unique


CODE
===============================================================================
"""

class Solution:

    def singleNumber(self, nums):

        nums.sort()

        ans = []

        i = 0

        while i < len(nums):

            if i + 1 < len(nums) and nums[i] == nums[i + 1]:

                i += 2

            else:

                ans.append(nums[i])

                i += 1

        return ans


"""
===============================================================================
COMPLEXITY
===============================================================================

Time:

O(N log N)


Space:

Depends on sorting implementation.


===============================================================================
APPROACH 3 - XOR + DIFFERENTIATING BIT ⭐
===============================================================================

This is the important optimal solution.

We know:

Every duplicate appears twice.

Therefore:

x ^ x = 0


So if we XOR the entire array:

duplicate numbers cancel each other.


Example:

[1, 2, 1, 3, 2, 5]


XOR:

1 ^ 2 ^ 1 ^ 3 ^ 2 ^ 5


Rearrange:

(1 ^ 1)
^
(2 ^ 2)
^
3
^
5


= 0 ^ 0 ^ 3 ^ 5


= 3 ^ 5


Let:

xor_all = 3 ^ 5


It is NOT one of the answers.

It is the difference between the two answers in terms of bits.


===============================================================================
WHY DO WE NEED A DIFFERENT BIT?
===============================================================================

Since 3 and 5 are different numbers,

their binary representations must differ at least at ONE bit.


3:

011


5:

101


Different bits:

bit 1

and

bit 2


We only need ONE bit where they are different.


The standard trick:

rightmost_set_bit = xor_all & (-xor_all)


===============================================================================
WHY DOES THIS WORK?
===============================================================================

Suppose:

xor_all = 3 ^ 5


3 = 011
5 = 101

XOR:

110


Rightmost set bit:

010


Now this bit is:

different

between 3 and 5.


Therefore we can use this bit to divide all numbers into TWO groups.


===============================================================================
TWO GROUPS
===============================================================================

Group 1:

Numbers whose chosen bit is 0.


Group 2:

Numbers whose chosen bit is 1.


The two unique numbers MUST go into different groups.


Why?

Because the chosen bit is exactly a bit where they differ.


Meanwhile every duplicate pair goes into the SAME group.


Therefore duplicates still cancel with XOR.


===============================================================================
EXAMPLE
===============================================================================

nums:

[1, 2, 1, 3, 2, 5]


Unique:

3 and 5


xor_all:

3 ^ 5

= 6

Binary:

110


rightmost set bit:

010


Now divide numbers.


Check bit 1.


Group 0:

1
1
5


XOR:

1 ^ 1 ^ 5

= 5


Group 1:

2
3
2


XOR:

2 ^ 3 ^ 2

= 3


Answer:

[5, 3]


===============================================================================
CODE - OPTIMAL ⭐⭐⭐
===============================================================================
"""

class Solution:

    def singleNumber(self, nums):

        # XOR of the two unique numbers
        xor_all = 0

        for num in nums:
            xor_all ^= num

        # Get the rightmost bit where the two unique numbers differ
        diff_bit = xor_all & -xor_all

        a = 0
        b = 0

        for num in nums:

            if num & diff_bit:

                a ^= num

            else:

                b ^= num

        return [a, b]


"""
===============================================================================
DRY RUN
===============================================================================

nums:

[1, 2, 1, 3, 2, 5]


STEP 1
------

XOR everything:

1 ^ 2 ^ 1 ^ 3 ^ 2 ^ 5

Duplicate pairs cancel:

(1 ^ 1)
(2 ^ 2)

Remaining:

3 ^ 5

= 6


Binary:

6 = 110


STEP 2
------

Find rightmost set bit:

6 & -6

= 2

Binary:

010


STEP 3
------

Divide numbers based on bit 1.


Number | Binary | Bit 1
-------|--------|------
1      | 001    | 0
2      | 010    | 1
1      | 001    | 0
3      | 011    | 1
2      | 010    | 1
5      | 101    | 0


Group A:

2, 3, 2


XOR:

2 ^ 3 ^ 2

= 3


Group B:

1, 1, 5


XOR:

1 ^ 1 ^ 5

= 5


Final:

[3, 5]


===============================================================================
WHY DUPLICATES CANCEL?
===============================================================================

Suppose duplicate is 7.

If both copies go into the same group:

7 ^ 7

= 0


Therefore they disappear.


Only the unique number remains in each group.


===============================================================================
WHY MUST UNIQUE NUMBERS GO INTO DIFFERENT GROUPS?
===============================================================================

We selected a bit where:

unique1 != unique2


Therefore:

one has that bit = 1

other has that bit = 0


So they are guaranteed to go into different groups.


This is the entire trick.


===============================================================================
APPROACH COMPARISON
===============================================================================

1. HashMap

Time  : O(N)
Space : O(N)

Easy


-----------------------------------

2. Sorting

Time  : O(N log N)
Space : Depends on sorting

Easy/Medium


-----------------------------------

3. XOR + Partition

Time  : O(N)
Space : O(1)

Best ⭐


===============================================================================
COMMON MISTAKES
===============================================================================

1.

Doing only:

ans ^= num


This gives:

unique1 ^ unique2

NOT the two numbers individually.


--------------------------------------------------

2.

Using:

xor_all & 1


This may not be a bit where the two numbers differ.


Use:

xor_all & -xor_all


to get the rightmost set bit.


--------------------------------------------------

3.

Forgetting that duplicates must go into the SAME group.

The chosen bit guarantees this because a number and itself
have identical bits.


===============================================================================
INTERVIEW TRICK
===============================================================================

Remember this chain:

Everything XOR

↓

Duplicate pairs cancel

↓

unique1 ^ unique2

↓

Find one different bit

↓

Split numbers into TWO groups

↓

XOR each group

↓

Get unique1 and unique2


===============================================================================
10-SECOND MEMORY TRICK
===============================================================================

Two unique numbers?

Think:

    XOR ALL

        ↓

    Find different bit

        ↓

    Split into 2 groups

        ↓

    XOR each group


===============================================================================
RELATED PROBLEMS
===============================================================================

LeetCode 136

Single Number

Every number appears twice except one.

Solution:

XOR


LeetCode 137

Single Number II

Every number appears three times except one.

Solution:

Bit Counting / State Machine


LeetCode 260

Single Number III

Every number appears twice except TWO.

Solution:

XOR + Different Bit + Partition


===============================================================================
FINAL TAKEAWAY
===============================================================================

The most important observation is:

XOR of the entire array does not give either unique number.

It gives:

unique1 ^ unique2


That XOR tells us where the two numbers are different.

We use that different bit to separate the array into two groups.

Then XOR each group independently.

===============================================================================
"""