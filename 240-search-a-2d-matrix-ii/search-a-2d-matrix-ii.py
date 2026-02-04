class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res=[]
        for x in matrix:
            res.extend(x)
        print(res)
        if target in res:
            return True
        return False