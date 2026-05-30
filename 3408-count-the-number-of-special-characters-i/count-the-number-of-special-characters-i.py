class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set(word)
        c=0
        for i in s:
            if i.islower() and i.upper() in s:
                c+=1
        return c