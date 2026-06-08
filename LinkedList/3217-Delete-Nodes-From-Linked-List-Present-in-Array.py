# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if len(nums)==0:
            return head
        d=ListNode(0)
        i=0
        while i<len(nums)and t is not None and t.next is not None:
            if  nums[i]==t.next.data:
                t.next=t.next.next
                i=i+1
        t=d
        return t
        