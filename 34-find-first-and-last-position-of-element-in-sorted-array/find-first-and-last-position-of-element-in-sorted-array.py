class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,i,j=[],0,len(nums)
        if len(nums)==1 and target not in nums:
            return [-1,-1]
        while i<j:
            if nums[i]==target:
                l.append(i)
            i+=1
        if len(l)==0:
            return [-1,-1]
        return [min(l),max(l)]