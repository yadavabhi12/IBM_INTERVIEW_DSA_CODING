# # Definition for singly-linked list.
# 👌👌👌👌👌❤️😏LeetCode 160 - Intersection of Two Linked Lists

# Approach:

# * Store nodes of both linked lists in separate stacks.
# * Compare the tail nodes first. If tails are different, no intersection exists.
# * Pop nodes from both stacks while they are the same.
# * The last common node popped is the intersection node.

# Complexity:

# * Time: O(m + n)
# * Space: O(m + n)

# Note:
# This solution uses extra space (stacks) for simplicity. An optimized O(1) space two-pointer solution also exists.
# 👌👌👌👌👌❤️😏








# bruteforce approach using stacks to find the intersection node of two linked lists.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> Optional[ListNode]:
        l=[]
        n=[]
      
        if b is None or a is None:
            return None
        while a is not None or b is not None:
            if a is not None:
                l.append(a)
                a=a.next
            if b is not None:
                n.append(b)
                b=b.next
    
        if(l[-1] != n[-1]):
            return None
        t=None
        while len(l)>0 and len(n)>0 and l[-1]==n[-1]:
            t=l.pop()
            n.pop()
       



        
        return t
    




# method 2 optimized approach using two pointers
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a