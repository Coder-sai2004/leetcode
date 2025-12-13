class Solution:
    def arrangeCoins(self, n: int) -> int:
        x,c=1,0
        while n>=x:
            c+=1
            n-=x
            x+=1
        return c