class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
                x = sum([int(j) for j in str(nums[i])])
                if x == i:
                    return i
        return -1