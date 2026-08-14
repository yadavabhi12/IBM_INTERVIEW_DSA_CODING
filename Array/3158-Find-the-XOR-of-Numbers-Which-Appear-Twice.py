"""
===============================================================================
LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
===============================================================================

PROBLEM
-------
Given an integer array nums.

Every number appears either:

    1 time
    OR
    2 times

We need to find all numbers that appear EXACTLY TWICE
and return the XOR of those numbers.

Example:

nums = [1, 2, 1, 3, 2]

Numbers appearing twice:

1
2

Answer:

1 ^ 2 = 3


===============================================================================
EXAMPLE
===============================================================================

nums = [1, 2, 1, 3, 2]

Frequency:

1 -> 2 times
2 -> 2 times
3 -> 1 time


Therefore:

Repeated numbers = [1, 2]

XOR:

1 ^ 2 = 3


Answer:

3


===============================================================================
KEY OBSERVATION
===============================================================================

We only care whether a number has appeared before.

We can use a SET.

When we see a number for the first time:

    add it to the set.


When we see the same number again:

    it appears exactly twice.

So:

    answer ^= number


Because the problem guarantees that every number appears
either once or twice, there cannot be a third occurrence.


===============================================================================
VISUALIZATION
===============================================================================

nums:

1  2  1  3  2
   ↓     ↓     ↓

First 1:

seen = {1}

Second 1:

1 already exists

answer = 0 ^ 1

answer = 1


First 2:

seen = {1,2}

Second 2:

2 already exists

answer = 1 ^ 2

answer = 3


3 appears only once.

Final:

answer = 3


===============================================================================
APPROACH 1 - SET + XOR ⭐
===============================================================================

CODE
===============================================================================
"""

class Solution:

    def duplicateNumbersXOR(self, nums):

        seen = set()

        ans = 0

        for num in nums:

            if num in seen:

                ans ^= num

            else:

                seen.add(num)

        return ans


"""
===============================================================================
DRY RUN
===============================================================================

nums = [1, 2, 1, 3, 2]

Initial:

seen = {}
ans = 0


--------------------------------------------------

num = 1

1 not in seen

seen = {1}

ans = 0


--------------------------------------------------

num = 2

2 not in seen

seen = {1,2}

ans = 0


--------------------------------------------------

num = 1

1 already exists

ans = 0 ^ 1

ans = 1


--------------------------------------------------

num = 3

3 not in seen

seen = {1,2,3}

ans = 1


--------------------------------------------------

num = 2

2 already exists

ans = 1 ^ 2

ans = 3


Final answer:

3


===============================================================================
WHY XOR?
===============================================================================

Suppose duplicate numbers are:

1, 2, 5

We need:

1 ^ 2 ^ 5


XOR has useful properties:

x ^ 0 = x

x ^ x = 0


So we can accumulate all numbers that appear twice.


===============================================================================
APPROACH 2 - FREQUENCY MAP
===============================================================================

This is the more straightforward approach.

First count every number.

Then XOR numbers whose count == 2.


CODE
===============================================================================
"""

class Solution:

    def duplicateNumbersXOR(self, nums):

        freq = {}

        for num in nums:

            freq[num] = freq.get(num, 0) + 1

        ans = 0

        for num, count in freq.items():

            if count == 2:

                ans ^= num

        return ans


"""
===============================================================================
COMPLEXITY
===============================================================================

Set + XOR:

Time  : O(N)
Space : O(N)


Frequency Map:

Time  : O(N)
Space : O(N)


===============================================================================
CAN WE DO IT WITHOUT EXTRA SPACE?
===============================================================================

Because the problem allows every number to appear either once or twice,
we need some way to remember whether we have already seen each number.

A normal XOR over the entire array does NOT work.

Example:

nums = [1, 2, 1, 3, 2]

Total XOR:

1 ^ 2 ^ 1 ^ 3 ^ 2

Since:

1 ^ 1 = 0
2 ^ 2 = 0

Result:

3


But we need:

1 ^ 2 = 3

In this particular example it happens to produce the same result,
but this is NOT a valid general approach.

For example:

nums = [1, 1, 2]

Total XOR:

1 ^ 1 ^ 2

= 2

But required answer:

1


Therefore we need to distinguish:

first occurrence

from

second occurrence.


===============================================================================
IMPORTANT DIFFERENCE FROM LEETCODE 136
===============================================================================

LeetCode 136 - Single Number

Every number appears TWICE except one.

Use:

XOR


Because:

x ^ x = 0


--------------------------------------------------

LeetCode 3158

We need the numbers that appear TWICE.

Therefore:

We cannot simply XOR the whole array.

We first need to detect the SECOND occurrence.

Then:

ans ^= num


===============================================================================
INTERVIEW MEMORY TRICK
===============================================================================

Question:

"Find XOR of numbers appearing twice."


Think:

    SET

↓

First time:

    add


Second time:

    XOR


===============================================================================
PATTERN
===============================================================================

Array

↓

Track Seen Numbers

↓

Duplicate Found

↓

XOR Duplicate

↓

Return Answer


===============================================================================
EDGE CASE
===============================================================================

nums = [1, 2, 3]

No number appears twice.

Therefore:

ans = 0


Code naturally returns:

0


===============================================================================
FINAL TAKEAWAY
===============================================================================

The cleanest solution is:

    seen = set()

    ans = 0

    for num in nums:

        if num in seen:
            ans ^= num
        else:
            seen.add(num)

The SET answers:

"Have I seen this number before?"

XOR answers:

"What is the XOR of all numbers whose second occurrence I found?"


===============================================================================
"""