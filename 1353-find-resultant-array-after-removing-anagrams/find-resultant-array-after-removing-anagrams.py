class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        x=[]
        x=words
        r=[]
        r.append(x[0])
        for i in range(1,len(x)):
            if sorted(x[i])!=sorted(x[i-1]):
                r.append(x[i])
            elif sorted(x[i])==sorted(x[i-1]):
                continue
            else:
                r.append(x[i])
        return r