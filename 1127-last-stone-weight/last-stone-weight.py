import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        h=[]
        stones=[-i for i in stones]
        for i in stones:
            heapq.heappush(h,i)
        
        while len(h)>1:
            x=heapq.heappop(h)
            y=heapq.heappop(h)
            x=-x
            y=-y
            if x!=y:
                z=abs(x-y)
                heapq.heappush(h,-z)
        
        if h:
            return -h[0]
        return 0