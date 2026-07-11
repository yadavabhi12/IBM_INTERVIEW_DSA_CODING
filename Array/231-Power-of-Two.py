# my first approach 


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t=n
        if n==0:
            return False
        if n==1:return True

        while n!=0 and n>1:
            
            if n%2==1:
                print (n)
                return False
                

            n=n//2
        return True if t>0 else False
    






    # better approach  
        
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2

        return True
    





    # optimized approach

class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0
    




'''Best Solution (Bit Manipulation)

A power of 2 has exactly one set bit in binary.

Examples:

1  = 0001
2  = 0010
4  = 0100
8  = 1000
16 = 10000

The trick is:

n & (n - 1) == 0

because:

8      = 1000
7      = 0111
---------------
8 & 7  = 0000

But for a non-power of two:

10     = 1010
9      = 1001
---------------
10 & 9 = 1000'''