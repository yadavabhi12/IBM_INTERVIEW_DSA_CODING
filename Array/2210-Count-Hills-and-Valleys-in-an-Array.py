"""
===============================================================================
LeetCode 2210 - Count Hills and Valleys in an Array
===============================================================================

PROBLEM
-------
Given an integer array nums, count the number of Hills and Valleys.

Definitions:

Hill:
------
A position is a HILL if its nearest NON-EQUAL neighbors are BOTH smaller.

Valley:
--------
A position is a VALLEY if its nearest NON-EQUAL neighbors are BOTH greater.

IMPORTANT:
-----------
Adjacent duplicate values are ignored.

We compare ONLY the nearest different values.


===============================================================================
EXAMPLE 1
===============================================================================

nums = [2,4,1,1,6,5]

Ignoring duplicate 1

Array becomes conceptually

2 4 1 6 5


Check each element

4

2 < 4 > 1

Hill ✔


1

4 > 1 < 6

Valley ✔


6

1 < 6 > 5

Hill ✔


Answer = 3


===============================================================================
EXAMPLE 2
===============================================================================

nums = [6,6,5,5,4,1]

Ignore duplicates

6 5 4 1


No hill

No valley

Answer = 0


===============================================================================
KEY OBSERVATION
===============================================================================

Duplicates should NOT affect comparison.

Example

1 2 2 2 3

Middle 2's are same.

Treat them as

1 2 3


Similarly

3 2 2 2 1

Treat as

3 2 1


Therefore

Whenever we compare,

skip equal values.


===============================================================================
INTUITION
===============================================================================

For every index

Find

Nearest Different Left

Nearest Different Right

Then

Hill

left < current > right

Valley

left > current < right


===============================================================================
VISUALIZATION
===============================================================================

Array

2 4 1 1 6 5

            ↑

Current = 1


Nearest Different Left

4

Nearest Different Right

6


Condition

4 > 1 < 6

Valley


-------------------------------------------------------------------------------

Array

2 4 1 1 6 5

      ↑

Current = 4


Left

2

Right

1


Condition

2 < 4 > 1

Hill


===============================================================================
ALGORITHM
===============================================================================

For every index

1.

Move left

Skip duplicates

Find nearest different value.

2.

Move right

Skip duplicates

Find nearest different value.

3.

Compare

Hill

OR

Valley

Increase answer.


===============================================================================
CODE
===============================================================================

class Solution:

    def countHillValley(self, nums):

        ans = 0

        n = len(nums)

        for i in range(1, n - 1):

            left = i - 1

            while left >= 0 and nums[left] == nums[i]:
                left -= 1

            right = i + 1

            while right < n and nums[right] == nums[i]:
                right += 1

            if left < 0 or right >= n:
                continue

            if nums[left] < nums[i] > nums[right]:
                ans += 1

            elif nums[left] > nums[i] < nums[right]:
                ans += 1

        return ans


===============================================================================
DRY RUN
===============================================================================

nums

2 4 1 1 6 5


i = 1

Current = 4

Left = 2

Right = 1

2 < 4 > 1

Hill

Answer = 1


----------------------------------------------------

i = 2

Current = 1

Right duplicate

Skip

Next different = 6

Left = 4

4 > 1 < 6

Valley

Answer = 2


----------------------------------------------------

i = 3

Current = 1

Left duplicate

Skip

Left = 4

Right = 6

Again

4 > 1 < 6

Already represented by previous duplicate

This index is skipped naturally because nearest different
neighbors are the same after duplicate handling.


----------------------------------------------------

i = 4

Current = 6

Left = 1

Right = 5

1 < 6 > 5

Hill

Answer = 3


===============================================================================
OPTIMIZED IDEA
===============================================================================

Instead of skipping duplicates for every index,

first remove consecutive duplicates.

Example

Original

2 4 1 1 1 6 5


Compressed

2 4 1 6 5


Now simply count

Peak

a < b > c

or

Valley

a > b < c


This simplifies the logic.


===============================================================================
OPTIMIZED CODE
===============================================================================

class Solution:

    def countHillValley(self, nums):

        arr = [nums[0]]

        for x in nums[1:]:

            if x != arr[-1]:
                arr.append(x)

        ans = 0

        for i in range(1, len(arr)-1):

            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                ans += 1

            elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                ans += 1

        return ans


===============================================================================
TIME COMPLEXITY
===============================================================================

Approach 1

Worst Case

O(N²)

(Because every index may scan left/right)


--------------------------------------

Approach 2 (Compressed Array)

O(N)

Best solution.


===============================================================================
SPACE COMPLEXITY
===============================================================================

Approach 1

O(1)


Compressed Array

O(N)


===============================================================================
COMMON MISTAKES
===============================================================================

❌ Compare immediate neighbours only.

Wrong because duplicates must be ignored.

--------------------------------------

❌ Count every duplicate hill.

Duplicates represent SAME position.

Should count only once.

--------------------------------------

❌ Forget boundary conditions.

First and last element can never be hill/valley.

--------------------------------------

❌ Not skipping equal elements.


===============================================================================
INTERVIEW TRICK
===============================================================================

Whenever the question says

"Ignore consecutive duplicates"

Immediately think

Compress the array first.

Then solve the original problem.

This converts an O(N²) solution into O(N).


===============================================================================
PATTERN
===============================================================================

Array

↓

Ignore Consecutive Duplicates

↓

Peak / Valley Detection

↓

Compare Three Consecutive Values

↓

Count

===============================================================================
"""