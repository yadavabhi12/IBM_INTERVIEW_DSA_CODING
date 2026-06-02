#  Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



#  more massive code 
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        """
        f=head
        s=head
        while f is not None and f.next is not None:
            f=f.next.next
            s=s.next
        l:ListNode=[]
        c=s
        while c is not None:
            l.append(c)
            c=c.next
        
        h=head

        print(len(l))
        while len(l)>0 and h is not s:
            t=h.next
            e=l.pop()
            h.next=e
            e.next=t
            h=t
        print(len(l))
        if(len(l)==0):
            h.next=None

        else:
            t=l.pop()
            print(t.val)
            h.next=t
            t.next=None







            # clean and efficient code using slow/fast pointer technique to find the middle node and reverse the second half.

class Solution:
    def reorderList(self, head):

        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        stack = []

        cur = slow.next
        slow.next = None

        while cur:
            stack.append(cur)
            cur = cur.next

        cur = head

        while stack:
            nxt = cur.next
            node = stack.pop()

            cur.next = node
            node.next = nxt

            cur = nxt
        

        
        
        