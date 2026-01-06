class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            if i%10==nums[i]:
                l.append(i)
        if len(l)>0:
            return min(l)
        else:
            return -1