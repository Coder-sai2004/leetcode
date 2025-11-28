class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxcurrent=maxglobal=nums[0]
        for i in range(1,len(nums)):
            maxcurrent=max(nums[i],maxcurrent+nums[i])
            if maxcurrent>maxglobal:
                maxglobal=maxcurrent
        return maxglobal