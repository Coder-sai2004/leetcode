from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq=Counter(word)
        w=''.join(k for k,v in sorted(freq.items(),key=lambda x:x[1],reverse=True))
        count=0
        push=1
        ans=0
        for ch in w:
            count+=1
            ans+=freq[ch]*push
            if count%8==0:
                push+=1
        return ans