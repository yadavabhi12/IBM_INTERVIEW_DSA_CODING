def morris_inorder_traversal(root):
    current = root
    while current:
        if current.left is None:
            print(current.data, end=" ")
            current = current.right
        else:
            # Find the inorder predecessor
            predecessor = current.left
            while predecessor.right is not None and predecessor.right != current:
                predecessor = predecessor.right
            if predecessor.right is None:
                # Make current the right child of its predecessor
                predecessor.right = current
                current = current.left
            else:
                # Revert the changes made to restore the original tree
                predecessor.right = None
                print(current.data, end=" ")
                current = current.right