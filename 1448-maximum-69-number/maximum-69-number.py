class Solution:
    def maximum69Number (self, num: int) -> int:
        x=list(str(num))
        y=''
        r=[]
        r.append(num)
        for i in range(len(x)):
            if x[i]=='6':
                x[i]='9'
                y=int("".join(x))
                r.append(y)
                x[i]='6'
        return max(r)