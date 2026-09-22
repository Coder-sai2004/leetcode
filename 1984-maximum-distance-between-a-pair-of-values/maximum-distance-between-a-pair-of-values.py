class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        ans = 0
        left = 0
        right = 0

        while left < len(nums1) and right < len(nums2):
            if nums1[left] <= nums2[right] and left <= right:

                ans = max(ans, right - left)

                right += 1

            elif nums1[left] > nums2[right]:
                left += 1
                
                if left > right:
                    right = left
        
        return ans