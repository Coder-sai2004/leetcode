class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        j=0
        for i in range(n):
            if nums[i]>0:
                x=i+nums[i]
                idx=x%n
            elif nums[i]<0:
                x=i+nums[i]
                if -1<x<n:
                    idx=x
                else:
                    idx=-(abs(x)%n)
            else:
                idx=i
            res[j]=nums[idx]
            j+=1
        return res