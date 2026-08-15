class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        val=0
        n=len(nums)
        c=0
        for i in range(n):
            val^=nums[i]
            if nums[i]>0:
                c+=1
        if val==0 and c==0:
            return 0
        elif val>0:
            return n
        else:
            return n-1