class Solution:
    def minimumFlips(self, n: int) -> int:
        f=0
        x=format(n,'b')
        y=x[::-1]
        for i in range(len(x)):
            if x[i]!=y[i]:
                f+=1
        return f