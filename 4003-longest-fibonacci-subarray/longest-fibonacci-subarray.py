from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        c=2
        m=2
        for i in range(2,n):
            if nums[i]==nums[i-1]+nums[i-2]:
                c+=1
                m=max(m,c)
            else:
                c=2
        return m