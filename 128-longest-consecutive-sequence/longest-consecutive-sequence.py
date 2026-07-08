class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        c=0
        m=1
        print(nums)
        for i in range(1,len(nums)):
            if nums[i]-1==nums[i-1]:
                m+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                c=max(c,m)
                m=1
        c=max(c,m)
        return c