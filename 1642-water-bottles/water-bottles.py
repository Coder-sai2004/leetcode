class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        x=numBottles
        y=numExchange
        s=0
        s=x
        while x>=y:
            ex=x//y
            re=x%y
            s+=ex
            x=ex+re
        return s