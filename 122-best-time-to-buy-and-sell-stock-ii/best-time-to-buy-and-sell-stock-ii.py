class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=1
        res=0
        while i<len(prices):
            if prices[i]>prices[i-1]:
                res+=(prices[i]-prices[i-1])
            i+=1
        return res