class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        x=[i for i in s if i.isalpha()]
        x=x[::-1]
        i=0
        y=list(s)
        for j in range(len(y)):
            if y[j].isalpha():
                y[j]=x[i]
                i+=1
        return "".join(y)