from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        x=defaultdict(list)
        m=float('inf')

        for i in range(len(nums)):
            x[nums[i]].append(i)

        for sub in x.values():
            if len(sub)>=3:
                i=0
                j=1
                k=2
                while k<len(sub):
                    cur=abs(sub[j]-sub[i])+abs(sub[k]-sub[j])+abs(sub[k]-sub[i])
                    m=min(m,cur)
                    i+=1
                    j+=1
                    k+=1

        if m==float('inf'):
            return -1
        return m