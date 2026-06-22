# brute force solution, time complexity is O(n)  space complexity is O(n) where n is the number of nodes in the tree
class Solution:
    def collect_path_numbers(self, node, path_numbers, current_number):
        if node is None:
            return

        current_number = current_number * 10 + node.val

        if node.left is None and node.right is None:
            path_numbers.append(current_number)
            return

        self.collect_path_numbers(node.left, path_numbers, current_number)
        self.collect_path_numbers(node.right, path_numbers, current_number)

    def sumNumbers(self, root):
        path_numbers = []

        self.collect_path_numbers(root, path_numbers, 0)

        total_sum = 0
        for number in path_numbers:
            total_sum += number

        return total_sum
    



# This is more efficient because it avoids storing all root-to-leaf numbers in a list. Time complexity is O(n) and extra space is only the recursion stack.








class Solution:
    def dfs(self, node, current_number):
        if node is None:
            return 0

        current_number = current_number * 10 + node.val

        if node.left is None and node.right is None:
            return current_number

        return (
            self.dfs(node.left, current_number)
            + self.dfs(node.right, current_number)
        )

    def sumNumbers(self, root):
        return self.dfs(root, 0)