class Solution:
    def checkDivisibility(self, n: int) -> bool:
        val=n
        a=0
        b=1
        
        while n>0:
            a+=n%10
            b*=n%10
            n=n//10

        if val%(a+b)==0:
            return True
        return False