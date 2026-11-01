class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        res = float('inf')
        for i in range(1,len(nums),2):
            val = int(str(nums[i - 1]) + str(nums[i]))
            res = min(res,val)
        return res