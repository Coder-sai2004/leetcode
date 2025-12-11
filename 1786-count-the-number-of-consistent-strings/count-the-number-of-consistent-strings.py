class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c,s=0,set(allowed)
        for x in words:
            j=0
            b=False
            while j<len(x):
                if x[j] in s:
                    b=True
                    j+=1
                else:
                    b=False
                    break
            if b:
                c+=1
        return c