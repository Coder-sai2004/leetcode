class Solution:
    def minCost(self, n: int) -> int:
        ans = 0
        for i in range(n):
            ans += i
        return ans