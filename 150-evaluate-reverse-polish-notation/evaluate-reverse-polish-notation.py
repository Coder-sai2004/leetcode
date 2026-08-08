class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        #this op set determines which operations need to be done
        op={'+','-','*','/'}
        for i in range(len(tokens)):
            if tokens[i] in op:
                #we are taking the top two elements for the operation
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
                #appending the integer values to the stack
                st.append(int(tokens[i]))
        return st[-1]