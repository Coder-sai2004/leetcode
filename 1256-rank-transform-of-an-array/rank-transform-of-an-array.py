class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp={}
        temp=set(arr)
        x=sorted(list(temp))
        l={}
        rs=[]
        for i in range(len(x)):
            l[x[i]]=i+1
        for i in arr:
            if i in l.keys():
                rs.append(l[i])
        return rs