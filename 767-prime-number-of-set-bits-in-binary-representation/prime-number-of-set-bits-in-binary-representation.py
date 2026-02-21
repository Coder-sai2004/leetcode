class Solution:
    def count(self,n):
        t=bin(n)[2:]
        return t.count('1')
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c=0
        s={2,3,5,7,11,13,17,19}
        for i in range(left,right+1):
            x=self.count(i)
            if x in s:
                c+=1
        return c