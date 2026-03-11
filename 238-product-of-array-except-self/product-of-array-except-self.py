class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1]*n
        suf=[1]*n
        res=[0]*n
        i=0
        j=n-1
        while i<n:
            pre[i]=nums[i]*(1 if i==0 else pre[i-1])
            suf[j]=nums[j]*(1 if j==n-1 else suf[j+1])
            i+=1
            j-=1
        for k in range(n):
            a=1 if k==0 else pre[k-1]
            b=1 if k==n-1 else suf[k+1]
            res[k]=a*b
        return res