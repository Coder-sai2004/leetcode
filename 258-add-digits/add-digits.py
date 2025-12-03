class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        c=0
        if len(s)==1:
            return int(s)
        for i in s:
            c+=int(i)
        num=c
        return self.addDigits(num)