# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """

        def match(listNode, treeNode):
            if not listNode:
                return True
            if not treeNode:
                return False
            if listNode.val != treeNode.val:
                return False

            return (match(listNode.next, treeNode.left) or
                    match(listNode.next, treeNode.right))

        if not root:
            return False

        return (match(head, root) or
                self.isSubPath(head, root.left) or
                self.isSubPath(head, root.right))