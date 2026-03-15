class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        if n<1000:
            return 0
        elif n>999 and n<=100000:
            c=n-999
        return c