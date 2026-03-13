class Solution:
    def clearDigits(self, s: str) -> str:
        res=[]
        for ch in s:
            if ch.isdigit():
                res.pop()
            else:
                res.append(ch)
        return "".join(res)