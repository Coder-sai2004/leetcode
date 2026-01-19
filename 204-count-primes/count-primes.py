class Solution:
    def countPrimes(self, n: int) -> int:
        arr=[True]*(n+1)
        if n==0 or n==1:
            return 0
        arr[0]=arr[1]=arr[n]=False
        for i in range(2,int(n**0.5)+1):
            for j in range(i*i,n+1,i):
                arr[j]=False
        return arr.count(True)