class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Calculate the prefix sum array.
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])

        # freq stores the frequency of each prefix sum encountered.
        freq = {}

        # res stores the total number of subarrays whose sum equals the goal.
        res = 0

        for cur in prefix_sum:
            # Check whether (current prefix sum - goal) exists in freq.
            # If it exists, add its frequency to the answer because those
            # prefix sums form subarrays whose sum is equal to the goal.
            if cur - goal in freq:
                res += freq[cur - goal]

            freq[cur] = freq.get(cur, 0) + 1

            # If the current prefix sum itself equals the goal,
            # then the subarray from index 0 to the current index is valid.
            if cur == goal:
                res += 1

        return res