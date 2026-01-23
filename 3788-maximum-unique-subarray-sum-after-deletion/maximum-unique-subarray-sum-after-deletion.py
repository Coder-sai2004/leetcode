class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s=0
        r=[]
        for i in nums:
            if i>0:
                r.append(i)
        if len(r)==0:
            return max(nums)
        return sum(set(r))