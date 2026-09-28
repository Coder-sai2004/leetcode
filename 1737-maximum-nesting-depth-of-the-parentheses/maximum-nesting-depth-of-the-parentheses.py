class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        cur = 0
        for i in s:
            if i == '(':
                cur += 1
                ans = max(ans,cur)
            elif i ==')':
                cur -= 1
        return ans