class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i=0         
        c=0
        while i<len(nums)-2:
            if nums[i]==0:
                nums[i]=1
                nums[i+1]^=1
                nums[i+2]^=1
                c+=1
            i+=1
        if 0 in nums:
            return -1
        return c