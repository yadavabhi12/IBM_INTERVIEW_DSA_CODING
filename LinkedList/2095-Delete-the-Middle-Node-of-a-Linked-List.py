# my first approach to solving the problem is to use the slow/fast pointer technique to find the middle node. write code more  massive


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=head
        if head is None or head.next is None:
            head=None
            return head
        
        elif s.next is not None and s.next.next is  None  :
            s.next=None
            return head
        elif s.next is not None and s.next.next.next is None  :
            s.next=s.next.next
            return head
        
        f=head.next
        while(f is not None and f.next is not None and f.next.next is not None  ):
            f=f.next.next
            s=s.next
        if s.next and s.next is not None:
           s.next=s.next.next
       
        return head
    







    # short and clean code using slow/fast pointer technique to find the middle node and delete it.


class Solution:
     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head