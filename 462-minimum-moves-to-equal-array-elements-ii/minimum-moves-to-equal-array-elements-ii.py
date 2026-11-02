class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        total_moves = 0
        nums.sort()
        median = nums[len(nums) // 2]

        # Calculate moves required to make every element equal to the median
        for value in nums:
            total_moves += abs(value - median)

        return total_moves