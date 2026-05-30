# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.




# brute force approach  ❤️❤️❤️❤️❤️👌👌👌👌

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s=head
        f=s
        while f is not None and f.next is not None:
            s=s.next
            f=f.next.next
        c=s
        m=c
        l=[]
        while s is not None:
            l.append(s)
            s=s.next
        c=head
       
      
        while c is not m:
            t=c.next
            p=l.pop()
            c.next=p
            p.next=t
            c=t
           
        if len(l)==0:
            c.next.next=None
        else:
            print(c.val)
            c.next=None
        
        return head






# optimize approach  ❤️❤️❤️❤️❤️👌👌👌👌

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find middle using slow/fast pointer
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        # If odd length, skip middle element
        second = slow if fast is None else slow.next
        first = prev
        # Reorder list
        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2