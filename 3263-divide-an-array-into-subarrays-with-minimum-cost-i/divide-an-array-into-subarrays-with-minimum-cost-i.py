class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a=nums[0]
        nums.remove(a)
        nums.sort()
        b=nums[0]
        c=nums[1]
        return a+b+c