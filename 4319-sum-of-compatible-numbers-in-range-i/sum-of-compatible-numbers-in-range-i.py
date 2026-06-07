class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        x=max(n-k,0)
        s=0
        while abs(n-x)<=k:
            if n&x==0:
                s+=x
            x+=1
        return s