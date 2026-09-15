class Solution:
    def intersect(self, nums1, nums2):

        count = {}

        # Count nums1
        for num in nums1:
            count[num] = count.get(num, 0) + 1

        ans = []

        # Match with nums 2
        for num in nums2:
            if count.get(num, 0) > 0:
                ans.append(num)
                count[num] -= 1

        return ans











class Solution:
    def intersect(self, nums1, nums2):

        nums1.sort()
        nums2.sort()

        i = 0
        j = 0

        ans = []

        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return ans