class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        d=set()
        for i in range(len(s)-k+1):
            d.add(s[i:i+k])
        for i in range(2**k):
            x=bin(i)[2:]
            y=x.zfill(k)
            if y not in d:
                return False 
        return True