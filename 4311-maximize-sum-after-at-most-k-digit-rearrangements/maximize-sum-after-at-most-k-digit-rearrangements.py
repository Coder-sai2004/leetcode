from collections import defaultdict

class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:

        # Store numbers grouped by their maximum possible increase
        groups = defaultdict(list)

        for i in range(len(nums)):

            # Arrange digits in descending order
            digits = sorted(str(nums[i]), reverse=True)
            max_num = int("".join(digits))

            # Calculate the increase possible for this number
            if max_num >= nums[i]:
                increase = max_num - nums[i]
                groups[increase].append(nums[i])
            else:
                groups[0].append(nums[i])

        # Process numbers with the largest increase first
        increases = sorted(groups.keys())[::-1]
        total = 0
        count = 0

        for increase in increases:
            numbers = groups[increase]

            for num in numbers:
                if count < k:
                    total += num + increase
                    count += 1
                else:
                    total += num

        return total