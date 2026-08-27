from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s=set(banned)
        ans=''
        res=[]
        for i in range(len(paragraph)):
            if paragraph[i].isalpha():
                ans+=paragraph[i].lower()
            else:
                if ans!='' and ans not in s:
                    res.append(ans)
                ans=''
        if ans and ans not in s:
            res.append(ans)
        temp=Counter(res)
        mx=max(temp.values())
        for key,val in temp.items():
            if val==mx:
                return key