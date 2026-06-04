class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        w=0
        for i in range(num1,num2+1):
            x=list(str(i))
            for j in range(1,len(x)-1):
                prev=x[j-1]
                cur=x[j]
                nex=x[j+1]
                if (prev<cur and nex<cur) or (prev>cur and nex>cur):
                    w+=1
        return w