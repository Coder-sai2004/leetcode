from collections import defaultdict
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        c=defaultdict(list)
        n=len(s)
        for i in range(n):
            c[s[i]].append(cost[i])
        res=[]
        for x in c.values():
            res.append(sum(x))
        res.remove(max(res))
        return sum(res)