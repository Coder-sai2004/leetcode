class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m=max(nums)
        if len(nums)!=m+1:
            return False
        nums.sort()
        for i in range(m):
            if i+1!=nums[i]:
                return False
        return True