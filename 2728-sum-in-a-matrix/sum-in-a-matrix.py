class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        n=len(nums)
        m=len(nums[0])
        result=0
        for i in nums:
            i.sort()
        transpose=[[0]*n for i in range(m)]
        for i in range(n):
            for j in range(m):
                transpose[j][i]=nums[i][j]
        for x in transpose:
            result+=max(x)
        return result