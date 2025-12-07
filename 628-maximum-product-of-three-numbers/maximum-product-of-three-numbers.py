class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)
        n=len(nums)-1
        i=0
        a=nums[i]*nums[i+1]*nums[n]
        b=nums[n]*nums[n-1]*nums[n-2]
        if a>b:
            return a
        return b