class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        t1=""
        t2=""
        for i in s:
            if i==y:
                t1+=i
            else:
                t2+=i
        return t1+t2