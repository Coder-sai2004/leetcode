class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        m=0
        for i in range(0,len(nums),2):
            m+=nums[i]
        return m