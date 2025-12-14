class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res=[]
        s=set(groupSizes)
        for i in s:
            a=[]
            for j in range(len(groupSizes)):
                if i==groupSizes[j]:
                    a.append(j)
            res.append(a)
        l=list(s)
        y=[]
        for g in range(len(l)):
            m=0
            n=l[g]
            o=n
            temp=res[g]
            while n<len(temp)+1:
                k=temp[m:n]
                m+=o
                n+=o
                y.append(k)
        return y
            