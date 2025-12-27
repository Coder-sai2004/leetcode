import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        for i in range(1,n+1):
            res.append(i)
        x=list(itertools.combinations(res,k))
        return x