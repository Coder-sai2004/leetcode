class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_increasing = 0
        max_decreasing = 0

        increasing = 1
        decreasing = 1

        # Find the longest strictly increasing and decreasing subarrays
        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                increasing += 1
            else:
                max_increasing = max(max_increasing, increasing)
                increasing = 1

            if nums[i] < nums[i - 1]:
                decreasing += 1
            else:
                max_decreasing = max(max_decreasing, decreasing)
                decreasing = 1

        # Update maximum lengths after completing the loop
        max_increasing = max(max_increasing, increasing)
        max_decreasing = max(max_decreasing, decreasing)

        return max(max_increasing, max_decreasing)