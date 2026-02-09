class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        st=[]
        for i in range(1,n+1):
            res.append("Push")
            st.append(i)
            if st==target:
                return res
            if i not in target:
                res.append("Pop")
                st.pop()
        return res