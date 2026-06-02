



# my first approach to solving the problem is to use a dummy node to store the sum of the nodes between the zeros and then return the next of the dummy node as the head of the new linked list.
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=ListNode(0)
        if head is None:
            return head
        c=p
        s=0
        l=head.next
        while(l is not None):
            if l.val ==0:
                c.next=ListNode(s)
                c=c.next
                s=0
            else:
                s+=l.val
            l=l.next
        return p.next



# Correctness: ✅ 10/10
# Readability: ✅ 9/10
# Space: ⚠️ 7/10


# method 2 optimized approach using two pointers to merge the nodes between the zeros and return the next of the head as the head of the new linked list.

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        modify = head.next
        curr = modify

        total = 0

        while curr:
            if curr.val == 0:
                modify.val = total
                modify.next = curr.next

                modify = modify.next
                total = 0
            else:
                total += curr.val

            curr = curr.next

        return head.next
    


# Correctness: ✅ 10/10
# Time: ✅ O(n)
# Space: ✅ O(1)