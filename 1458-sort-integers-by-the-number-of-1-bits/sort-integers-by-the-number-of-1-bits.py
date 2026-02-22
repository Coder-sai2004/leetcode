from collections import defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res=defaultdict(list)
        ans=[]
        for i in arr:
            a=format(i,'b')
            t=a.count('1')
            res[t].append(i)
        y=sorted(res.items(),key=lambda x:x[0])
        for x in y:
            ans.extend(sorted(x[1]))
        return ans