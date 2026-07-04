# meri first solution is to find the leaves of both trees and compare them. If they are the same, then the trees are leaf-similar.
class Solution:
    def majorityElement(self, nums):
        freq = Counter(nums)

        ans = []

        for key, value in freq.items():
            if value > len(nums) // 3:
                ans.append(key)

        return ans
    






    # Approach 2: Boyer-Moore Voting Algorithm ⭐⭐⭐ (Expected)

# Observation:

# Agar koi element n/3 se zyada baar aata hai, to maximum 2 elements hi ho sakte hain.

# Example

# n = 9

# Need > 3

# 4 + 4 = 8 ✔

# 4 + 4 + 4 = 12 ❌

# Isliye sirf 2 candidates maintain karne padte hain.

# Algorithm

# Maintain

# candidate1
# candidate2

# count1
# count2

# Rules

# if num == candidate1
#     count1++

# elif num == candidate2
#     count2++

# elif count1 == 0
#     candidate1 = num
#     count1 = 1

# elif count2 == 0
#     candidate2 = num
#     count2 = 1

# else
#     count1--
#     count2--

# Ye sirf possible candidates deta hai.

# Finally unki frequency dobara count karni padti hai.

# Code
class Solution:
    def majorityElement(self, nums):

        candidate1 = None
        candidate2 = None

        count1 = 0
        count2 = 0

        for num in nums:

            if num == candidate1:
                count1 += 1

            elif num == candidate2:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        ans = []

        if nums.count(candidate1) > len(nums)//3:
            ans.append(candidate1)

        if candidate2 != candidate1 and nums.count(candidate2) > len(nums)//3:
            ans.append(candidate2)

        return ans
# Dry Run
# nums = [1,2,3,1,2,1,1]
# Num	cand1	c1	cand2	c2
# 1	1	1	None	0
# 2	1	1	2	1
# 3	1	0	2	0
# 1	1	1	2	0
# 2	1	1	2	1
# 1	1	2	2	1
# 1	1	3	2	1

# Verification

# 1 -> 4
# 2 -> 2

# n=7

# 7//3 =2

# Only 1 >2

# Answer

# [1]
# Complexity
# Approach	Time	Space
# Counter	O(n)	O(n)
# Boyer-Moore	O(n)	O(1) ✅
# Interview Tip

# Agar interviewer follow-up me "Can you solve it in O(1) extra space?" puche, to expected answer Boyer-Moore Voting Algorithm hai. This is the optimal solution for LeetCode 229.