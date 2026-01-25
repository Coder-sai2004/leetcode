class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        c=-1
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                c=i
        return c+1