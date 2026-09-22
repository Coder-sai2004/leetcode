class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        right = 0
        ans = 0
        while left<len(nums1) and right<len(nums2):
            #adding the maximum distance when left index and value less than or equal to right index and value.
            if nums1[left]<=nums2[right] and left<=right:
                ans=max(ans,right-left)
                right+=1
            #when the left index or value greater than right index or value
            else:
                left+=1
                if left > right:
                    right = left
        return ans