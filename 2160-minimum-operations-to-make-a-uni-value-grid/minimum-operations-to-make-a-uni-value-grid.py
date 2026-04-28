class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        #res is for taking all elements into a list
        #temp is for taking difference between m and other values
        res=[]
        temp=[]
        c=0
        for n in grid:
            res.extend(n)
        res.sort()

        #m is the index of the value, which we are converting all elements into that
        m=len(res)//2
        for i in res:
            temp.append(abs(i-res[m]))

        #counting the no of operations needed
        for j in temp:
            if j%x!=0:
                return -1
            else:
                y=j//x
                c+=y
        return c