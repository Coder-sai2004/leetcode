class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        t=0
        for j in range(1,k+1):
            x=(t*10+1)%k
            if x==0:
                return j
            t=x
        return -1