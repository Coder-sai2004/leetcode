class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        res=[]
        for i in range(len(asteroids)-1,-1,-1):
            if asteroids[i]>0:
                b=True
                while st and abs(st[-1])<=asteroids[i]:
                    if abs(st[-1])<asteroids[i]:
                        st.pop()
                    elif abs(st[-1])==asteroids[i]:
                        st.pop()
                        b=False
                        break 
                if len(st)==0 and b:
                    res.append(asteroids[i])
            elif asteroids[i]<0:
                st.append(asteroids[i])
        return st[::-1]+res[::-1]