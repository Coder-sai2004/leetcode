class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        res=0
        m=0
        c=0
        while j<len(nums):
            if nums[j]==0 and c==k:
                while c==k:
                    res=max(res,m)
                    if nums[i]==1:
                        m-=1
                    else:
                        m-=1
                        c-=1
                    i+=1
            elif nums[j]==0:
                c+=1
                m+=1
                j+=1
            elif nums[j]==1:
                m+=1
                j+=1
            
        res=max(res,m)
        return res