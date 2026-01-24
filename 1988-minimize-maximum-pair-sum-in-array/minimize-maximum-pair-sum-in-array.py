class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        mx=0
        while i<j:
            if nums[i]+nums[j]>mx:
                mx=nums[i]+nums[j]
            i+=1
            j-=1
        return mx