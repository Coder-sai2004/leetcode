from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s={'b':1,'a':1,'l':2,'o':2,'n':1}
        #temp is to store the instance words only
        temp=[]
        for i in text:
            if i in s:
                temp.append(i)
        #x is used to store frequency of current text,it also makes the space constant
        x=Counter(temp)
        res=float('inf')
        #calculating the number of instances
        for i in s.keys():
            val=x[i]
            t=s[i]
            m=0
            while val>=t:
                val-=t
                m+=1
            res=min(res,m)
        return res