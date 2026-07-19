class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def backtrack(index, parts):
            # 4 parts complete
            if len(parts) == 4:
                if index == len(s):
                    ans.append(".".join(parts))
                return

            # Try length 1, 2, 3
            for length in range(1, 4):

                if index + length > len(s):
                    break

                part = s[index:index + length]

                # Leading zero
                if len(part) > 1 and part[0] == '0':
                    continue

                # Greater than 255
                if int(part) > 255:
                    continue

                parts.append(part)

                backtrack(index + length, parts)

                # Backtrack
                parts.pop()

        backtrack(0, [])

        return ans