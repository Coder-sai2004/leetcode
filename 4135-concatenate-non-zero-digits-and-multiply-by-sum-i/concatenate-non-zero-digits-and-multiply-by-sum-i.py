class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=0
        x=''
        st=str(n)
        for i in st:
            if int(i)>0:
                s+=int(i)
                x+=i
        if s==0:
            return 0
        return int(x)*s