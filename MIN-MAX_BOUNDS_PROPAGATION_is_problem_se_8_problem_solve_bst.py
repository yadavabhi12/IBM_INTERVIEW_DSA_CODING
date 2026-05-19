# ============================================================
# PATTERN: "MIN-MAX BOUNDS PROPAGATION THROUGH RECURSION"
# ============================================================
# Core Idea:
#   - हर recursive call में एक valid range (min, max) pass होती है
#   - अगर current node उस range में है → valid, आगे बढ़ो
#   - Left child को: (min, current.data) range मिलती है
#   - Right child को: (current.data, max) range मिलती है
#
# यह pattern क्यों? क्योंकि:
#   - BST property GLOBAL होती है, LOCAL नहीं
#   - Example: root=10, root.left=5, root.left.right=7
#     → 7 अपने parent(5) से बड़ा है ✓
#     → लेकिन root(10) से छोटा होना भी जरूरी है ✓
#     → यह globally valid BST है
#   - Simple "left < root < right" check FAIL होता है globally
#   - इसीलिए bounds ऊपर से नीचे pass करने पड़ते हैं
# ============================================================


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ============================================================
# PROBLEM 1: Validate Binary Search Tree
# ============================================================
# क्यों यह pattern?
#   - हर node को यह जानना होगा कि उसके सभी ancestors ने
#     कौन सी constraint impose की है
#   - Inorder traversal से भी होता है, लेकिन bounds से
#     O(1) extra space में होता है (stack overhead छोड़ें)
# Time: O(N), Space: O(H) — H = height of tree
# ============================================================

def validate_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """
    हर node के लिए check करो: min_val < node.data < max_val
    Left जाओ तो max_val = current (current से छोटा होना चाहिए)
    Right जाओ तो min_val = current (current से बड़ा होना चाहिए)
    """
    if root is None:
        return True  # Empty tree/subtree always valid
    
    # Current node valid range में है?
    if root.data <= min_val or root.data >= max_val:
        return False
    
    # Left subtree: सब कुछ current से छोटा होना चाहिए → max = root.data
    # Right subtree: सब कुछ current से बड़ा होना चाहिए → min = root.data
    return (validate_bst(root.left, min_val, root.data) and
            validate_bst(root.right, root.data, max_val))


# ============================================================
# PROBLEM 2: Construct BST from Preorder Traversal
# ============================================================
# क्यों यह pattern?
#   - Preorder में पहला element root है
#   - अगला element तब left subtree में जाएगा जब वह
#     current bounds के अंदर हो
#   - Bounds pass करके हम decide करते हैं कि अगला
#     element left में जाएगा या right में
# Time: O(N), Space: O(H)
# ============================================================

def construct_bst_from_preorder(preorder):
    """
    Preorder array से BST बनाओ — bounds से decide होगा
    कि next element किस subtree में जाएगा
    """
    index = [0]  # Mutable index (list में wrap किया)
    
    def build(min_val, max_val):
        # सभी elements process हो गए, या current element
        # इस subtree की valid range में नहीं है
        if index[0] == len(preorder):
            return None
        
        val = preorder[index[0]]
        
        # यह value इस subtree की range में नहीं → यहाँ नहीं जाएगा
        if val <= min_val or val >= max_val:
            return None
        
        # यह value इस subtree की है → node बनाओ
        node = Node(val)
        index[0] += 1
        
        # Left subtree: range (min_val, val)
        node.left = build(min_val, val)
        # Right subtree: range (val, max_val)
        node.right = build(val, max_val)
        
        return node
    
    return build(float('-inf'), float('inf'))


# ============================================================
# PROBLEM 3: Trim BST to Range [low, high]
# ============================================================
# क्यों यह pattern?
#   - अगर node.data < low → पूरा left subtree भी छोटा है
#     (BST property) → right subtree trim करो
#   - अगर node.data > high → पूरा right subtree भी बड़ा है
#     → left subtree trim करो
#   - Bounds propagation से हम subtrees को efficiently skip करते हैं
# Time: O(N), Space: O(H)
# ============================================================

def trim_bst(root, low, high):
    """
    BST को [low, high] range में trim करो
    Range के बाहर के nodes हटा दो
    """
    if root is None:
        return None
    
    # अगर root.data < low → root और उसका left subtree
    # दोनों range से बाहर हैं → only right subtree trim करो
    if root.data < low:
        return trim_bst(root.right, low, high)
    
    # अगर root.data > high → root और उसका right subtree
    # दोनों range से बाहर हैं → only left subtree trim करो
    if root.data > high:
        return trim_bst(root.left, low, high)
    
    # root valid range में है → दोनों subtrees trim करो
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)
    
    return root


# ============================================================
# PROBLEM 4: Count BST Nodes in Range [low, high]
# ============================================================
# क्यों यह pattern?
#   - Bounds की knowledge से हम unnecessary subtrees
#     explore नहीं करते
#   - अगर node < low → left subtree में कोई valid node नहीं
#   - अगर node > high → right subtree में कोई valid node नहीं
#   - Simple traversal से O(N), लेकिन bounds से subtrees skip → faster
# Time: O(N) worst, O(H + K) best — K = count of valid nodes
# ============================================================

def count_nodes_in_range(root, low, high):
    """
    BST में [low, high] range में कितने nodes हैं?
    Bounds का use करके invalid subtrees skip करो
    """
    if root is None:
        return 0
    
    # Current node range से छोटा → left subtree skip करो
    # (BST property: left में सब और छोटे होंगे)
    if root.data < low:
        return count_nodes_in_range(root.right, low, high)
    
    # Current node range से बड़ा → right subtree skip करो
    if root.data > high:
        return count_nodes_in_range(root.left, low, high)
    
    # Current node valid है → दोनों sides check करो + current count करो
    return (1 +
            count_nodes_in_range(root.left, low, high) +
            count_nodes_in_range(root.right, low, high))


# ============================================================
# PROBLEM 5: Range Sum of BST
# ============================================================
# क्यों यह pattern?
#   - Same as count, लेकिन count की जगह sum
#   - LeetCode 938 — यही exact pattern
#   - Bounds से invalid subtrees prune होती हैं
# Time: O(N) worst, O(H + K) best
# ============================================================

def range_sum_bst(root, low, high):
    """
    BST में [low, high] range के सभी nodes का sum निकालो
    """
    if root is None:
        return 0
    
    # Current node too small → only right explore करो
    if root.data < low:
        return range_sum_bst(root.right, low, high)
    
    # Current node too large → only left explore करो
    if root.data > high:
        return range_sum_bst(root.left, low, high)
    
    # Current node valid → sum में add करो + दोनों sides explore करो
    return (root.data +
            range_sum_bst(root.left, low, high) +
            range_sum_bst(root.right, low, high))


# ============================================================
# PROBLEM 6: Check if Array is Valid BST Preorder Sequence
# ============================================================
# क्यों यह pattern?
#   - Preorder में हम जैसे-जैसे आगे बढ़ते हैं, bounds
#     automatically update होती हैं
#   - Stack-based bounds propagation (iterative version)
#   - जब भी हम right subtree में जाते हैं, lower bound
#     update होती है (parent की value)
# Time: O(N), Space: O(N)
# ============================================================

def verify_preorder_bst(preorder):
    """
    Check करो: क्या यह array किसी valid BST का
    preorder traversal हो सकता है?
    
    Stack में lower_bound track होती है —
    जब right subtree में जाते हैं तो lower bound = popped value
    """
    stack = []
    lower_bound = float('-inf')  # Current node की minimum allowed value
    
    for val in preorder:
        # अगर current value lower bound से छोटी है →
        # हम किसी left subtree में हैं जहाँ हमें नहीं होना चाहिए
        if val < lower_bound:
            return False
        
        # जब भी हम right subtree में जाते हैं (val > stack top):
        # सब pop करो जब तक stack top < val
        # Lower bound = सबसे बड़ा popped element (parent of right subtree)
        while stack and stack[-1] < val:
            lower_bound = stack.pop()
        
        stack.append(val)
    
    return True


# ============================================================
# PROBLEM 7: Largest BST Subtree
# ============================================================
# क्यों यह pattern?
#   - REVERSE direction: bounds नीचे से ऊपर आती हैं
#   - हर subtree अपना (min, max, size) return करता है
#   - Parent check करता है: क्या दोनों children की bounds
#     consistent हैं?
#   - Same concept, लेकिन bottom-up propagation
# Time: O(N), Space: O(H)
# ============================================================

def largest_bst_subtree(root):
    """
    Binary Tree में largest BST subtree का size निकालो
    Returns: (is_bst, min_val, max_val, size)
    
    Bottom-up: हर node अपने subtree की info return करता है
    Parent decide करता है: क्या मैं BST का हिस्सा हूँ?
    """
    max_size = [0]  # Global maximum size track करने के लिए
    
    def helper(node):
        """
        Returns: (is_bst, subtree_min, subtree_max, bst_size)
        """
        if node is None:
            # Empty subtree: valid BST, min=+inf, max=-inf, size=0
            return True, float('inf'), float('-inf'), 0
        
        # Left और right subtrees की info लो
        left_bst, left_min, left_max, left_size = helper(node.left)
        right_bst, right_min, right_max, right_size = helper(node.right)
        
        # Current node valid BST बनाता है अगर:
        # 1. Left subtree valid BST है
        # 2. Right subtree valid BST है
        # 3. node.data > left subtree का maximum
        # 4. node.data < right subtree का minimum
        if (left_bst and right_bst and
                left_max < node.data < right_min):
            
            size = left_size + right_size + 1
            max_size[0] = max(max_size[0], size)
            
            # इस subtree की actual min और max return करो
            curr_min = min(left_min, node.data)
            curr_max = max(right_max, node.data)
            
            return True, curr_min, curr_max, size
        
        # Valid BST नहीं है — लेकिन children की info propagate करो
        # ताकि ancestors को सही size मिले
        return False, float('-inf'), float('inf'), max(left_size, right_size)
    
    helper(root)
    return max_size[0]


# ============================================================
# PROBLEM 8: Closest Value in BST within Range
# ============================================================
# क्यों यह pattern?
#   - Bounds की knowledge से हम decide करते हैं
#     किस direction में जाना है
#   - अगर target < current → left में जाओ
#   - अगर target > current → right में जाओ
#   - यह essentially bounds को dynamically narrow करना है
# Time: O(H), Space: O(1)
# ============================================================

def closest_value_bst(root, target):
    """
    BST में target के closest value वाला node ढूंढो
    
    हर step पर bounds automatically narrow होती हैं —
    BST property हमें guarantee देती है कि हम
    correct direction में जा रहे हैं
    """
    closest = root.data
    
    while root:
        # Current node closer है?
        if abs(root.data - target) < abs(closest - target):
            closest = root.data
        
        # BST bounds use करके direction decide करो:
        # target < root → left subtree में closer होगा
        # target > root → right subtree में closer होगा
        if target < root.data:
            root = root.left   # Effective upper bound = root.data
        elif target > root.data:
            root = root.right  # Effective lower bound = root.data
        else:
            break  # Exact match मिल गया
    
    return closest


# ============================================================
# TESTING ALL PROBLEMS
# ============================================================

def build_test_tree():
    """
         10
        /  \
       5    15
      / \     \
     3   7    18
    """
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.right = Node(18)
    return root


if __name__ == "__main__":
    root = build_test_tree()
    
    print("=" * 55)
    print("PATTERN: Min-Max Bounds Propagation")
    print("=" * 55)
    
    # Problem 1
    print(f"\n1. Validate BST: {validate_bst(root)}")
    # → True
    
    # Problem 2
    preorder = [10, 5, 3, 7, 15, 18]
    bst_root = construct_bst_from_preorder(preorder)
    print(f"2. Construct from Preorder, then validate: {validate_bst(bst_root)}")
    # → True
    
    # Problem 3
    trimmed = trim_bst(build_test_tree(), 5, 15)
    print(f"3. Trim BST [5,15], root: {trimmed.data}, "
          f"left: {trimmed.left.data}, right: {trimmed.right.data}")
    # → root=10, left=5, right=15
    
    # Problem 4
    print(f"4. Count nodes in [5,15]: {count_nodes_in_range(root, 5, 15)}")
    # → 4 (5, 7, 10, 15)
    
    # Problem 5
    print(f"5. Range Sum [5,15]: {range_sum_bst(root, 5, 15)}")
    # → 37 (5+7+10+15)
    
    # Problem 6
    print(f"6. Verify Preorder [10,5,3,7,15,18]: {verify_preorder_bst([10,5,3,7,15,18])}")
    print(f"   Verify Invalid  [10,15,5,3,7,18]: {verify_preorder_bst([10,15,5,3,7,18])}")
    # → True, False
    
    # Problem 7
    print(f"7. Largest BST Subtree size: {largest_bst_subtree(root)}")
    # → 6 (entire tree is BST)
    
    # Problem 8
    print(f"8. Closest to 6: {closest_value_bst(root, 6)}")
    print(f"   Closest to 12: {closest_value_bst(root, 12)}")
    # → 7, 10