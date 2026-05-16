class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def reversePrint(llist):
    stack = []

    h = llist

    # Push all elements into stack
    while h is not None:
        stack.append(h.data)
        h = h.next

    # Pop until stack becomes empty
    while stack:
        print(stack.pop())


# Creating Linked List manually
head = SinglyLinkedListNode(1)
second = SinglyLinkedListNode(2)
third = SinglyLinkedListNode(3)

head.next = second
second.next = third

# Call function
reversePrint(head)