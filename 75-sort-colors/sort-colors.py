class Solution:
    def sortColors(self, nums: List[int]) -> None:
        z=nums.count(0)
        o=nums.count(1)
        t=nums.count(2)
        for i in range(len(nums)):
            if i<z:
                nums[i]=0
            elif i>=z and i<(z+o):
                nums[i]=1
            else:
                nums[i]=2
        return nums