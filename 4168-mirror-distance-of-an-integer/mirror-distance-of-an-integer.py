class Solution:
    def mirrorDistance(self, n: int) -> int:
        x=str(n)[::-1]
        return abs(n-int(x))