class Solution:
    def convertDateToBinary(self, date: str) -> str:
        a=int(date[:4])
        b=int(date[5:7])
        c=int(date[8:])
        x=str(bin(a))
        y=str(bin(b))
        z=str(bin(c))
        return x[2:]+'-'+y[2:]+'-'+z[2:]