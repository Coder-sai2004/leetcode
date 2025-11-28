class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        rs=set()
        for i in s:
            if i>0:
                rs.add(i)
        if len(rs)==0:
            return 1
        x=max(rs)
        for i in range(1,x+1):
            if i not in rs:
                return i
        return x+1