class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res=[]
        for i in range(1,n+1):
            res.append(str(i))
        ans=sorted(res,key=tuple)
        result=[int(i) for i in ans]
        return result