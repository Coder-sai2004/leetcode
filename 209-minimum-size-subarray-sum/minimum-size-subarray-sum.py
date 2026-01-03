class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        c=False
        s=0
        res=float('inf')
        while j<len(nums)+1:
            while(s>=target):
                res=min(res,(j-i))
                s-=nums[i]
                c=True
                i+=1
            if j==len(nums):
                break
            s+=nums[j]
            j+=1
        if res and c:
            return res
        return 0