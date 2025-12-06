class Solution:
    def convertToBase7(self, num: int) -> str:
        x=abs(num)
        if num==0:
            return "0"
        s=''
        if x>0:
            while x>0:
                s+=str(x%7)
                x=x//7
        if num<0:
            s+='-'
            return s[::-1]
        return s[::-1]