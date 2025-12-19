from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=set(ransomNote)
        b=set(magazine)
        x=Counter(ransomNote)
        y=Counter(magazine)
        for i in a:
            if x[i]>y[i]:
                return False
        return True