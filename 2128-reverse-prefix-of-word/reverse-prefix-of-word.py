class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack=[]
        found=False
        for i in word:
            stack.append(i)
            if i==ch:
                found=True
                break
        if not found:
            return word
        pre=""
        while stack:
            pre+=stack.pop()
        suffix=word[len(pre):]
        return pre+suffix