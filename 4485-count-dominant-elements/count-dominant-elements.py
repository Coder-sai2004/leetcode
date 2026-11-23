class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        ans = 0
        
        if len(nums) == 1:
            return 1
        
        if nums[0] >= nums[1]:
            ans += 1
        
        if nums[-1] >= nums[-2]:
            ans += 1
        
        for i in range(1,len(nums) - 1):
            avg = (nums[i - 1] + nums[i + 1]) / 2

            if nums[i] >= avg:
                ans += 1
        
        return ans