class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        elif numRows==2:
            left=''
            right=''
            for i in range(len(s)):
                if i%2==0:
                    left+=s[i]
                else:
                    right+=s[i]
            return left+right



        col=0
        n=len(s)
        k=0
        z=numRows-2
        while n>0:
            if k%2==0:
                if n>=numRows:
                    n-=numRows
                else:
                    n-=n
                col+=1
                    
            else:
                if n>=z:
                    col+=z
                    n-=z
                else:
                    col+=n
                    n-=n
            k+=1

        res=[[0]*col for _ in range(numRows)]
        for x in res:
            print(x)

        i=0
        j=0
        b1=True
        b2=False
        c=0

        for ch in s:
            if i<numRows and b1:
                res[i][j]=ch
                i+=1
        
            if c<z and b2:
                res[i][j]=ch
                i-=1
                j+=1
                c+=1
            
            if c==z:
                b1=True
                b2=False
                c=0

            if i==numRows:
                i-=2
                j+=1
                b1=False
                b2=True
        
        ans=''
        for i in range(len(res)):
            for j in range(len(res[0])):
                if res[i][j]!=0:
                    ans+=res[i][j]
        return ans