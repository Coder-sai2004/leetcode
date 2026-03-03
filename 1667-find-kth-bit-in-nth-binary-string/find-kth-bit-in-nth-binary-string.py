class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        res=["0"]
        for i in range(1,n):
            temp=res[i-1][::-1]
            x=''
            for j in range(len(temp)):
                if temp[j]=='1':
                    x+='0'
                else:
                    x+='1'
            a=res[i-1]+"1"+x
            res.append(a)
        return res[n-1][k-1]