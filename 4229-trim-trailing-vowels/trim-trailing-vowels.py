class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        idx=len(s)
        i=len(s)-1
        while i>-1:
            if s[i] in 'aeiou':
                idx-=1
                i-=1
            else: break
        return s[:idx]