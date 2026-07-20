class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        c=0
        while l<r:
            if nums[l]+nums[r]<target:
                c+=(r-l)
                l+=1
            elif nums[l]+nums[r]>=target:
                r-=1
        return c