class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        r = 0
        l = 0

        for i in range(len(s)):
            if s[i] == 'R':
                r += 1
            elif s[i] == 'L':
                l += 1

            if r == l:
                count += 1
                r = 0
                l = 0
        
        return count