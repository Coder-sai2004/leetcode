class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n=len(piles)-(len(piles)//3)
        ans=0
        for i in range(1,n,2):
            ans+=piles[i]
        return ans