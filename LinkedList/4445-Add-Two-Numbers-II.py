'''You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 '''





#  my aproach to solve this problem 


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
   
    def reverse(s,l):
        if l is None or l.next is None:
            return l
        
        t=l.next
        p=l
        p.next =None

    

        while t is not None :
            m=t.next
            t.next =p
            p=t
            t=m
        return p


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        l1=self.reverse(l1)
        l2=self.reverse(l2)
        c=0
        la=l1
        lb=l2

        while la is not None and lb is not None:
            t=(la.val+lb.val+c)
            c=t//10
            if(c==0):
                la.val=t
                lb.val=t
            else:
                la.val=t%10
                lb.val=t%10
            la=la.next
            lb=lb.next
        if la is not None:
            while la is not None and c==1:
              t=la.val+c
              c=t//10
              if(c==0):
                la.val=t
              else:
                la.val=t%10
              la=la.next
       
            t=self.reverse(l1)
            if c==1:
             c=ListNode(1)
             c.next=t
             return c
            else:
             return t
        else :
            while lb is not None and c==1:
              t=lb.val+c
              c=t//10
              if(c==0):
                lb.val=t
              else:
                lb.val=t%10
              lb=lb.next
       
            t=self.reverse(l2)
            if c==1:
             c=ListNode(1)
             c.next=t
             return c
            else:
             return t


        
        



# method  II

# Agar tum reverse approach hi use karna chahte ho, to ye uska corrected version hai.

class Solution(object):

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def addTwoNumbers(self, l1, l2):

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        dummy = ListNode(0)
        tail = dummy

        carry = 0

        while l1 or l2 or carry:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry

            carry = total // 10

            tail.next = ListNode(total % 10)
            tail = tail.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return self.reverse(dummy.next)


# Time Complexity
# Reverse l1 → O(n)
# Reverse l2 → O(m)
# Addition → O(max(n,m))
# Reverse result → O(max(n,m))

# Overall:

# O(n + m)
# Space Complexity
# O(max(n,m))









# optional approach without reversing the linked lists or stack:





class Solution(object):
    def addTwoNumbers(self, l1, l2):

        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while s1 or s2 or carry:

            x = s1.pop() if s1 else 0
            y = s2.pop() if s2 else 0

            total = x + y + carry
            carry = total // 10

            node = ListNode(total % 10)
            node.next = head
            head = node

        return head
    









# Interview Recommendation

# Approach	        Time	    Extra Space         	Preferred
# Stack	            O(n+m)	    O(n+m)	                  ⭐⭐⭐⭐⭐
# Reverse + Reverse	O(n+m)	    O(1) auxiliary	          ⭐⭐⭐⭐
# Recursion	        O(n+m)	    O(n+m)	                  ⭐⭐