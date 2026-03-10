class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v=0
        c=0
        for i in s:
            if i in 'aeiou':
                v+=1
            elif i not in 'aeiou' and i.isalpha():
                c+=1
        if c>0:
            return v//c
        return 0