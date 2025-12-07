class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        x=[]
        y=set(nums)
        i=min(nums)
        j=max(nums)+1
        for k in range(i,j):
            if k not in y:
                x.append(k)
        return x