from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        if root is None:
            return result

        queue = deque([root])

        while queue:

            current_level = []

            level_size = len(queue)

            for _ in range(level_size):

                current_node = queue.popleft()

                current_level.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            result.insert(0, current_level)

        return result
    

#     Complexity
# Time: O(n + L²) (insert at front ka overhead)
# Space: O(n)












# Optimized Version ⭐ (Recommended)

# Instead of list, use deque for the result.

from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = deque()

        if root is None:
            return []

        queue = deque([root])

        while queue:

            current_level = []

            level_size = len(queue)

            for _ in range(level_size):

                current_node = queue.popleft()

                current_level.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            result.appendleft(current_level)

        return list(result)
# Complexity
# Time: O(n) ✅
# Space: O(n)
# Aur ek Clean Version (Interview Favorite)

# Ye sabse readable mana jata hai:





















from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        levels = []

        while queue:

            level = []

            for _ in range(len(queue)):

                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            levels.append(level)

        return levels[::-1]
    




# Complexity
# BFS: O(n)
# Reverse list (levels[::-1]): O(L), jahan L levels ki sankhya hai.

# Total:

# Time: O(n)
# Space: O(n)