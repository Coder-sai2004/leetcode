class Solution:
    def reverseWords(self, s: str) -> str:
        l=list(s)
        temp=[]
        result=[]
        for i in range(len(l)):
            if l[i]==' ':
                result.extend(temp[::-1])
                result.append(' ')
                temp.clear()
                continue
            temp.append(l[i])
        if temp:
            result.extend(temp[::-1])
        return "".join(result)