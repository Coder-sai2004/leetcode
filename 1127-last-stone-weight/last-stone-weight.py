class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)!=1:
            a=max(stones)
            stones.remove(a)
            b=max(stones)
            stones.remove(b)
            x=abs(a-b)
            stones.append(x)
        if stones:
            return stones[0]
        return 0