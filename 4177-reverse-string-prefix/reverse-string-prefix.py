class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        x=list(s)
        y=x[:k][::-1]+x[k:]
        return "".join(y)