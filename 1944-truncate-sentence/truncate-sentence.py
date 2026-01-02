class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        x=[i for i in s.split(" ")]
        r=''
        for j in range(k):
            r+=x[j]
            r+=' '
        return r.strip()