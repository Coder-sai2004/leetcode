class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        x=sorted(score)[::-1]
        d1={}
        l=[]
        c=4
        d1[x[0]]="Gold Medal"
        if len(score)==1:
            l.append(d1[x[0]])
        elif len(score)==2:
            d1[x[1]]="Silver Medal"
            for i in score:
                l.append(d1[i])
        elif len(score)>=3:
            b=x[3:len(x)]
            d1[x[1]]="Silver Medal"
            d1[x[2]]="Bronze Medal"
            for i in b:
                d1[i]=str(c)
                c+=1
            for j in score:
                l.append(d1[j])
        return l