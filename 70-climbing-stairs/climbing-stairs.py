class Solution:
    def climbStairs(self, n: int) -> int:
        res=[1,2,3]
        for i in range(4,n+1):
            res.append(res[i-2]+res[i-3])
        return res[n-1]