class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        res=0
        for x in queries:
            l=x[0]
            r=x[1]
            k=x[2]
            v=x[3]
            idx=l
            while idx<=r:
                nums[idx]=(nums[idx]*v)%(10**9+7)
                idx+=k
        for i in nums:
            res^=i
        return res