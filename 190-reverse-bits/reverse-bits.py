class Solution:
    def reverseBits(self, n: int) -> int:
        x=bin(n)[2:]
        t=''
        k=32-len(x)
        while k!=0:
            t+='0'
            k-=1
        s=t+x
        y=s[::-1]
        return int(y,2)