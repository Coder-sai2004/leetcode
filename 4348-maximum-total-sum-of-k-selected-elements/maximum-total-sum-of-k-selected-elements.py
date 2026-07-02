class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        s=0
        nums=sorted(nums)[::-1]
        for i in range(k):
            if mul>0:
                s+=nums[i]*mul
                mul-=1
            else:
                s+=nums[i]
        return s