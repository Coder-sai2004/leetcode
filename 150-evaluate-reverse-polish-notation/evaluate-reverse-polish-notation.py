class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        op={'+','-','*','/'}
        for i in range(len(tokens)):
            if tokens[i] in op:
                x=st.pop()
                y=st.pop()
                if tokens[i]=='+':
                    z=y+x
                elif tokens[i]=='-':
                    z=y-x
                elif tokens[i]=='*':
                    z=y*x
                else:
                    z=int(y/x)
                st.append(z)
            else:
                st.append(int(tokens[i]))
        return st[-1]