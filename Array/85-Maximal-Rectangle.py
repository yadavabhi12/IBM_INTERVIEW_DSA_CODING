
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        ans = 0

        for row in matrix:

            # Build histogram
            for c in range(cols):
                if row[c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Largest Rectangle in Histogram
            stack = []

            for i in range(cols + 1):

                # Sentinel 0 at the end
                curr_height = 0 if i == cols else heights[i]

                while stack and heights[stack[-1]] > curr_height:

                    h = heights[stack.pop()]

                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i

                    ans = max(ans, h * width)

                stack.append(i)

        return ans






# 🏆 Final Code — Interview Version
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        ans = 0

        for row in matrix:

            # Convert current row into histogram
            for c in range(n):
                if row[c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Largest Rectangle in Histogram
            stack = []

            for i in range(n + 1):
                curr = 0 if i == n else heights[i]

                while stack and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]

                    width = i if not stack else i - stack[-1] - 1

                    ans = max(ans, h * width)

                if i < n:
                    stack.append(i)

        return ans


    #                      Binary Matrix
    #                    │
    #                    ▼
    #           Process one row
    #                    │
    #                    ▼
    #          Update heights[]
    #                    │
    #                    ▼
    #             Histogram
    #                    │
    #                    ▼
    #    Largest Rectangle in Histogram
    #                    │
    #                    ▼
    #           Monotonic Stack
    #                    │
    #                    ▼
    #              max area