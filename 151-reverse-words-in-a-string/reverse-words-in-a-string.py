class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.strip()
        z=[w for w in x.split(' ')]
        y=z[::-1]
        result=" ".join(y)
        return " ".join(result.split())