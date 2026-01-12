class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        #calculating max sum using kadane
        maxcurrent=maxglobal=nums[0]
        for i in range(1,len(nums)):
            maxcurrent=max(nums[i],maxcurrent+nums[i])
            if maxcurrent>maxglobal:
                maxglobal=maxcurrent

        #calculating min sum using kadane
        mincurrent=minglobal=nums[0]
        for i in range(1,len(nums)):
            mincurrent=min(nums[i],mincurrent+nums[i])
            if mincurrent<minglobal:
                minglobal=mincurrent
                
        return max(abs(minglobal),abs(maxglobal))