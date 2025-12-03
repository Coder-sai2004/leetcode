class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=0
        for i in sentences:
            x=[word for word in i.split()]
            if len(x)>c:
                c=len(x)
        return c