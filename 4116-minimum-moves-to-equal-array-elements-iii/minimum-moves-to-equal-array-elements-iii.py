class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = max(nums)
        ans = 0
        for val in nums:
            ans += (n - val)
        return ans