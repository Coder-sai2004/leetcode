class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n=columnNumber
        s=""
        while n>0:
            n-=1
            s=chr((n%26)+65)+s
            n=n//26
        return s