class Solution:
    def totalMoney(self, n: int) -> int:
        c=0
        if n<=7:
            for i in range(1,n+1):
                c+=i
            return c
        else:
            m,count=(n//7)+2,0
            for i in range(1,m):
                for j in range(i,i+7):
                    c+=j
                    count+=1
                    if count==n:
                        return c