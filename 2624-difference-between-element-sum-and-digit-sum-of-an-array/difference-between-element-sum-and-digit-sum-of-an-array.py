class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        s = ''
        for i in nums:
            s += str(i)
        
        digit = 0
        for i in s:
            digit += int(i)
        
        return sum(nums) - digit