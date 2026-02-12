class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        idx=[]
        res=[]
        for i in range(len(nums)):
            if nums[i]==x:
                idx.append(i)
        n=len(idx)
        for i in queries:
            if i<=n:
                res.append(idx[i-1])
            else:
                res.append(-1)
        return res