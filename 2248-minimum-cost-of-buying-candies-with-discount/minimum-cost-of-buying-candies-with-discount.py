class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n=len(cost)
        if n<3:
            return sum(cost)
        cost=sorted(cost)[::-1]
        i=0
        res=0
        while i+2<n:
            if cost[i]<=cost[i+1] and cost[i]<=cost[i+2]:
                res+=(cost[i+1]+cost[i+2])

            elif cost[i+1]<=cost[i] and cost[i+1]<=cost[i+2]:
                res+=(cost[i]+cost[i+2])

            elif cost[i+2]<=cost[i+1] and cost[i+2]<=cost[i]:
                res+=(cost[i+1]+cost[i])

            if n-(i+3)<3:
                res+=sum(cost[i+3:])
            i+=3
        
        return res