from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        #counting frequency of each character
        x=Counter(s)
        r=''
        #sorting the characters based on frequency
        x=sorted(x.items(),key=lambda x: x[1],reverse=True)
        for i,j in x: 
            r+=(i*j)
        return r