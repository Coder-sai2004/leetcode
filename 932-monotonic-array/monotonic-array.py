class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        x=sorted(nums)
        if nums==x:
            return True
        elif nums==x[::-1]:
            return True
        return False