class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        res=[]
        for i in range(len(names)):
            d[heights[i]]=names[i]
        x=sorted(d.items(),key=lambda x: x[0],reverse=True)
        for name in x:
            res.append(name[1])
        return res