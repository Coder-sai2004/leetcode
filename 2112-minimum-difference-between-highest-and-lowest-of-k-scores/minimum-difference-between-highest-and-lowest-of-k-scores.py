class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)-k+1
        mi=float('inf')
        for i in range(n):
            mi=min(mi,nums[i:i+k][-1]-nums[i:i+k][0])
        return mi