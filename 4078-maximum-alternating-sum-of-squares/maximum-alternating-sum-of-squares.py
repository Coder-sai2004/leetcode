class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        positive_sum = 0
        negative_sum = 0

        # Convert negative numbers to positive
        nums = [-nums[i] if nums[i] < 0 else nums[i] for i in range(len(nums))]
        nums.sort()

        # Process elements from both ends
        while left <= right:
            if left == right:
                positive_sum += nums[right] ** 2
            else:
                positive_sum += nums[right] ** 2
                negative_sum += nums[left] ** 2

            left += 1
            right -= 1
        
        print(positive_sum,negative_sum)

        return positive_sum - negative_sum