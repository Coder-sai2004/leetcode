class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        if x>0:
            if int(s[::-1])>(2**31)-1:
                return 0
            else:
                return int(s[::-1])
        else:
            x=''
            for i in range(1,len(s)):
                x+=s[i]
            x=x[::-1]
            if int(s[0]+x)<(-2**31):
                return 0
            else:
                return int(s[0]+x)
        return 0