class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        mi=min(s)
        mx=max(s)
        if mi-1>0 or mx<0:
            return 1
        for i in range(1,mx+1):
            if i not in s:
                return i
        return mx+1