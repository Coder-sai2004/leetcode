class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        if 1 not in nums or 2 not in nums:
            return -1
        o=0
        t=0
        i=0
        j=0
        mi=0
        l=False
        r=False
        while i<len(nums):
            if nums[i]==1:
                o=i
                l=True
            elif nums[j]==2:
                t=j
                r=True
            if l and r:
                mi=abs(t-o) if mi==0 else min(mi,abs(t-o))
            i+=1
            j+=1
        return mi