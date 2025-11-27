class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            x=nums.count(i)
            while x>1:
                nums.remove(i)
                x=x-1
        return len(nums)