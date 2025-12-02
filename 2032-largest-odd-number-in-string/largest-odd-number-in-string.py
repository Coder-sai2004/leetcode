class Solution:
    def largestOddNumber(self, num: str) -> str:
        s=[]
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                s=num[:i+1]
                break
        if len(s)==0:
            return ""
        return s