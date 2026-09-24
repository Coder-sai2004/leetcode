class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen = set()
        unique_count = 0
        operations = 0

        # Traverse from right to left
        for index in range(len(nums)-1,-1,-1):
            if nums[index] in seen:
                operations = len(nums) - unique_count
                break
            else:
                seen.add(nums[index])
                unique_count += 1

        # Calculate required operations
        if operations % 3 == 0:
            return operations // 3
        return operations // 3 + 1