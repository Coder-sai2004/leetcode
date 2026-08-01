class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s>9*n:
            return -1
        else:
            ans=''
            while s>8:
                ans+=str('9')
                s-=9
                n-=1
            if n>0:
                ans+=str(s)
                n-=1
                ans+=('0')*n
            return int(ans)