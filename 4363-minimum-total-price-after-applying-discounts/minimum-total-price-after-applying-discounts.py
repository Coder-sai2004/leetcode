class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        price=sorted(prices,reverse=True)
        dis=sorted(discounts,reverse=True)
        ans=0
        j=0
        m=min(len(price),len(dis))
        while j<m:
            val=(price[j]*(100-dis[j]))/100
            j+=1
            ans+=val
        while j<len(price):
            ans+=price[j]
            j+=1
        return ans