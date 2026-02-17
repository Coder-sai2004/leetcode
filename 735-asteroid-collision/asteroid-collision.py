class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        arr=asteroids
        st=[]
        res=[]
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>0:
                b=True
                while st and abs(st[-1])<=arr[i]:
                    if abs(st[-1])<arr[i]:
                        st.pop()
                    elif abs(st[-1])==arr[i]:
                        st.pop()
                        b=False
                        break 
                if len(st)==0 and b:
                    res.append(arr[i])
            elif arr[i]<0:
                st.append(arr[i])
        return st[::-1]+res[::-1]