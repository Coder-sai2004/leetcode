class Solution:
    def minimumPushes(self, word: str) -> int:
        ans=0
        n=len(word)
        i=1
        while n>8:
            ans+=8*i
            n-=8
            i+=1
        ans+=n*i
        return ans