class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        x=list(map(int,s))
        y=len(x)-2
        temp=[]
        for i in range(y+1):
            temp[:]=x
            x[:]=[]
            for j in range(len(temp)-1):
                b=(temp[j]+temp[j+1])%10
                x.append(b)
        if temp[0]==temp[1]:
            return True
        else:
            return False