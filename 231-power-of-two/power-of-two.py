class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0:
            x=str(bin(n))
            temp=[i for i in x]
            c=x.count('1')
            if c==1:
                return True
        return False