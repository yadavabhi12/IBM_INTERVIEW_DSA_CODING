class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if len(nums)==0:
            return head
        d=ListNode(0)
        d.next=head
        i=0
        t=d

        for i in nums:
        
            while   t is not None and t.next is not None:
              if  i==t.next.val:          # Check if the current value is equal to the next node's value
                t.next=t.next.next       # Delete the node

              else:
                t=t.next

            t=d
       
        
       
        return d.next
    






# LeetCode 3217 - Delete Nodes From Linked List Present in Array

## 😱😱🤣Meri Approach

# * nums ke har element ke liye poori linked list traverse kar raha tha.
# * Agar value match hui to node delete kar raha tha.
# * Har deletion ke baad traversal dobara start ho raha tha.

# ### Problem

# ```text
# For each number in nums
#     Traverse entire linked list
# ```

# Isliye same linked list baar-baar scan ho rahi thi.

# ### Complexity

# ```text
# O(len(nums) * length_of_linked_list)
# ```

# Agar:

# nums = 1000 elements

# linked list = 100000 nodes

# To bahut zyada operations ho jayenge.

# Result:

# ```text
# TLE (Time Limit Exceeded)
# ```

# ---

# #  👌👌👌👌👌👌👌👌 Optimization Idea         👌👌👌👌

# Question ko ulta socho:

# Linked List ko ek hi baar traverse karo.

# Har node ke liye check karo:

# ```text
# Kya ye value nums me present hai?
# ```

# Ye check baar-baar ho raha hai.

# Isliye nums ko Set me convert kar do.

# ### Why Set?

# ```text
# List Lookup  -> O(n)
# Set Lookup   -> O(1)
# ```

# ---

# # Final Thinking

# 1. nums → Set
# 2. Linked List ko sirf 1 baar traverse karo
# 3. Agar node value set me hai → delete
# 4. Nahi hai → aage badho

# ---

# # Interview Learning

# Jab bhi question me baar-baar ye check ho:

# ```text
# value exists in collection?
# ```

# Turant socho:

# ```text
# Can I use a Set?
# ```

# Ye pattern bahut common hai.

# Array + Frequent Lookup

# ↓

# Set

# ↓

# O(1) lookup

# ↓

# Better Time Complexity






    # method 2  optimized solution 👌👌👌👌

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        nums_set = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr and curr.next:
            if curr.next.val in nums_set:    # Check if the next node's value is in the set
                curr.next = curr.next.next    # Delete the node
            else:
                curr = curr.next

        return dummy.next

        




