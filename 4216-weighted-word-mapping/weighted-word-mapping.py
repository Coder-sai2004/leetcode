class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alpha={}
        x='z'
        y='a'
        current_words={}
        ans=''
        for i in range(26):
            alpha[i]=x
            x=chr(ord(x)-1)
        for i in range(len(weights)):
            current_words[y]=weights[i]
            y=chr(ord(y)+1)
        for w in words:
            cur_sum=0
            for j in w:
                cur_sum+=current_words[j]
            idx=cur_sum%26
            ans+=alpha[idx]
        return ans