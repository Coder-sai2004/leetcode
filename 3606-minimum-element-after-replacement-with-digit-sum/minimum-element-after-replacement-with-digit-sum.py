class Solution:
    def minElement(self, nums: List[int]) -> int:
        res=[0]*len(nums)
        n=max(nums)
        l=len(str(n))
        for i in range(l):
            for j in range(len(nums)):
                res[j]+=nums[j]%10
                nums[j]=nums[j]//10
        return min(res)