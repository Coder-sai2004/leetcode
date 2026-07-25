class Solution:
    def maxProduct(self, n: int) -> int:
        ans=1
        res=[]
        while n>0:
            x=n%10
            res.append(x)
            n=n//10
        res.sort()
        return res[-1]*res[-2]