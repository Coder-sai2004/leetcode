class Solution:
    def processStr(self, s: str) -> str:
        res=[]
        for i in s:
            if i.islower():
                res.append(i)
            elif i=="*":
                if res:
                    res.pop()
            elif i=="#":
                x="".join(res)
                y=list(x)
                res.extend(y)
            elif i=="%":
                res=res[::-1]
        return "".join(res)