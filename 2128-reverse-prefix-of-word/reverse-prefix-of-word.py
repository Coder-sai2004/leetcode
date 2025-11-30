class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        i=word.index(ch)+1
        x=list(word)
        y=[]
        y[:]=x[:i][::-1]+x[i:]
        return "".join(y)