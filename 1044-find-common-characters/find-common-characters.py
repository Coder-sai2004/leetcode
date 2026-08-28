from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=[Counter(w) for w in words]
        s=res[0]
        t=set()
        ans=[]
        for i in range(1,len(res)):
            target=res[i]
            for k in s.keys():
                if k in target:
                    s[k]=min(s[k],target[k])
                else:
                    t.add(k)
        for k,v in s.items():
            if k not in t:
                for _ in range(v):
                    ans.append(k)
        return ans