class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        m=len(candyType)//2
        n=len(set(candyType))
        if n<m:
            return n
        return m