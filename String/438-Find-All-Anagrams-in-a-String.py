class Solution:
    def findAnagrams(self, s: str, p: str):

        if len(p) > len(s):
            return []

        p_count = [0] * 26
        window = [0] * 26

        # Frequency of p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        k = len(p)
        ans = []

        # First window
        for i in range(k):
            window[ord(s[i]) - ord('a')] += 1

        if window == p_count:
            ans.append(0)

        # Slide window
        for i in range(k, len(s)):

            # Add new character
            window[ord(s[i]) - ord('a')] += 1

            # Remove character leaving window
            window[ord(s[i - k]) - ord('a')] -= 1

            # Check anagram
            if window == p_count:
                ans.append(i - k + 1)

        return ans












class Solution:
    def findAnagrams(self, s: str, p: str):

        if len(p) > len(s):
            return []

        need = [0] * 26
        window = [0] * 26

        for ch in p:
            need[ord(ch) - ord('a')] += 1

        required = 0

        for count in need:
            if count > 0:
                required += 1

        matches = 0
        left = 0
        ans = []

        for right in range(len(s)):

            idx = ord(s[right]) - ord('a')
            window[idx] += 1

            if window[idx] == need[idx]:
                matches += 1

            elif window[idx] == need[idx] + 1:
                matches -= 1

            # Window size > len(p)
            if right - left + 1 > len(p):

                idx = ord(s[left]) - ord('a')

                if window[idx] == need[idx]:
                    matches -= 1

                elif window[idx] == need[idx] + 1:
                    matches += 1

                window[idx] -= 1
                left += 1

            # Valid anagram
            if right - left + 1 == len(p) and matches == required:
                ans.append(left)

        return ans