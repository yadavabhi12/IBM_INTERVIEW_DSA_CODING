class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(start, temp):

            # k elements mil gaye
            if len(temp) == k:
                ans.append(temp[:])
                return

            for i in range(start, n + 1):

                # Choose
                temp.append(i)

                # Explore
                backtrack(i + 1, temp)

                # Undo / Backtrack
                temp.pop()

        backtrack(1, [])

        return ans
        