class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0: return 1
        p=0
        x=2**p
        while x<=n:
            p+=1
            x=2**p
        return n^(x-1)