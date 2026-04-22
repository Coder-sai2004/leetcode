class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for x in range(left,right+1):
            d=True
            a=str(x)
            if '0' in a:continue
            b=[int(i) for i in a]
            for i in b:
                if x%i!=0:
                    d=False
            if d:res.append(x)
        return res