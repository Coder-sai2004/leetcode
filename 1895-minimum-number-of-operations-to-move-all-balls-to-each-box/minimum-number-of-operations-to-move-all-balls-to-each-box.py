class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        p=[]
        for s in range(len(boxes)):
            p.append(s)
        x=list(boxes)
        pr=[]
        for v in range(len(x)):
            if x[v]=='1':
                pr.append(v)
        rs=[]
        res=0
        for i in range(len(p)):
            res=0
            a=p[i]
            for j in pr:
                if j>a:
                    res+=j-a
                else:
                    res+=a-j
            rs.append(res)
        return rs