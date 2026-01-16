class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        x=[]
        y=[]
        for i in range(1,n+1):
            if i%m==0:
                x.append(i)
            else:
                y.append(i)
        return sum(y)-sum(x)