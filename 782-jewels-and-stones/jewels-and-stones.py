class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x=list(jewels)
        y=list(stones)
        c=0
        for i in stones:
            if i in jewels:
                c+=1
        return c