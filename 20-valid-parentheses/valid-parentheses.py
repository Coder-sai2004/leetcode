class Solution:
    def isValid(self, s: str) -> bool:
        b={'}':'{',']':'[',')':'('}
        st=[]
        for i in s:
            if i=='{' or i=='[' or i=='(':
                st.append(i)
            else:
                if len(st)==0:
                    return False
                elif st[-1]==b[i]:
                    st.pop()
                else:
                    return False
        if len(st)==0:
            return True
        return False