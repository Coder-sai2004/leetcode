class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x={}
        y=''
        for i in range(len(s)):
            x[indices[i]]=s[i]
        for j in range(len(x)):
            y+=x[j]
        return y