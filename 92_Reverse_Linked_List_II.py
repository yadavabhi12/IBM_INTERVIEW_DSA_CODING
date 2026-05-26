# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

#       input  ====>'🔜👍💕    1--->2--->3--->4--->5
# output  ====>'🔜👍💕    1--->4--->3--->2--->5

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]



# brute force approach

def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    # Step 1: Reach the left position
    dummy = SinglyLinkedListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    # Step 2: Reverse the sublist
    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next







# second approach  better optimized  using stack

def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    stack = []
    curr = head
    pos = 1

    # Push nodes onto the stack until we reach the left position
    while curr and pos < left:
        stack.append(curr)
        curr = curr.next
        pos += 1

    # Reverse the sublist between left and right
    sublist = []
    while curr and pos <= right:
        sublist.append(curr)
        curr = curr.next
        pos += 1

    # Reconnect the reversed sublist
    if stack:
        stack[-1].next = sublist[-1]
    for i in range(len(sublist) - 1):
        sublist[i].next = sublist[i + 1]
    if sublist:
        sublist[-1].next = curr

    return stack[0] if stack else sublist[0]
