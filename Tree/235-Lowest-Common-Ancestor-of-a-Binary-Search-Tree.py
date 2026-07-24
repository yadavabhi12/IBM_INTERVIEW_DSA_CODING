# 235. Lowest Common Ancestor of a Binary Search Tree


# first approach is to do a recursive traversal of the tree and check if the current node is the lowest common ancestor of the two given nodes. If it is, return the current node. If not, continue traversing the left and right subtrees.
# 1. Recursive BST👌👌👌👌👌👌❤️❤️❤️


class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if root is None:
            return None

        # Dono left mein
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Dono right mein
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Split point
        return root
    

    
# Time: O(h)
# Space: O(h) recursion stack.




    # 2. Iterative BST — recursion ke bina👍👍👍👍💕

# second approach is to do an iterative traversal of the tree and check if the current node is the lowest common ancestor of the two given nodes. If it is, return the current node. If not, continue traversing the left and right subtrees.
class Solution:
    def lowestCommonAncestor(self, root, p, q):

        while root:

            if p.val < root.val and q.val < root.val:
                root = root.left

            elif p.val > root.val and q.val > root.val:
                root = root.right

            else:
                return root
            

    
Time  = O(h)
Space = O(1)









# 3. Normal Binary Tree LCA approach

# Agar humein pata hi na ho ki tree BST hai, tab values compare karke left/right decide nahi kar sakte.



class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        return right

# Isme potentially poora tree explore hota hai:

# Time  = O(n)
# Space = O(h)

# Ye approach bahut important hai kyunki ye LeetCode 236 — LCA of Binary Tree mein use hoti hai.

