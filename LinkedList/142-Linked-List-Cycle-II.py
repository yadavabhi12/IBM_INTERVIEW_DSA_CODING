class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
    




    # NOTE :👌👌👌💕


    # LeetCode 142 - Linked List Cycle II

## Problem Summary

# Given a linked list, determine whether a cycle exists.

# If a cycle exists, return the node where the cycle begins.

# If no cycle exists, return `None`.

# ### Example

# ```text
# 1 -> 2 -> 3 -> 4 -> 5
#           ^       |
#           |_______|
# ```

# Cycle starts at node `3`.

# Expected Output:

# ```text
# Node(3)
# ```

# ---

# # Key Observation

# A normal linked list eventually reaches:

# ```text
# None
# ```

# A cyclic linked list never reaches `None`.

# If we keep following `next`, we will keep visiting the same nodes again and again.

# ---

# # Brute Force Approach

# Store every visited node in a HashSet.

# While traversing:

# * If node already exists in HashSet → cycle found.
# * Return that node.
# * Otherwise add node to HashSet.

# ### Complexity

# Time: O(n)

# Space: O(n)

# ---

# # Optimal Approach (Floyd's Cycle Detection)

# Also called:

# * Tortoise and Hare Algorithm
# * Slow Fast Pointer Technique

# ### Idea

# Use two pointers:

# ```text
# slow -> moves 1 step
# fast -> moves 2 steps
# ```

# ---

# # Why Will They Meet?

# If there is no cycle:

# ```text
# fast reaches None
# ```

# If there is a cycle:

# ```text
# slow enters cycle
# fast enters cycle
# ```

# Since fast moves faster than slow, it will eventually catch slow inside the cycle.

# Therefore:

# ```text
# slow == fast
# ```

# means a cycle exists.

# ---

# # Important Question

# After slow and fast meet,

# How do we find the starting node of the cycle?

# This is the real challenge of the problem.

# ---

# # Mathematical Insight

# Let:

# ```text
# x = distance from head to cycle start
# y = distance from cycle start to meeting point
# c = cycle length
# ```

# When pointers meet:

# ```text
# slow distance = x + y

# fast distance = 2(x + y)
# ```

# Fast travels exactly one or more extra full cycles.

# Therefore:

# ```text
# fast distance - slow distance = n * c
# ```

# Substituting:

# ```text
# 2(x + y) - (x + y) = n*c
# ```

# Result:

# ```text
# x + y = n*c
# ```

# Rearranging:

# ```text
# x = n*c - y
# ```

# ---

# # Meaning of x = n*c - y

# This equation tells us:

# Distance from Head to Cycle Start

# equals

# Distance from Meeting Point to Cycle Start
# (while moving inside the cycle).

# This is the key insight.

# ---

# # Final Trick

# After slow and fast meet:

# 1. Move one pointer back to Head.
# 2. Keep the other pointer at Meeting Point.
# 3. Move both pointers one step at a time.

# ```text
# ptr1 = head
# ptr2 = meeting_point
# ```

# Eventually:

# ```text
# ptr1 == ptr2
# ```

# The node where they meet is the starting node of the cycle.

# ---

# # Why Does This Work?

# Because:

# ```text
# Head -> CycleStart = x

# MeetingPoint -> CycleStart = x
# ```

# Both pointers travel the same distance.

# Hence they meet exactly at Cycle Start.

# ---

# # Algorithm

# Step 1:

# Use Slow and Fast pointers.

# Step 2:

# If Fast reaches None:

# ```text
# No cycle
# ```

# Return:

# ```python
# None
# ```

# Step 3:

# If Slow == Fast:

# ```text
# Cycle exists
# ```

# Step 4:

# Move Slow back to Head.

# Step 5:

# Move Slow and Fast one step at a time.

# Step 6:

# The node where they meet again is the Cycle Start.

# Return that node.

# ---

# # Complexity

# Time Complexity:

# ```text
# O(n)
# ```

# Space Complexity:

# ```text
# O(1)
# ```

# ---

# # Interview Takeaway

# Whenever you see:

# * Linked List
# * Cycle Detection
# * Find Cycle Start
# * Loop in Linked List

# Immediately think:

# ```text
# Floyd's Cycle Detection Algorithm
# (Tortoise and Hare)
# ```

# This problem is a classic application of Slow-Fast Pointers and mathematical reasoning using:

# ```text
# x + y = n*c
# ```

# which leads to:

# ```text
# x = n*c - y
# ```

# and helps us locate the exact node where the cycle begins.

#   '''  🤪😱😱