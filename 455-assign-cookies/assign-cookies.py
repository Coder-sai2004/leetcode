class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()
        c = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                c += 1
                i += 1
                j += 1
            else:
                j += 1
        return c