class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre=[nums[0]]
        for i in range(1,len(nums)):
            a=pre[i-1]+nums[i]
            pre.append(a)
        n=len(pre)-1
        l=r=0
        if l==pre[n]-pre[0]:
            return 0
        for i in range(1,n):
            if pre[i-1]==pre[n]-pre[i]:
                return i
        if pre[n-1]==r:
            return n
        return -1