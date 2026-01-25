class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)-k+1
        mi=float('inf')
        for i in range(n):
            mi=min(mi,max(nums[i:i+k])-min(nums[i:i+k]))
        return mi