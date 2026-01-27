class Solution:
    def scoreBalance(self, s: str) -> bool:
        x=[]
        lsum=0
        rsum=0
        for i in s:
            x.append(ord(i)-96)
        for i in range(len(x)-1):
            lsum+=x[i]
            rsum=sum(x)-lsum
            if lsum==rsum:
                return True
        return False