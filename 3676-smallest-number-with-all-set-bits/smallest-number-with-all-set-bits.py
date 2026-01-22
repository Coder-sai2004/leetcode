class Solution:
    def smallestNumber(self, n: int) -> int:
            x=bin(n)[2:]
            y=len(x)
            return 2**y-1