class Solution:
    def sortSentence(self, s: str) -> str:
        i=0
        res=[]
        t=' '
        ans=''
        while i<len(s):
            if s[i].isdigit():
                res.append((s[i],t))
                t=''
            else:
                t+=s[i]
            i+=1
        res=sorted(res)
        for x in res:
            ans+=x[1]
        return ans[1:]