# 
from LinkedList.singly_linked_list_reverse_print import SinglyLinkedListNode


def mergeLists(head1, head2):

    l = None
    c = None

    while head1 is not None and head2 is not None:

        if head1.data <= head2.data:

            if l is None:
                l = SinglyLinkedListNode(head1.data)
                c = l
            else:
                c.next = SinglyLinkedListNode(head1.data)
                c = c.next

            head1 = head1.next

        else:

            if l is None:
                l = SinglyLinkedListNode(head2.data)
                c = l
            else:
                c.next = SinglyLinkedListNode(head2.data)
                c = c.next

            head2 = head2.next

    while head1 is not None:

        c.next = SinglyLinkedListNode(head1.data)
        c = c.next
        head1 = head1.next

    while head2 is not None:

        c.next = SinglyLinkedListNode(head2.data)
        c = c.next
        head2 = head2.next

    return l








# 👍🔜  Better Optimized Version
def mergeLists(head1, head2):

    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data < head2.data:
        merged_head = head1
        head1 = head1.next
    else:
        merged_head = head2
        head2 = head2.next

    current = merged_head

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    # Append any remaining elements from either list
    if head1 is not None:
        current.next = head1
    else:
        current.next = head2

    return merged_head