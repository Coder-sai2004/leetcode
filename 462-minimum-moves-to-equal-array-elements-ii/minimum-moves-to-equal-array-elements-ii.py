class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        ans = 0
        nums.sort()
        target = nums[len(nums) // 2]
        
        for val in nums:
            ans += abs(val - target)

        return ans