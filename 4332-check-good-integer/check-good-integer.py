class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s=str(n)
        digitsum=0
        squaresum=0
        for i in s:
            x=int(i)
            digitsum+=x
            squaresum+=x*x
        return squaresum-digitsum>=50