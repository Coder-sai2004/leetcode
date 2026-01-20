class Solution:
    def validStrings(self, n: int) -> List[str]:
        x=2**n
        s=''
        res=[]
        b=False
        for y in range(x):
            bi=format(y,f'0{n}b')
            s=str(bi)
            for i in range(len(s)-1):
                b=False
                if s[i]=='0' and s[i+1]=='0':
                    b=True
                    break
            if not b:
                res.append(s)
        return res