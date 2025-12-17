class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x=[nums[0]]
        for i in range(1,len(nums)):
            x.append(x[i-1]+nums[i])
        return x