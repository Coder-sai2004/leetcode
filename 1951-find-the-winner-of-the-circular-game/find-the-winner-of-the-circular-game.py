class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res=[i for i in range(1,n+1)]
        i=-1
        c=0
        while len(res)>1:
            i+=1
            c+=1
            if c==k:
                res.pop(i)
                c=0
                i-=1
            if res[i]==res[-1]:
                i=-1
        return res[0]